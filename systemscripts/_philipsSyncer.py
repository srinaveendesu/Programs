#!/usr/bin/python3
import optparse
import signal
import random
import taglib

import os
import sys
import time

PRESERVE_PERCENTAGE = 80

def getMinChargingTime():
	MAX_CHARGING_TIME = 6*3600 # 6-hour charging
	now = time.localtime()
	currentTime = time.mktime(now)
	# as player should be detached before 5:30 pm, calculate min time for charging
	eveningTime = time.mktime((now[0], now[1], now[2], 17, 30, now[5], now[6], now[7], now[8]))
	minChargingTime = min(MAX_CHARGING_TIME, (eveningTime - currentTime))
	pv(minChargingTime)
	return(minChargingTime)

def removePreviousSongs(playerMusicDir):
	pi('Removing Previous Files')
	for f in os.listdir(playerMusicDir):
		remove(os.path.join(playerMusicDir, f))

def changeId3Tag(mp3filename, albumName):
	f = taglib.File(mp3filename)
	basename = os.path.basename(mp3filename)
	f.tags['TITLE'] = basename
	f.tags['ARTIST'] = f.tags['ALBUM']
	f.tags['ALBUM'] = albumName
	f.tags['COMMENT'] = 'MadhuSudhanPlayerSyncSystem'
	f.save()
	return(True)

def philipsSafeRemove():
	import ctypes
	import dbus
	pi('Syncing file system')
	libc = ctypes.CDLL('libc.so.6')
	libc.sync()
	pi('Safe Removing the Player')
	udiskBusName = 'org.freedesktop.UDisks'
	udiskInterfaceName = '/org/freedesktop/UDisks'
	bus = dbus.SystemBus()
	udiskProxy = bus.get_object(udiskBusName, udiskInterfaceName)
	deviceObjectPathList = udiskProxy.EnumerateDevices(dbus_interface='org.freedesktop.UDisks')
	deviceObjectPathList.sort()
	deviceObjectPathList.reverse()
	for deviceObjectPath in deviceObjectPathList:
		pv(deviceObjectPath)
		deviceProxy = bus.get_object(udiskBusName, deviceObjectPath)
		propertyInterface = dbus.Interface(deviceProxy, dbus.PROPERTIES_IFACE)
		isPartition = propertyInterface.Get('org.freedesktop.UDisks.Device', 'DeviceIsPartition')
		pv(isPartition)
		if (isPartition != True):
			continue
		vendorName = propertyInterface.Get('org.freedesktop.UDisks.Device', 'DriveVendor')
		pv(vendorName)
		if (vendorName != 'Philips'):
			continue
		isMounted = propertyInterface.Get('org.freedesktop.UDisks.Device', 'DeviceIsMounted')
		pv(isMounted)
		if (isMounted == True):
			deviceProxy.FilesystemUnmount([], dbus_interface='org.freedesktop.UDisks.Device', timeout=300)
		philipsDeviceObjectPath = propertyInterface.Get('org.freedesktop.UDisks.Device', 'PartitionSlave')
		philipsDeviceProxy = bus.get_object(udiskBusName, philipsDeviceObjectPath)
		propertyInterface = dbus.Interface(philipsDeviceProxy, dbus.PROPERTIES_IFACE)
		canDetach = propertyInterface.Get('org.freedesktop.UDisks.Device', 'DriveCanDetach')
		pv(canDetach)
		if (canDetach == True):
			philipsDeviceProxy.DriveDetach([], dbus_interface='org.freedesktop.UDisks.Device')
			pi('Successfully Completed Philips Player Detaching')
		break
	return(True)

def parse_args():
	usage = 'Usage: %s [options]' %(sys.argv[0])
	parser = optparse.OptionParser(usage=usage, version='philipsSyncer_2.0v')
	parser.add_option('-r', '--reminder', action='store_true', \
			dest='lauchReminder', default=False, \
			help='for lauching reminder for syncing philips player')
	parser.add_option('-d', '--detach', action='store_true', \
			dest='detach', default=False, \
			help='for detaching the philips player')
	options, args = parser.parse_args()
	return(options, args)

