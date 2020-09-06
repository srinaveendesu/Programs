#!/usr/bin/python3

import os
import sys
import time

clocks = [
	('IST', 0, 'GREEN'),
	('EDT', -34200, 'MAGENTA'),
]

def main():
	utc = time.time()
	for (timeZone, secDiff, color) in clocks:
		string = '%s: %s\n' %(timeZone, time.ctime(utc + secDiff))
		writeLog(string, color)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
