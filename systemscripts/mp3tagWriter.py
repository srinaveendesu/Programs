#!/usr/bin/python3
import re
import taglib

import os
import sys
import time

def writeMp3Tag(musicFilePath, title, artist, album, year, comment):
	# ignoring imageFile, as taglib will not support APIC tag as mutagen in python2.7
	# writing the other tag 
	f = taglib.File(musicFilePath)
	f.tags['TITLE'] = title
	f.tags['ARTIST'] = artist
	f.tags['ALBUM'] = album
	f.tags['DATE'] = year
	f.tags['COMMENT'] = comment
	f.tags['GENRE'] = 'Classical'
	f.save()
	return(True)
	
def main():
	if (len(sys.argv) < 2):
		pe('Usage: %s <musicDirs...>', sys.argv[0])
		sys.exit(1)
	artist = 'Madhusudhan'
	year = str(time.localtime()[0])
	comment = 'Madhusudhan Audio Songs'
	for musicDir in sys.argv[1:]:
		if (musicDir != '.'):
			musicDir = re.sub('/$', '', musicDir) # remove / at end
			album = os.path.basename(musicDir)
		else:
			album = os.path.basename(os.getcwd())
		for fileName in os.listdir(musicDir):
			if (not fileName.endswith('.mp3')):
				continue
			title = os.path.splitext(fileName)[0]
			musicFilePath = os.path.join(musicDir, fileName)
			pi('Writing mp3 Tag: %s', musicFilePath)
			writeMp3Tag(musicFilePath, title, artist, album, year, comment)
	pi('Succussfully Completed')
	return(0)

if (__name__ == '__main__'):
	main()

