#!/usr/bin/python
import time
import signal

def handler(signum, frame):
	print 'Signal handler called with signal', signum
	raise StandardError('script time out')

def main():
	# Set the signal handler and a 5-second alarm
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(2)
	time.sleep(3)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
