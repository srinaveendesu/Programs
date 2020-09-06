#!/usr/bin/python3

import os
import sys
import time

def dec1(funcObj):
	def func():
		try:
			print('in try1')
			ret = funcObj()
			return(ret)
		except:
			print('in except1')
			raise
		finally:
			print('in finally1')
			raise
	return(func)

def dec2(funcObj):
	def func():
		try:
			print('in try2')
			ret = funcObj()
			return(ret)
		except:
			print('in except2')
			raise
		finally:
			print('in finally2')
	return(func)

@dec1
@dec2
def main():
	i = 1/0
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
