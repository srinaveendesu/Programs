#!/usr/bin/python3
import os
import sys
import time
import xmlrpc.client
import xml.dom.minidom

import os
import sys
import time

def usage():
	pe('Usage: %s <boot|poweroff>', sys.argv[0])

def getProxy(address):
	proxy = xmlrpc.client.ServerProxy(address)
	if (isinstance(proxy, xmlrpc.client.ServerProxy) != True):
		pd('Failed to get xml rpc proxy')
		return(False)
	pd('Successfully openned rpc proxy session')
	return(proxy)

def poweroffVm(proxy, auth, vmId):
	(ret, response, errorNo) = proxy.one.vm.action(auth, 'shutdown', vmId)
	if (ret == False):
		pe('Failed to shutdown the vm: %d', vmId)
		pe('errorStr: %s', response)
		pe('errorNo: %s', errorNo)
		return(False)
	pd('response: %s', response)
	return(True)
	
def bootVm(proxy, auth, vmId):
	(ret, response, errorNo) = proxy.one.vm.action(auth, 'resume', vmId)
	if (ret == False):
		pe('Failed to boot the vm: %d', vmId)
		pe('errorStr: %s', response)
		pe('errorNo: %s', errorNo)
		return(False)
	pd('response: %s', response)
	return(True)

def getVmInfo(proxy, auth, vmId):
	# requesting for vm info
	(ret, response, errorNo) = proxy.one.vm.info(auth, vmId)
	if (ret == False):
		pe('errorResponse: %s', response)
		pe('errorNo: %s', errorNo)
		return(1)
	# parsing response
	parser = xml.dom.minidom.parseString(response)
	lcmStateElement = parser.getElementsByTagName('LCM_STATE')[0]
	vmState = int(lcmStateElement.firstChild.data)
	ipElement = parser.getElementsByTagName('IP')[0]
	vmIp = ipElement.firstChild.data
	return(vmState, vmIp)

def main():
	if (len(sys.argv) < 2):
		usage()
		return(1)
	address = 'http://100.65.136.4:2633/RPC2'
	auth = 'mkasula:Madhutk'
	vmId = 1009
	userCmd = sys.argv[1]
	# open xml rpc proxy session to open nebulla
	pi('Opening proxy session')
	proxy = getProxy(address)
	# get the vm info
	(vmState, vmIp) = getVmInfo(proxy, auth, vmId)
	if (userCmd == 'boot'):
		if (vmState == 3):
			pi('VM Already running with IP: %s', vmIp)
			return(0)
		# boot vm
		pi('Booting vm: %s', vmId)
		ret = bootVm(proxy, auth, vmId)
		if (ret == False):
			return(1)
		pi('Successfully Booted the vm: %d', vmId)
		# get the vm info
		(vmState, vmIp) = getVmInfo(proxy, auth, vmId)
		if (vmState != 3):
			pe('Failed to booting the vm')
			return(1)
		pi('VM booted with IP: %s', vmIp)
	elif (userCmd == 'poweroff'):
		if (vmState == 0):
			pi('VM Already powerred off')
			return(0)
		pi('Poweroff vm: %s', vmId)
		ret = poweroffVm(proxy, auth, vmId)
		if (ret == False):
			return(1)
		pi('Successfully powerred off the vm: %d', vmId)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
