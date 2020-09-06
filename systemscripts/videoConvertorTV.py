#!/usr/bin/python3

import os
import sys
import time

def usage():
	pe('Usage: %s <inputfile> [<outputfile>.mp4]', sys.argv[0])

def convertTVCompatibleVideo(origVideoPath, newVideoPath):
	# convering command
	avconvCmd = ('avconv', 
			'-threads', '0',
			'-i', origVideoPath,
			'-vcodec', 'mpeg4',
			'-vsync', '2',
			'-r', '24',
			'-b', '1800k',
			'-f', 'mp4',
			'-acodec', 'libvo_aacenc',
			'-async', '1',
			'-ab', '64k',
			'-ac', '2',
			'-ar', '22050',
			'-vf', 'pad=iw:iw*9/16:(ow-iw)/2:(oh-ih)/2',
			newVideoPath)
	# converting
	pi('Converting: %s', origVideoPath)
	(ret, out) = runCmdGetOutput(avconvCmd)
	if (ret != 0):
		out = out.decode()
		if (out.find('Failed to configure input pad') != -1):
			writeLog('Reconverting video with padding adjustments', 'BLUE', BACKGROUND_BRIGHT_'YELLOW')
			writeLog('\n')
			safeRemove(newVideoPath)
			avconvCmd = avconvCmd[:-3] + ('-vf', 'pad=ih*16/9:ih:(ow-iw)/2:(oh-ih)/2')
			avconvCmd += (newVideoPath,)
			ret = runCmd(avconvCmd)
	if (ret == 0):
		pd('Successfully Converted: %s', newVideoPath)
		return(True)
	else:
		pe('Failed to Convert: %s', origVideoPath)
		return(False)

def main():
	if (len(sys.argv) < 2):
		usage()
		return(1)
	for inputFile in sys.argv[1:]:
		name = os.path.splitext(os.path.basename(inputFile))[0]
		outputFile = '%s.mp4' %(name)
		pv(outputFile)
		convertTVCompatibleVideo(inputFile, outputFile)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