def main():
	(options, args) = parse_args()
	currentMachine = getMachine()
	# for lauching reminder
	if (options.lauchReminder == True):
		weekDay = time.localtime()[6]
		if (weekDay in [1,3]) and (currentMachine == OFFICE_LAPTOP):
			displayEvent('Charge the Media Player')
		elif (weekDay in [5,6]) and (currentMachine == LAPTOP_MACHINE):
			displayEvent('Sync the Media Player')
		return(0)
	# check for the philips player connection
	connectedDrives = getDrivesConnected()
	if (PHILIPS_PLAYER not in connectedDrives):
		pe('PHILIPS_PLAYER is not connected')
		return(1)
	# safe remove the philips player
	if (options.detach == True):
		philipsSafeRemove()
		return(0)
	# for charging on office laptop machine
	playerMountPoint = getDiskMountPoint(PHILIPS_PLAYER)
	if (currentMachine == OFFICE_LAPTOP):
		childLogFile = os.path.join('/', 'tmp', 'philipsSyncer')
		childPid = os.fork()
		if (childPid == 0):
			# child process starts here
			os.chdir('/') # change dir to root, for not to block current dir to umount
			# redirecting stdout and stderr to file
			fd = open(childLogFile, 'w')
			sys.stdout = sys.stderr = fd
			# ignoring sighup signal
			signal.signal(signal.SIGHUP, signal.SIG_IGN)
			# sleep for min charging time and detach on or before 5:30 PM
			minChargingTime = getMinChargingTime()
			time.sleep(minChargingTime)
			# safe remove the philips player
			philipsSafeRemove()
			displayEvent('Disconnect the Media Player')
			os._exit(0)
		else:
			# exit for parent process
			pi('Player Charging Started')
			pi('Lauched Child process [PID]: %d', childPid)
			pi('Child log file: %s', childLogFile)
			return(0)
	# required paths
	alpTmpDir = ALPT
	musicDir = os.path.join(HOME, 'music')
	## DEBUG #####################
	#alpTmpDir = 'alp/tmp'
	#playerMountPoint = 'philips'
	## DEBUG #####################
	musicPlayListFile = os.path.join(alpTmpDir, 'musicPlaylist.tmp')
	playerMusicDir = os.path.join(playerMountPoint, 'MUSIC', 'MadhuSudhan_AudioSongs')
	playerPlayListFile = os.path.join(playerMusicDir, 'playlist')
	# sync the music play list
	musicDict = getMusicDb()
	fileList = list(musicDict.keys())
	# remove previous songs
	removePreviousSongs(playerMusicDir)
	# read the music play list file
	statusData = readStatusFile(musicPlayListFile)
	if (statusData != False):
		(controlInfo, data) = readStatusFile(musicPlayListFile)
		prevPlayList = data[0]
	else:
		prevPlayList = []
	fileListLen = len(fileList)
	if (len(prevPlayList)+5 >= fileListLen):
		pe('No Enough Files for Successfull Syncing')
		return(1)
	# set the system suspend off
	systemSuspend(False)
	# recharging cycles
	# * monM + monE + tueM + chrg + tueE + wedM + wedE + thuM + chrg + thuE + friM + friE + WeekEnd
	#    1   +  1   +  1   +  ||  +  1   +  1   +  1   +  1   +  ||  +  1   +  1   +  1   +   ||   = 10 hours
	albumPlayTimes = [3600*3, 3600*4, 3600*3]
	# copy the random songs into the player as per the recharging cycles
	totalFileCount = len(fileList)
	albumCount = 1
	for limitPlayTime in albumPlayTimes:
		prevPlayList.append('--: album_%d :--' %(albumCount))
		random.seed(random.randint(0, totalFileCount))
		totalPlaytime = 0
		fileCount = 1
		albumName = '%02d_MadhuSudhan_AudioSongs' %(albumCount)
		pi('Syncing album: %s', albumName)
		while(totalPlaytime < limitPlayTime):
			if (totalFileCount == 0):
				pe('No File left to sync from: %s', musicDir)
				break
			index = random.randint(0, totalFileCount-1)
			selectedFile = fileList[index]
			if (musicDict[selectedFile][1] == DONT_SYNC) or (selectedFile in prevPlayList):
				del(fileList[index])
				totalFileCount -= 1
				continue
			pv(selectedFile)
			srcFile = os.path.join(musicDir, selectedFile)
			basename = os.path.basename(selectedFile)
			dstFile = os.path.join(playerMusicDir, '%02d_%s' %(fileCount, basename))
			copyFile(srcFile, dstFile)
			pr(' Copied: %d', fileCount)
			changeId3Tag(dstFile, albumName)
			# if play time is more than 15 min will be truncated to 15 min itself
			playTime = musicDict[selectedFile][0]
			if (playTime > 600):
				totalPlaytime += 600
			else:
				totalPlaytime += playTime
			prevPlayList.append(selectedFile)
			del(fileList[index])
			totalFileCount -= 1
			fileCount += 1
		pv(limitPlayTime)
		pv(totalPlaytime)
		albumCount += 1
	# only keep last MAX_PRESERVE_COUNT in the prev play list
	MAX_PRESERVE_COUNT = int(fileListLen * (PRESERVE_PERCENTAGE / 100.0))
	prevPlayList = prevPlayList[-(MAX_PRESERVE_COUNT+1):-1]
	writeStatusFile(musicPlayListFile, [prevPlayList])
	copyFile(musicPlayListFile, playerPlayListFile)
	pi('Player Sync: Successfully Completed')
	# safe remove the philips player
	philipsSafeRemove()
	# set the system suspend off
	systemSuspend(True)
	# display an event to disconnect the media player
	displayEvent('Disconnect the Media Player')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
