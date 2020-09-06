#!/usr/bin/python3
import os
import sys
import fcntl
import tty
import termios
import socket
import select

PORT = 9999
def droidKeyboardClient(serverIp):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# making stdin non-blocking
	fd = sys.stdin.fileno()
	fl = fcntl.fcntl(fd, fcntl.F_GETFL)
	fcntl.fcntl(fd, fcntl.F_SETFL, fl | os.O_NONBLOCK)
	# tty settings for one char input
	ttyAtributes = termios.tcgetattr(fd)
	tty.setraw(fd)
	while (True): # blocking for ever
		(rfds, wfds, xfds) = select.select([sys.stdin], [], [], 20)
		if (rfds == []):
			print('Timeout\r')
			break
		keyBytes = bytearray(sys.stdin.read(8).encode())
		keyInt = int.from_bytes(keyBytes, byteorder=sys.byteorder)
		print('keyInt: 0x%X\r' %(keyInt))
		sys.stdin.flush()
		sys.stdout.flush()
		sock.sendto(keyBytes, (serverIp, PORT))
	# revert the tty setting if needed
	termios.tcsetattr(fd, termios.TCSADRAIN, ttyAtributes)
	fcntl.fcntl(fd, fcntl.F_SETFL, fl)
	return(True)

def main():
	serverIp = sys.argv[1]
	ret = droidKeyboardClient(serverIp)
	return(ret)

if (__name__ == '__main__'):
	ret = main()
	sys.exit((1, 0)[ret])
