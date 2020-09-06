#!/usr/bin/python
import os
import sys
import thread
import time
import ctypes

import os
import sys
import time

def f():
	for i in range(10):
		pd('Thread: %d', i)
		time.sleep(1)

def main():
	threadId = thread.start_new_thread(f, ())
	pv(threadId)
	time.sleep(5)
	pthread = ctypes.cdll.LoadLibrary('libpthread.so.0')
	pthread.pthread_cancel(ctypes.c_ulong(threadId))
	for i in range(5):
		pd('Main: %d', i)
		time.sleep(1)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
