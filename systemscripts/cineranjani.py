#!/usr/bin/python3
import random

import os
import sys
import time

PLAY_TIME = 240
VIDEO_DIR = os.path.join(HOME, 'videos')
HDD_VIDEO_DIR = os.path.join('/', 'media', USER, 'BackUpDrive', 'videos')
SUB_VIDEO_DIRS = ['teluguMovies', 'hindiMovies']
DATA_FILE = os.path.join(ALPT, 'cineranjaniData.tmp')

def main():
	# collect videos from video dirs
	videoDirList = []
	for subDir in SUB_VIDEO_DIRS:
		if (os.path.exists(HDD_VIDEO_DIR)):
			videoDirList.append(os.path.join(HDD_VIDEO_DIR, subDir))
		else:
			videoDirList.append(os.path.join(VIDEO_DIR, subDir))
	pv(videoDirList)
	videoList = []
	for videoDir in videoDirList:
		for f in os.listdir(videoDir):
			if (os.path.splitext(f)[1] in ['.mp4', '.webm', '.mkv', '.flv', '.avi']):
				videoList.append(os.path.join(videoDir, f))
	# read cache file
	DATA = readDataFile(DATA_FILE)
	if (DATA == False):
		pi('creating new data file')
		DATA = getNewDataModule()
		DATA.videoDetails = {}
	# start playing
	while (True):
		random.seed(time.time())
		random.shuffle(videoList)
		for videoFile in videoList:
			videoBaseName = os.path.basename(videoFile)
			pi('Playing Video: %s', videoBaseName)
			if (videoBaseName in DATA.videoDetails):
				duration = DATA.videoDetails[videoBaseName]
			else:
				duration = int(getVideoDetails(videoFile)['ID_LENGTH'])
				DATA.videoDetails[videoBaseName] = duration
				writeDataFile(DATA_FILE, DATA)
			startPos = random.randint(0, (duration - PLAY_TIME - 120)) + 120 # 120 seconds are to skip titles
			mplayerCmd = ('mplayer', '-af', 'volnorm=2:0.90', '-ss', str(startPos), '-endpos', str(PLAY_TIME), '-fs', '-nosub', videoFile)
			runCmd(mplayerCmd, verbose=True)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)

