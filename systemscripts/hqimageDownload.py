#!/usr/bin/python
import urllib

import os
import sys
import time

HQ_IMAGE_WEB_LINK = 'http://www.hqimage.com'

def usage():
	pe('Usage: %s <category> <startImgCount> <lastImgCount>', sys.argv[0])
	pe('Known Categories:')
	pe('      * Space_And_Planets')
	pe('      * 3D')
	pe('      * lakes-and-rivers')
	pe('      * Rainbow')
	pe('      * Ubuntu_&_Linux')
	pe('      * Waterfall')
	pe('Example: %s Space_And_Planets 1 117', sys.argv[0])

def main():
	if (len(sys.argv) < 4):
		usage()
		sys.exit(1)
	category = sys.argv[1]
	startImgCount = int(sys.argv[2])
	lastImgCount = int(sys.argv[3])
	for i in range(startImgCount, lastImgCount + 1):
		imageName = '%s_%d.jpg' %(category, i)
		imageLink = '%s/%s/DtWallpaper/Img/%s' %(HQ_IMAGE_WEB_LINK, category, imageName)
		pv(imageLink)
		pi('Trying for %s: ...', imageName)
		socket = urllib.urlopen(imageLink)
		out = socket.read()
		fd = open(imageName, 'w')
		fd.write(out)
		fd.close()
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
