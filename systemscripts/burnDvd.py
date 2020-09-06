#!/usr/bin/python3
import signal

import os
import sys
import time

DISK_SIZE = 4700000000
burnList = {}
tmpFile = '/tmp/burnList.tmp'

def usage():
	pe('Usage: %s <volume_name> <previous_size>', sys.argv[0])
	pe('Usage: %s <add> <files...>', sys.argv[0])

def addExternally():
	# read the main process pid from the tmp file
	tmpFd = open(tmpFile, 'r')
	t = tmpFd.read()
	tmpFd.close()
	mainPid = int(t)
	# write the requested files to the tmp file
	tmpFd = open(tmpFile, 'w')
	for filePath in sys.argv[2:]:
		filePath = os.path.realpath(filePath)
		tmpFd.write(filePath + '\n')
	tmpFd.close()
	# send an USR1 signal to the main process
	os.kill(mainPid, signal.SIGUSR1)

def addElements(filePathList):
	global burnList
	for filePath in filePathList:
		if (not os.path.exists(filePath)):
			pe('no File exists: %s', filePath)
			return
		(ret, out) = runCmdGetOutput('du -sb %s' %(filePath))
		fileSize = int(out.split()[0])
		burnList[filePath] = fileSize
		pi('Added: %s', filePath)

def readable(number):
	numberStr = str(number)
	string = []
	for i, c in enumerate(reversed(numberStr)):
		if (i != 0) and (not(i % 3)):
			string.insert(0, ',')
		string.insert(0, c)
	return ''.join(string)

def printBurnList(diskSizeLimit):
	totalSize = 0
	count = 0
	# calulate output string lengths as per the colume length of the
	#+ terminal screen
	(rows, columns) = getSttySize()
	countStingWidth = 3
	fileSizeStringWidth = 13
	filePathStringWidth = columns - (countStingWidth + 2) - (4 + fileSizeStringWidth + 1)
	writeLog('%s\n' %('-' * columns), 'NORMAL')
	stringFormat = '%' + '-%d' %(countStingWidth) + 's  %' + \
					'-%d' %(filePathStringWidth) + 's   %' + \
					'-%d' %(fileSizeStringWidth) + 's \n'
	writeLog(stringFormat %('Sno', 'FilePaths', 'Sizes'), 'NORMAL')
	stringFormat = '%' + '%d' %(countStingWidth) + 'd. %' + \
					'-%d' %(filePathStringWidth) + 's  : %' + \
					'%d' %(fileSizeStringWidth) + 's \n'
	filePathList = list(burnList.keys())
	filePathList.sort()
	for filepath in filePathList:
		count += 1
		fileSize = burnList[filepath]
		totalSize += fileSize
		# if the length of the filepath increases the line limit,
		#+ ignore the fullpath of the file
		if (len(filepath) > filePathStringWidth):
			t = filepath.split('/')
			filepath = '/%s/.../%s' %(t[1], t[-1]) 
		fileSize = readable(fileSize)
		writeLog(stringFormat %(count, filepath, fileSize)), 'NORMAL' 
	writeLog('%s\n' %('-' * columns), 'NORMAL')
	stringFormat = '%' + '%d' %((countStingWidth + 2) + filePathStringWidth) + 's  : %' + \
					'%d' %(fileSizeStringWidth) + 's \n'
	writeLog(stringFormat %('Total Size', readable(totalSize)), 'NORMAL')
	# decide the color of the result string as per the disk usage
	resultBytes = diskSizeLimit - totalSize
	if (resultBytes < 0):
		writeLog('[%s]: Data bytes exceeds the disk space\n' %(readable(resultBytes)), 'RED')
	elif (resultBytes < 50000000): # for optimised burning, we can leave 50MB of disk space
		writeLog('[%s]: Data Bytes Correctly fits into the disk\n' %(readable(resultBytes)), 'GREEN')
	else:
		writeLog('[%s]: Bytes will be left on the disk\n' %(readable(resultBytes)), 'YELLOW')
	writeLog('%s\n' %('-' * columns), 'NORMAL')

def deleteElements(indexList):
	global burnList
	filePathList = list(burnList.keys())
	filePathList.sort()
	deleteFileList = []
	for i in indexList:
		i = int(i) - 1
		if (i < len(filePathList)):
			fileName = filePathList[i]
			del(burnList[fileName])
			pi('Deleted: %s', fileName)
		else:
			pe('Wrong Index: %d', i+1)

def createBurnCmd(volumeName, multisession):
	global burnList
	growisofsCmd = 'growisofs'
	growisofsCmd += ' -dry-run'
	growisofsCmd += ' -speed=8'
	if (multisession == True):
		growisofsCmd += ' -M /dev/dvd'
	else:
		growisofsCmd += ' -Z /dev/dvd'
	#growisofsCmd = 'mkisofs'
	#growisofsCmd += ' -o m.iso'
	growisofsCmd += ' -V '%s'' %(volumeName)
	growisofsCmd += ' -iso-level 4'
	growisofsCmd += ' -joliet-long'
	growisofsCmd += ' -r -R -J -l -L'
	growisofsCmd += ' -graft-points'
	for filepath in burnList:
		fileBasename = os.path.basename(filepath)
		growisofsCmd += ' '/%s=%s'' %(fileBasename, filepath)
	pv(growisofsCmd)

def writePid():
	tmpFd = open(tmpFile, 'w')
	pid = os.getpid()
	tmpFd.write('%d' %(pid))
	tmpFd.close()
	
def main():
	try:
		option = sys.argv[1]
	except:
		usage()
		sys.exit(1)
	# runnning another program for external addition of files to the burnList
	if (option == 'add'):
		addExternally()
		sys.exit(0)
	else:
		volumeName = sys.argv[1]
	# give the size of the disk already written
	try:
		diskSizeLimit = int(sys.argv[2])
		multisession = True
	except:
		diskSizeLimit = DISK_SIZE
		multisession = False
	# write a tmp file to listen the external files addition to the burnList
	if (os.path.exists(tmpFile)):
		pe('tmp file is already exists')
		sys.exit(0)
	writePid()
	# registering signal handler for the external addition of files to the burnList
	def signal_hdl(signum, frame):
		return
	signal.signal(signal.SIGUSR1, signal_hdl)
	# following user to finalise the burnList
	while (1):
		# readline() raises IOError when signal occurs in middle, so
		# catch IOError and write the files into the burnList
		try:
			request = readStdin(' [a|d|p|c|q]')
		except IOError:
			print()
			tmpFd = open(tmpFile, 'r')
			filePathList = tmpFd.read().splitlines()
			addElements(filePathList)
			writePid()
			request = ''
		request = request.strip()
		if (request == ''):
			continue
		t = request.split()
		if (t[0] == 'a'):
			addElements(t[1:])
		elif (t[0] == 'p'):
			printBurnList(diskSizeLimit)
		elif (t[0] == 'd'):
			deleteElements(t[1:])
		elif (t[0] == 'c'):
			createBurnCmd(volumeName, multisession)
		elif (t[0] == 'q'):
			createBurnCmd(volumeName, multisession)
			os.unlink(tmpFile)
			pi('Quiting...')
			break
		else:
			pe('Unknown request')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)

# usage:
# first run burnDvd.py in one terminal
# $ burnDvd.py
# from any terminal you can add files to the burn list using
# $ burnDvd.py add <files...>
# this will files to the burnlist
# use 'p' command to print the content and 'q' to quit
