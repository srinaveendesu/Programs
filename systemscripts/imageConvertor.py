#!/usr/bin/python
import commands
import shutil

import os
import sys
import time

# mobile details
# standard desktop details
#MOBILE_SCREEN_WIDTH = 1024
#MOBILE_SCREEN_HEIGHT = 768
# siri mobile details
#MOBILE_SCREEN_WIDTH = 220
#MOBILE_SCREEN_HEIGHT = 176
# my mobile details
MOBILE_SCREEN_WIDTH = 320
MOBILE_SCREEN_HEIGHT = 240


def usage():
	print 'Usage: %s <imageFolders...>' %(sys.argv[0])

def convert(srcImage, destImage):
	(ret, out) = runCmdGetOutput('identify '%s'' %(srcImage))
	size = out.split()[2].split('x')
	width = size[0]
	height = size[1]
	if (width >= height):
		resolution = '%sx%s' %(MOBILE_SCREEN_WIDTH, MOBILE_SCREEN_HEIGHT)
	else:
		resolution = '%sx%s' %(MOBILE_SCREEN_HEIGHT, MOBILE_SCREEN_WIDTH)
	convertCmd = 'convert '%s' -thumbnail %s '%s'' \
				%(srcImage, resolution, destImage)
	runCmd(convertCmd)

def convertImages(srcDir, destDir):
	# getting image file list
	fileList = findFiles('*.jpg', srcDir)
	# converting images
	totalFileCount = len(fileList)
	for i, srcFile in enumerate(fileList):
		print >> sys.stderr, ' [%d/%d]: %-80s' %(i+1, totalFileCount, srcFile)+ '\r',
		destFile = os.path.join(destDir, srcFile)
		srcFile = os.path.join(srcDir, srcFile)
		convert(srcFile, destFile)
	print '%-114s' %(' Image Conversion completed') # to erase the status line completely

def main():
	pictureFiles= []
	for srcDir in sys.argv[1:]:
		if (srcDir[-1] == '/'):
			destDir= srcDir.split('/')[-2]+'_convertedImages/'
		else:
			destDir= srcDir.split('/')[-1]+'_convertedImages/'
		# creating output directory
		try:
			os.mkdir(destDir)
		except Exception:
			print >> sys.stderr, 'Error: %s already exited' %(destDir)
			choice= raw_input('Do you want to delete it? [y/n]: ')
			if (choice == 'y'):
				shutil.rmtree(destDir)
				os.mkdir(destDir)
			else:
				print ' Exiting with no conversions'
				sys.exit(0)
		# converting images
		convertImages(srcDir, destDir)
	return(0)
	
if (__name__ == '__main__'):
	if (len(sys.argv) < 2):
		usage()
	else:
		ret = main()
		sys.exit(ret)
