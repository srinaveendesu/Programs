#!/usr/bin/python
import sys
import socket
import select

HOST = '0.0.0.0'
PORT = 2000

def usage():
	pe('Usage: %s <scriptPath>', sys.argv[0])

def main():
	if (len(sys.argv) < 2):
		usage()
		return(1)
	client = socket.socket()
	client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	client.connect((HOST, PORT))
	scriptPath = sys.argv[1]
	fd = open(scriptPath, 'r')
	source = fd.read()
	fd.close()
	client.send(source)
	while (True):
		output = client.recv(1024 * 20)
		if (len(output) == 0):
			break
		sys.stdout.write(output)
	client.close()
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)

