#!/usr/bin/python3

import os
import sys
import time

def main():
	machineType = getMachine()
	assigningIpsCmd = 'pudo ifconfig eth0 up -pointopoint 192.168.1.%d dstaddr 192.168.1.%d'
	if (machineType == HL):
		assigningIpsCmd = assigningIpsCmd %(1, 2)
	elif (machineType == OFFICE_LAPTOP):
		assigningIpsCmd = assigningIpsCmd %(2, 1)
	else:
		pe('Unkown Machine')
		return(1)
	# down the eth0
	cmd = 'pudo ifconfig eth0 down'
	runCmd(cmd)
	# assigning ips
	runCmd(assigningIpsCmd)
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
