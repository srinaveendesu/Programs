#!/usr/bin/python3
import ctypes

import os
import sys
import time

def main():
	fiveElementIntArrayType = ctypes.c_int * 5
	intArray = fiveElementIntArrayType(5, 1, 33, 7, 99)
	# loading c dynamic link library
	libc = ctypes.CDLL('libc.so.6')
	# c function as 'qsort()'
	qsort = libc.qsort
	qsort.restype = None
	# registering callback function, which returns 'int' and
	#+ takes two int pointer types
	CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))
	def py_cmp_func(a, b):
		print('In Callback Function: %d %d' %(a[0], b[0]))
		return (a[0] - b[0])
	cmp_func = CMPFUNC(py_cmp_func)
	# calling the c function with callback function pointer
	qsort(intArray, len(intArray), ctypes.sizeof(ctypes.c_int), cmp_func)
	# check the sorted array
	print('Sorted Array values\n')
	for element in intArray:
		print(element)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
