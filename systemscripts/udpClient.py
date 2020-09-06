#!/usr/bin/python3
import os
import sys
import socket

import os
import sys
import time

# if ipv6 replace,
#    AF_INET -> AF_INET6
#    localhost -> ip6-localhost 
def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024*1024)
	sock.sendto(b'message from udp client', ('localhost', 2727))
	(msg, serverAddr) = sock.recvfrom(1024)
	pv(msg)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
