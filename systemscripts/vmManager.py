#!/usr/bin/python3
import optparse
import time

import os
import sys
import time

vmDict = {
	'dvat': ('dvat', '192.168.56.101', 22),
}

def usage():
	pe('Usage: %s [-l|-s|-k] <vmTag>', sys.argv[0])

def parse_args():
	usage = 'Usage: %s [options]' %(sys.argv[0])
	parser = optparse.OptionParser(usage=usage, version='startVirtualBox-1.0v')
	parser.add_option('-l', '--list', action='store_true', \
			dest='listVms', default=False, help='list the running vms')
	parser.add_option('-s', '--start', action='store', \
			dest='startVmName', default=None, type='string', help='starts the selected vm')
	parser.add_option('-k', '--kill', action='store', \
			dest='killVmName', default=None, type='string', help='kills the selected vm')
	options, args = parser.parse_args()
	return(options, args)

def chkReachable(ip, portNo):
	import socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(0.25)
	try:
		sock.connect((ip, portNo))
	except:
		try:
			sock.connect((ip, portNo))
		except:
			return(False)
	return(True)

def main():
	(options, args) = parse_args()
	listVms = options.listVms
	startVmName = options.startVmName
	killVmName = options.killVmName
	# running vms list
	if (listVms == True):
		vmListCmd = 'vboxmanage list runningvms'
		(ret, out) = runCmdGetOutput(vmListCmd)
		runningVmsList = out.decode().splitlines()
		for vmTag in vmDict.keys():
			(vmName, ipAddr, portNo) = vmDict[vmTag]
			outString = '[%s]: %s  -  %s\n' %(vmTag, vmName, ipAddr)
			vmRunning = False
			for runningVm in runningVmsList:
				if (runningVm.find(vmName) != -1):
					vmRunning = True
					break
			if (vmRunning == True):
				writeLog(outString, color='GREEN', textType=BOLD)
			else:
				writeLog(outString, color='BLUE')
		return(0)
	# starting vm
	elif (startVmName != None):
		(vmName, ipAddr, portNo) = vmDict[startVmName]
		vmStartCmd = 'vboxmanage startvm %s --type headless' %(vmName)
		runCmd(vmStartCmd)
		# wait till vm starts pinging
		pi('Waiting for VM to boot completely')
		while (chkReachable(ipAddr, portNo) != True):
			pd('Waiting for VM reachability')
			time.sleep(2)
		pi('VM is Successfully Up and Running')
		return(0)
	# killing vm
	elif (killVmName != None):
		(vmName, ipAddr, portNo) = vmDict[killVmName]
		vmPoweroffCmd = 'vboxmanage controlvm %s acpipowerbutton' %(vmName)
		runCmd(vmPoweroffCmd)
		# wait till VM stop pinging
		pi('Waiting for VM to poweroff completely')
		while (chkReachable(ipAddr, portNo) != False):
			pd('Waiting for VM to stop sshd')
			time.sleep(2)
		pi('VM is Successfully Powerdown')
		return(0)
	else:
		usage()
		sys.exit(1)
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
