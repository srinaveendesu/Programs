#!/usr/bin/env python
import os
import sys
import time

if sys.platform not in ('linux2',):
	sys.exit('%s only runs on Linux' % os.path.basename(sys.argv[0]))

# TODO: we should check that kernel version >= 2.4.19
# e.g. with 'uname -r'

import fcntl
import signal

def usage():
	print 'Usage: %s <dir>' %(sys.argv[0])

def handler(signum, frame):
	print 'Something happened; signal =', signum

def notify(directory, handler):
	fd = os.open(directory, os.O_RDONLY)
	fcntl.fcntl(fd, fcntl.F_NOTIFY, fcntl.DN_ACCESS|fcntl.DN_MODIFY|fcntl.DN_CREATE)
	signal.signal(signal.SIGIO, handler)

if __name__ == '__main__':
	if (len(sys.argv) < 2):
		usage()
		sys.exit(1)
	else:
		TESTDIRECTORY = sys.argv[1]
		notify(TESTDIRECTORY, handler)
try:
	signal.pause() # sleep until signal received
except KeyboardInterrupt:
	pass
