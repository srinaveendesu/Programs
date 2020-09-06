#!/usr/bin/python3
import hashlib

import os
import sys
import time

duplicateFolder = 'duplicateFiles'

def hashfile(filepath):
	pr('hashing: %-80s', filepath)
	sha1 = hashlib.sha1()
	fd = open(filepath, 'rb')
	#fd.seek(1024)
	data = fd.read(1024*8)
	sha1.update(data)
	fd.close()
	sha1Hex = sha1.hexdigest()
	return(sha1Hex)

def createHashDict(folderPath):
	hashDict = {}
	for f in findFiles('*', folderPath):
		if (duplicateFolder in f) or ('.git' in f):
			continue
		sha1hex = hashfile(os.path.join(folderPath, f))
		hashDict.setdefault(sha1hex, []).append(f)
	return(hashDict)

def getFileList(folderPath):
	sha1hexList = []
	filesList = findFiles('*', folderPath)
	for f in filesList:
		pv(f)
		sha1hex = hashfile(os.path.join(folderPath, f))
		sha1hexList.append(sha1hex)
	return(sha1hexList, filesList)

def main():
	if (len(sys.argv) < 2):
		pe('Usage: %s <folderPath>', sys.argv[0])
		pe('Usage: %s <properFolderPath> <improperFolderPath>', sys.argv[0])
		return(1)
	if (len(sys.argv) == 2):
		folderPath = sys.argv[1]
		hashDict = createHashDict(folderPath)
		for duplicateFileList in hashDict.values():
			if (len(duplicateFileList) > 1):
				pi('\nDuplicate file list: ')
				i = 1
				for filePath in duplicateFileList:
					writeLog('%d: %s\n' %(i, filePath))
					i += 1
				cmd = getchar('enter file id to save').strip()
				if (cmd == ''):
					continue
				duplicateFileList.pop(int(cmd) - 1)
				for filePath in duplicateFileList:
					srcPath = os.path.join(folderPath, filePath)
					destPath = os.path.join(duplicateFolder, filePath)
					moveFile(srcPath, destPath)
		pi('Moved duplicate files to: %s', duplicateFolder)
	elif (len(sys.argv) == 3):
		properFolderPath = sys.argv[1]
		improperFolderPath = sys.argv[2]
		(if_sha1hexList, if_fileList) = getFileList(improperFolderPath)
		(pf_sha1hexList, pf_fileList) = getFileList(properFolderPath)
		# compare files as per the sha1sum
		i = 0
		pi('\nDuplicate file list: ')
		while (i < len(if_sha1hexList)):
			if (if_sha1hexList[i] in pf_sha1hexList):
				writeLog('%s\n' %(if_fileList[i]))
				srcPath = os.path.join(improperFolderPath, if_fileList[i])
				destPath = os.path.join(duplicateFolder, if_fileList[i])
				moveFile(srcPath, destPath)
			i += 1
		pi('Moved duplicate files to: %s', duplicateFolder)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
