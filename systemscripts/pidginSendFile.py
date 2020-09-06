#!/usr/bin/python3
import dbus

import os
import sys
import time

pidginBusName = 'im.pidgin.purple.PurpleService'
pidginObjectName = '/im/pidgin/purple/PurpleObject'
pidginInterfaceName = 'im.pidgin.purple.PurpleInterface'

def sendFile(personName, filePathList):
	bus = dbus.SessionBus()
	proxyObject = bus.get_object(pidginBusName, pidginObjectName)
	pidginInterface = dbus.Interface(proxyObject, dbus_interface=pidginInterfaceName)
	activeActiveIdList = pidginInterface.PurpleAccountsGetAllActive()
	pv(activeActiveIdList)
	buddyFound = False
	buddyAliasList = []
	for activeActiveId in activeActiveIdList:
		buddyIdList = pidginInterface.PurpleFindBuddies(activeActiveId, '')
		for buddyId in buddyIdList:
			pv(buddyId)
			buddyAliasName = pidginInterface.PurpleBuddyGetAlias(buddyId)
			pv(buddyAliasName)
			isOnline = pidginInterface.PurpleBuddyIsOnline(buddyId)
			pv(isOnline)
			if (isOnline == True):
				buddyAliasList.append(buddyAliasName)
			if (buddyAliasName == personName):
				if (isOnline != True):
					pe('%s is offline', personName)
					return(False)
				buddyFound = True
				buddyEmailId = pidginInterface.PurpleBuddyGetName(buddyId)
				pv(buddyEmailId)
				connectionId = pidginInterface.PurpleAccountGetConnection(activeActiveId)
				pv(connectionId)
				if (type(filePathList) != list):
					filePathList = [filePathList]
				for filePath in filePathList:
					if (os.path.exists(filePath) == True):
						fileRealPath = os.path.realpath(filePath)
						pidginInterface.ServSendFile(connectionId, buddyEmailId, fileRealPath)
						pi('Successfully Send File: %s', filePath)
					else:
						pe('%s: file not found', filePath)
				break
		if (buddyFound == True):
			break
	if (buddyFound != True):
		pe('%s not found', personName)
		writeLog('Known person Names:\n')
		setTtyColor(color='GREEN', textType='BOLD')
		for buddyName in buddyAliasList:
			writeLog('\t%s\n' %(buddyName))
		setTtyColor('NORMAL')
	return(True)

def usage():
	print('Usage: %s <personName> <filepath>...' %(sys.argv[0]))
	return(True)

def main():
	if (len(sys.argv) < 3):
		usage()
		sendFile('', '')
		sys.exit(1)
	personName = sys.argv[1]
	filePathList = sys.argv[2:]
	sendFile(personName, filePathList)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
