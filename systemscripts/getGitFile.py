#!/usr/bin/python3
import re

import os
import sys
import time

def usage():
	pe('Usage: %s <filePathFromGitBase> <commit>', sys.argv[0])

def main():
	if (len(sys.argv) < 3):
		usage()
		return(1)
	filePath = sys.argv[1]
	commitId = sys.argv[2]
	gitCmd = ('git', 'cat-file', '-p')
	(ret, output) = runCmdGetOutput(gitCmd + (commitId,))
	if (ret != 0):
		pe('not a git repo')
		return(1)
	sha1 = re.search(b'tree\s([0-9a-f]*)', output).group(1)
	pathList = filePath.split('/')
	pv(pathList)
	for fp in pathList:
		(ret, output) = runCmdGetOutput(gitCmd + (sha1,))
		sha1 = re.search('([0-9a-f]*).%s' %(fp), output.decode()).group(1)
		pv(sha1)
	(ret, output) = runCmdGetOutput(gitCmd + (sha1,))
	newFile = '%s.%s' %(pathList[-1], commitId)
	fd = open(newFile, 'w')
	fd.buffer.write(output)
	fd.close()
	pi('Created File: %s', newFile)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
