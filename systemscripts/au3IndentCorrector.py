#!/usr/bin/python3
import re

import os
import sys
import time

def usage():
	pe('Usage: %s <>', sys.argv[0])

def main():
	if (len(sys.argv) < 2):
		usage()
		return(1)
	for srcFile in sys.argv[1:]:
		srcFd = open(srcFile, 'r', encoding = 'ISO-8859-1')
		destFile = 'c_%s' %(srcFile)
		destFd = open(destFile, 'w')
		indentLevel = 0
		for line in srcFd:
			line = line.strip()
			if (line == ''):
				destFd.write('\n')
				continue
			# pre indent corrections
			if (re.search('^endif', line, re.IGNORECASE) != None):
				indentLevel -= 1
			if (re.search('^else', line, re.IGNORECASE) != None):
				indentLevel -= 1
			elif (re.search('^elseif', line, re.IGNORECASE) != None):
				indentLevel -= 1
			elif (re.search('^next', line, re.IGNORECASE) != None):
				indentLevel -= 1
			elif (re.search('^wend', line, re.IGNORECASE) != None):
				indentLevel -= 1
			elif (re.search('^until', line, re.IGNORECASE) != None):
				indentLevel -= 1
			elif (re.search('^case', line, re.IGNORECASE) != None):
				indentLevel -= 1
			elif (re.search('^endfunc', line, re.IGNORECASE) != None):
				indentLevel -= 1
			# writing
			destFd.write('%s%s\n' %('\t'*indentLevel, line))
			# post indent corrections
			if (re.search('^if', line, re.IGNORECASE) != None):
				line = line.split(';')[0].strip()
				if (re.search('then$', line, re.IGNORECASE)):
					indentLevel += 1
			elif (re.search('^else', line, re.IGNORECASE) != None):
				indentLevel += 1
			elif (re.search('^elseif', line, re.IGNORECASE) != None):
				indentLevel += 1
			elif (re.search('^for', line, re.IGNORECASE) != None):
				indentLevel += 1
			elif (re.search('^while', line, re.IGNORECASE) != None):
				indentLevel += 1
			elif (re.search('^select', line, re.IGNORECASE) != None):
				indentLevel += 1
			elif (re.search('^switch', line, re.IGNORECASE) != None):
				indentLevel += 1
			elif (re.search('^do', line, re.IGNORECASE) != None):
				indentLevel += 1
			elif (re.search('^func', line, re.IGNORECASE) != None):
				indentLevel += 1
			# checking the indentation
			if (indentLevel < 0):
				pe('indentLevel: %d', indentLevel)
				pe('There is some error in correcting indentation. Existing...')
				pv(line)
				break
		destFd.close()
		pi('Converted: %s', destFile)
	for srcFile in sys.argv[1:]:
		destFile = 'c_%s' %(srcFile)
		writeLog('mv -f '%s' '%s'\n' %(destFile, srcFile))
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
