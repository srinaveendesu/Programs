#!/usr/bin/python3

import os
import sys
import time

###DEBUG#####
#def runSudoCmd(cmd):
#	pd('requested to run cmd: sudo %s', cmd)
#	pd('with passwd: %s', passwd)
#	return (0,0)
#############

def executeCmd(cmd):
	pi('Excuting Cmd: %s', cmd)
	os.system(cmd)
	return True
	
def waitPid(pid):
	pi('Waiting for pid[%d] to exit', pid)
	while (1):
		if (checkPid(pid) == True):
			pi('pid[%d]: still alive', pid)
			time.sleep(180)
		else:
			pi('PID[%d] Completed', pid)
			return True

def doHerbernate():
	connectedDrives = getDrivesConnected()
	# unmount the connected disks
	for connectedDisk in connectedDrives:
		mountPoint = getDiskMountPoint(connectedDisk)
		cmd = 'umount %s' %(mountPoint)
		(ret, out) = runSudoCmd(cmd)
		if (ret != 0):
			pe('Uable to mount the disk: %s', mountPoint)
			sys.exit(1)
	pi('Going to Hibernate')
	sndAlert(E, 5, MAX, FOREGROUND)
	handler = notifySend(W, 'Going to Hibernate', summary='afterProcess')
	for i in range(9, -1, -1):
		writeLog(': Press Ctrl+c to avoid System Hibernation: [%d]\r' %(i), 'YELLOW')
		time.sleep(1)
	handler.close()
	runSudoCmd('pm-hibernate')
	sys.exit(0)

def checkDisks():
	connectedDrives = getDrivesConnected()
	for connectedDisk in connectedDrives:
		mountPoint = getDiskMountPoint(connectedDisk)
		lsofCmd = 'lsof %s' %(mountPoint)
		(ret, out) = runCmdGetOutput(lsofCmd)
		if (ret == 0):
			pe('%s: is presently accessed by the following programs', mountPoint)
			out = out.splitlines()[1:]
			for line in out:
				programName = line.split()[0]
				pe('%s', programName)
			pe('Please exit from the above programs to safe hibernation')
			sys.exit(1)
	return connectedDrives

def main():
	# if hibernation is required
	if ('-h' in sys.argv):
		# check for the sudo permission
		ret = readSudoPasswd()
		if (ret != True):
			return(1)
		# check for disks mounted
		checkDisks()
	# check for enough agruments
	if (len(sys.argv) < 2):
		pe('sudo %s [ -c cmd | -p pid | -h ]', sys.argv[0])
		sys.exit(1)
	# arg parsing
	args = sys.argv[1:]
	i = 0
	while (i < len(args)):
		if (args[i] == '-c'):
			i += 1
			executeCmd(args[i])
		elif (args[i] == '-p'):
			i += 1
			waitPid(int(args[i]))
		elif (args[i] == '-h'):
			doHerbernate()
		else:
			pe('wrong arg')
		i += 1
	handler = notifySend(S, 'afterProcess: Succufully Completed')
	sndAlert(S, 1, MAX, FOREGROUND)
	handler.close()
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
