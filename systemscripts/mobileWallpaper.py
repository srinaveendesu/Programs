#!/usr/bin/python

import os
import sys
import time

MOBILE_SCREEN_WIDTH = 320
MOBILE_SCREEN_HEIGHT = 240

def usage():
	pe('Usage: %s left.jpg center.jpg right.jpg output.jpg')
	pw('Always try to give only portrait angled images')

def getImageInfo(image):
	(ret, out) = runCmdGetOutput('identify '%s'' %(image))
	size = out.split()[2].split('x')
	width = size[0]
	height = size[1]
	return (width, height)

def convertImage(image):
	resizedImage = image.replace('.jpg', '_resized.jpg')
	resizeCmd = 'convert '%s' -thumbnail %s '%s'' \
				%(image, MOBILE_SCREEN_HEIGHT, resizedImage)
	runCmd(resizeCmd)

	(width, height) = getImageInfo(resizedImage)
	if (height > MOBILE_SCREEN_WIDTH):
		cropedImage = image.replace('.jpg', '_croped.jpg')
		cropCmd = 'convert -crop %sx%s+0+0 '%s' '%s'' \
				%(MOBILE_SCREEN_HEIGHT, MOBILE_SCREEN_WIDTH, resizedImage, cropedImage)
		runCmd(cropCmd)
		remove(resizedImage)
		return cropedImage
	else:
		return resizedImage

def appendImages(leftImage, centreImage, rightImage, outputImage):
	appendCmd = 'convert '%s' '%s' '%s' +append '%s'' \
			%(leftImage, centreImage, rightImage, outputImage)
	ret = runCmd(appendCmd)
	remove(leftImage)
	remove(centreImage)
	remove(rightImage)
	return ret

def main():
	if(len(sys.argv) < 5):
		usage()
		sys.exit(0)
	leftImage = sys.argv[1]
	centreImage = sys.argv[2]
	rightImage = sys.argv[3]
	outputImage = sys.argv[4]
	
	leftImage = convertImage(leftImage)
	centreImage = convertImage(centreImage)
	rightImage = convertImage(rightImage)
	ret = appendImages(leftImage, centreImage, rightImage, outputImage)

	if (ret != False):
		pi('Successfully Created mobile wallpaper: %s', outputImage)
		return(0)
	else:
		return(1)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
