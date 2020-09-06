#!/usr/bin/python
import sys
import socket
import code
import traceback

HOST = '0.0.0.0'
PORT = 2000

class sockFileObject(object):
	def __init__(self, conn):
		self.conn = conn
	def read(self, len):
		return self.conn.recv(len)
	def write(self, str):
		return self.conn.send(str)
	def close(self):
		self.conn.close()
		

def main():
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((HOST, PORT))
	while True:
		server.listen(1)
		(conn, details) = server.accept()
		connFd = sockFileObject(conn)
		source = connFd.read(1024 * 20)
		sys.stdin = connFd
		sys.stdout = connFd
		sys.stderr = connFd
		interpreter = code.InteractiveInterpreter()
		interpreter.runcode(source)
		sys.stdin = sys.__stdin__
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__
		connFd.close()

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
