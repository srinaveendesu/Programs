#!/usr/bin/python
import re

import os
import sys
import time

def downloadImage(link, outFile):
	regExpr= re.compile('.*imgurl=(?P<jpgLink>[^&%]*).*')
	match= regExpr.match(link)
	if (match is not None):
		jpgLink = match.group('jpgLink')
	else:
		pe('jpgLink not found')
		return False
	pi('Downloading... : %s', outFile)
	wgetCmd = 'wget --timeout=60 '%s' -O '%s'' %(jpgLink, outFile)
	ret = runCmd(wgetCmd)
	return(ret)

def main():
	prefix = ''
	if (len(sys.argv) > 1):
		prefix = sys.argv[1] + '_'
	count = 1
	while(True):
		link = readStdin('enter the imagelink')
		if (link == 'q'):
			break
		outFile = '%s%d.jpg' %(prefix, count)
		ret = downloadImage(link, outFile)
		if (ret == 0):
			pi('Downloaded file: %s', outFile)
			count += 1
		else:
			pe('Error in Downloading file: %s', outFile)
	pi('Successfully Completed')
	return 0

if (__name__ == '__main__'):
	main()

