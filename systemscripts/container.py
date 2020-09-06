#!/usr/bin/python

class Container:
	pass

def fun(c):
	print c.name, c.ln

def main():
	c= Container()
	c.name= 'madhu'
	c.ln= 'sudhan'
	#print c.name, c.ln
	fun(c)
main()
