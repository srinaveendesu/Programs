#!/usr/bin/python

import os
import sys
import time

def usage():
	pi('%s: <videoFile> <FirstPartLength>', sys.argv[0])

def main():
	if (len(sys.argv) < 2):
		usage()
		sys.exit(1)
	inputFile = sys.argv[1]
	videoFileSize = os.stat(inputFile)[6]
	pv(videoFileSize)
	(inputVideoDuration, inputVideoBitrate, inputVideoWidth, \
		inputVideoHeight, inputVideoFPS, inputAudioSamplingFreq, \
		inputAudioBitrate) = getInputVideoProperties(inputFile)
	try:
		videoCutPoint = int(sys.argv[2])
	except:
		videoCutPoint = inputVideoDuration / 2
	estimatedFileSizePerSec = (videoFileSize / inputVideoDuration)
	t = os.path.splitext(inputFile)
	outDir = t[0]
	if (not os.path.exists(outDir)):
		os.mkdir(outDir)
	count = 1
	for option in ['-endpos', '-ss']:
		inputFileSliceName = os.path.join(outDir, t[0] + '_%d' %(count) + t[1])
		#mencoder -forceidx -ovc copy -oac copy -ss 5435 -o part2.avi file.avi
		cmd = 'mencoder -forceidx -ovc copy -oac copy %s %d -o %s %s' \
			%(option, videoCutPoint, inputFileSliceName, inputFile)
		monitoringFile = inputFileSliceName
		if (count == 1):
			estimatedFileSize = estimatedFileSizePerSec * videoCutPoint
		else:
			estimatedFileSize = estimatedFileSizePerSec * \
					(inputVideoDuration - videoCutPoint)
		os.system(cmd)
		count += 1
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
