#!/usr/bin/python3

import os
import sys
import time

def getEvenNumbers(numberList):
	for num in numberList:
		if (not (num % 2)):
			yield num

def main():
	evenNumberGenerator = getEvenNumbers(range(20))
	for num in evenNumberGenerator:
		pv(num)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
