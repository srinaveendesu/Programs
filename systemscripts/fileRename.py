#!/usr/bin/python3

import os
import sys
import time

logFile = '/tmp/fileRename.log'
logFd = None
def log(string):
	global logFd
	if (logFd == None):
		logFd = open(logFile, 'a')
	logFd.write(string + '\n')
	return(True)

def getNewName(fname):
	import re
	fname = re.sub('\.*$', '', fname)
	if (os.path.isdir(fname)):
		newName = formatString(fname)
	else:
		t = os.path.splitext(fname)
		if (t[1] != ''):
			newName = formatString(t[0]) + '.' + formatString(t[1][1:])
		else:
			newName = formatString(fname)
	return newName

def rename(filename, newName):
	pi('Renaming: %s -> %s', filename, newName)
	os.rename(filename, newName)
	fullPath = os.path.join(os.getcwd(), filename)
	newPath = os.path.join(os.getcwd(), newName)
	log('%s|%s' %(fullPath, newPath))

def renameFile(filename):
	newName = getNewName(filename)
	if (not os.path.exists(newName)):
		rename(filename, newName)
		return(newName)
	else:
		if (newName != filename):
			pe('%s -> %s: file already exists', filename, newName)
		else:
			pd('noRenaming: %s', filename)
		return(filename)

def renameDir(dirname):
	presentWorkingDir = os.getcwd()
	dirname = os.path.realpath(dirname)
	os.chdir(dirname)
	log('ChangeDir: %s' %(dirname))
	pd('working in: %s', dirname)
	for fname in os.listdir(dirname):
		newFname = renameFile(fname)
		if (os.path.isdir(newFname)):
			renameDir(newFname)
	os.chdir(presentWorkingDir)

def findSimilarStrings(stringList):
	import difflib
	similarStringDict = {}
	for i in range(len(stringList)):
		for j in range(i+1, len(stringList)):
			string1 = stringList[i]
			string2 = stringList[j]
			pd('comparing: %s - %s', string1, string2)
			smI = difflib.SequenceMatcher(None, string1, string2)
			match = smI.get_matching_blocks()
			for (string1Point, string2Poing, size) in match:
				if (size < 4):
					continue
				foundString = string1[string1Point:string1Point+size]
				pv(foundString)
				similarStringDict[foundString] = similarStringDict.get(foundString, 0) + 1
	# sorting
	pv(similarStringDict)
	similarStrings = sorted(similarStringDict, key=lambda e: similarStringDict[e], reverse=True)
	pv(similarStrings)
	return(similarStrings)

def splitExtension(fileList):
	newFileList = []
	extList = []
	for filename in fileList:
		newFileList.append(os.path.splitext(filename)[0])
		extList.append(os.path.splitext(filename)[1])
	pv(newFileList)
	pv(extList)
	return(newFileList, extList)

def eliminatingCommonString(dirname):
	presentWorkingDir = os.getcwd()
	dirname = os.path.realpath(dirname)
	os.chdir(dirname)
	pd('working in: %s', dirname)
	fileListExt = os.listdir(dirname)
	(fileList, extList) = splitExtension(fileListExt)
	similarStrings = findSimilarStrings(fileList)
	# manual editing
	pi('dn; rn rstring; cn;')
	writeLog('\nFiles in folder: %s' %(dirname))
	writeLog('\t' + '\n\t'.join(fileList))
	if (len(similarStrings) > 0):
		writeLog('\ndetected the following junk strings:')
		for i in range(len(similarStrings) - 1, -1, -1):
			writeLog('\n\t%d: %s' %(i+1, similarStrings[i]))
		choice = readStdin('\nenter editing cmd[d#; r# <nStr>; c#; q]')
		replaceArgs = []
		for choiceCmd in choice.split(';'):
			t = choiceCmd.strip().split()
			cmd = t[0][0]
			if (cmd == 'd'):
				junkStringCount = int(t[0][1:])
				pd('Deleting: %s', similarStrings[junkStringCount-1])
				replaceArgs.append((similarStrings[junkStringCount-1], ''))
			elif (cmd == 'r'):
				junkStringCount = int(t[0][1:])
				replaceString = t[1]
				pd('Replacing: %s -> %s', similarStrings[junkStringCount-1], replaceString)
				replaceArgs.append((similarStrings[junkStringCount-1], replaceString))
			elif (cmd == 'c'):
				junkStringCount = int(t[0][1:])
				pd('Adding count at: %s', similarStrings[junkStringCount-1])
				replaceArgs.append((similarStrings[junkStringCount-1], '%d'))
			elif (cmd == 'q'):
				pd('quiting...')
				break
		# creating new filenames
		if (len(replaceArgs) > 0):
			for i in range(len(fileList)):
				newFileName = fileList[i]
				for replaceArg in replaceArgs:
					if (replaceArg[1] != '%d'):
						newFileName = newFileName.replace(replaceArg[0], replaceArg[1])
					else:
						newFileName = newFileName.replace(replaceArg[0], '%02d_' %(i+1))
				newFileName = '%s%s' %(newFileName, extList[i])
				rename(fileListExt[i], newFileName)
	else:
		pi('No similar strings found in folder: %s', dirname)
	# recursive among all the fileList
	fileListExt = os.listdir(dirname)
	for dirname in fileListExt:
		if (os.path.isdir(dirname)):
			eliminatingCommonString(dirname)
	os.chdir(presentWorkingDir)

def usage():
	pe('For Usage: %s [-h|--help]', sys.argv[0])

def parse_args():
	import optparse
	usage = 'Usage: %s [options]' %(sys.argv[0])
	parser = optparse.OptionParser(usage=usage)

	parser.add_option('-e', '--eliminate-common-string', action='store_true', \
			dest='eliminateCommonString', default=False, \
			help='helps to eliminate common string in filenames')

	options, args = parser.parse_args()
	return(options, args)

def main():
	if (len(sys.argv) < 2):
		usage()
		sys.exit(1)
	(options, args) = parse_args()
	# creation of status file for the present dir
	for fname in args:
		if (fname == '.'):
			pe('Will not support "." for current dir, use "*"')
			continue
		newFname = renameFile(fname)
		if (os.path.isdir(newFname)):
			renameDir(newFname)
			if (options.eliminateCommonString == True):
				eliminatingCommonString(newFname)
	pi('Created Log file: %s', logFile)
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
