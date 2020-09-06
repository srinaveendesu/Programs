#!/usr/bin/python3
import random
import optparse
import signal
import taglib

import os
import sys
import time
import pycmds

MUSIC_DIR = os.path.join('/', 'media', USER, 'BackUpDrive', 'music')
INITIAL_VOLUME = 40
MAX_VOLUME = 95
TRASACTION_TIME = 8
TIME_OUT = 60 # this should be more than twice of TRASACTION_TIME

PAUSE_STATUS = False
LOOP_PLAY = False

VOL_DOWN = bytes([57])
VOL_UP = bytes([48])
PAUSE = bytes([112])
RIGHT_ARROW = bytes([27, 91, 65])
QUIT = bytes([113])
def mplayerKeySend(mplayerStdin, key):
	try:
		os.write(mplayerStdin, key)
	except:
		return(False)
	return(True)

def startMplayer(selectedFile, playtime):
	pv(selectedFile)
	mp3ValidLength = playtime - TIME_OUT
	pv(mp3ValidLength)
	if (mp3ValidLength <= 0):
		return(False)
	startPosition = random.randint(0, mp3ValidLength)
	mplayerCmd = pycmds.dts() + ('-msglevel', 'all=-1', '-volume', str(INITIAL_VOLUME), '-ss', str(startPosition), '-endpos', str(TIME_OUT), selectedFile)
	pi('Playing: %s', selectedFile)
	(mplayerPid, mplayerStdin, mplayerStdout) = runBg(mplayerCmd)
	pd('mplayer.pid: %d', mplayerPid)
	return(mplayerStdin)

def startMusicRock(fileTupleList):
	random.seed()
	mplayerStdin1 = None
	mplayerStdin2 = None
	# signal handler for child process
	def playerPause_SignalHandler(signum, frame):
		global PAUSE_STATUS
		PAUSE_STATUS = not(PAUSE_STATUS)
		pd('got signal')
		# send an pause/play signal to mplayers
		mplayerKeySend(mplayerStdin1, PAUSE)
		mplayerKeySend(mplayerStdin2, PAUSE)
		# wait till another signal come
		if (PAUSE_STATUS == True):
			pi('Paussed... ')
			signal.pause()
		else:
			pi('Continue... ')
	# off the system suspend
#	systemSuspend(suspend=False)
	# signal handling for player pause
	signal.signal(signal.SIGUSR1, playerPause_SignalHandler)
	# start mplayer
	lenFileTupleList = len(fileTupleList)
	random.shuffle(fileTupleList, random=random.random)
	count = 0
	while (count < lenFileTupleList):
		(selectedFile, playtime) = fileTupleList[count]
		mplayerStdin2 = startMplayer(selectedFile, playtime)
		# simply ignore the mp3 files which are less length than TIME_OUT
		while (mplayerStdin2 == False):
			count += 1
			(selectedFile, playtime) = fileTupleList[count]
			mplayerStdin2 = startMplayer(selectedFile, playtime)
		# start transition
		i = 0
		volumeSignalCount = ((MAX_VOLUME - INITIAL_VOLUME) / 2)
		while (i < volumeSignalCount):
			pd('VOL_DOWN -> mplayer1')
			mplayerKeySend(mplayerStdin1, VOL_DOWN)
			pd('VOL_UP -> mplayer2')
			mplayerKeySend(mplayerStdin2, VOL_UP)
			time.sleep(TRASACTION_TIME / float(volumeSignalCount))
			i += 1
		# sleep while playing
		idleCount = TIME_OUT - (TRASACTION_TIME * 2)
		while (idleCount > 0):
			pv(idleCount)
			time.sleep(1)
			idleCount -= 1
		# wait for previous mplayer to join
		if (mplayerStdin1 != None):
			pd('QUIT -> mplayer1')
			mplayerKeySend(mplayerStdin1, QUIT)
			os.wait()
		mplayerStdin1 = mplayerStdin2
		count += 1
		# for loop playing
		if (LOOP_PLAY == True) and (count >= lenFileTupleList):
			pd('re-shuffling the fileTupleList')
			random.shuffle(fileTupleList, random=random.random)
			count = 0
	# on the system suspend
#	systemSuspend(suspend=True)
	pi('Successfully Completed')
	return(0)

def playMusicDb():
	# sync the music play list
	musicDataFile = os.path.join(MUSIC_DIR, 'musicDataFile.tmp')
	data = readDataFile(musicDataFile)
	musicDict = data.musicDict
	fileTupleList = []
	for (musicFile, (playtime, rating)) in musicDict.items():
		fileName = os.path.join(MUSIC_DIR, musicFile)
		fileTupleList.append((fileName, playtime))
	ret = startMusicRock(fileTupleList)
	return(ret)

def playMusicDirs(musicDirs):
	# gathering music file lists
	fileTupleList = []
	for musicDir in musicDirs:
		fileList = findFiles('*.mp3', musicDir)
		for fileName in fileList:
			fileName = os.path.join(musicDir, fileName)
			playtime = taglib.File(fileName).length
			fileTupleList.append((fileName, playtime))
	ret = startMusicRock(fileTupleList)
	return(ret)

def playlistFile(playlist):
	fullpath = os.path.dirname(os.path.realpath(playlist))
	fd = open(playlist, 'r')
	# gathering music file lists
	fileTupleList = []
	for fileName in fd:
		fileName = fileName.strip()
		fileName = os.path.join(fullpath, fileName)
		playtime = taglib.File(fileName).length
		fileTupleList.append((fileName, playtime))
	ret = startMusicRock(fileTupleList)
	return(ret)

def pauseMplayer():
	musicRockPid = getMainProcessPid()
	# sending SIGUSR1 signal to the musicrock process to get paused
	if (musicRockPid != False):
		os.kill(musicRockPid, signal.SIGUSR1)
	return(0)

def parse_args():
	usage = 'Usage: %s [--pause|--loop] [musicDirs...]' %(sys.argv[0])
	parser = optparse.OptionParser(usage=usage, version='musicRock_1.0v')
	parser.add_option('-p', '--pause', action='store_true',
			dest='pause', default=False,
			help='pause player')
	parser.add_option('-l', '--loop', action='store_true',
			dest='loop', default=False,
			help='loop playing')
	parser.add_option('-f', '--playlist-file', action='store',
			dest='playlist', default=None,
			help='playlist file')
	parser.add_option('-v', '--max-volume', action='store',
			dest='maxVolume', default=MAX_VOLUME, type='int',
			help='max volume')
	options, args = parser.parse_args()
	return options, args

if (__name__ == '__main__'):
	options, args = parse_args()
	pv(options)
	pv(args)
	if (options.pause == True):
		ret = pauseMplayer()
		sys.exit(ret)
	if (options.playlist != None):
		playlistFile(options.playlist)
	if (options.loop == True):
		LOOP_PLAY = True
	if (options.maxVolume != MAX_VOLUME):
		MAX_VOLUME = options.maxVolume
	# start playing
	if (len(args) == 0):
		ret = playMusicDb()
	else:
		musicDirs = args
		for musicDir in musicDirs:
			if (not os.path.isdir(musicDir)):
				pe('%s: file not exits', musicDir)
				musicDirs.remove(musicDir)
		ret = playMusicDirs(musicDirs)
	sys.exit(ret)
