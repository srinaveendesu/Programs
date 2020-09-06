#!/usr/bin/python3

import os
import sys
import time

def usage():
	pe('Usage: %s <>', sys.argv[0])

#UP	ah p
#DOWN	d aw n
#SHOW	sh ow
#TIME	t ay m
#SILENCE	s ay l ax n s
#NEXT	n eh k s t
#INFO	ih n f ow
#DELETE	d ix l iy t
#PREV	p r iy v
#UPDATE	ax p d ey t
vocaFileStr = '''\
% NS_B
<s>		sil

% NS_E
</s>	sil

% COMMAND
YES		y eh s
NO		n ow
STOP	s t aa p
PLAY	p l ey
UNDONE	ax n d ah n
'''

grammarFileStr = '''\
S: NS_B COMMAND NS_E
'''

configFileStr = '''\
-dfa %s.dfa
-v %s.dict
-h /usr/share/julius-voxforge/acoustic/hmmdefs
-hlist /usr/share/julius-voxforge/acoustic/tiedlist
-penalty1 5.0		# first pass
-penalty2 20.0		# second pass
-iwcd1 max	# assign maximum likelihood of the same context
-gprune safe		# safe pruning, accurate but slow
-b2 200                 # beam width on 2nd pass (#words)
-sb 200.0		# score beam envelope threshold
-spmodel 'sp'		# HMM model name
-iwsp			# append a skippable sp model at all word ends
-iwsppenalty -70.0	# transition penalty for the appenede sp models
-input mic             # direct microphone input
-smpFreq 16000		# sampling rate (Hz)
-mapunk unknown
'''
#-quiet

def launchJulius():
	projectName = 'player'
	launchDir = os.path.join('/', 'tmp')
	# write voca file
	vocaFilePath = os.path.join(launchDir, '%s.voca' %(projectName))
	fd = open(vocaFilePath, 'w')
	fd.write(vocaFileStr)
	fd.close()
	# write grammar file
	grammarFilePath = os.path.join(launchDir, '%s.grammar' %(projectName))
	fd = open(grammarFilePath, 'w')
	fd.write(grammarFileStr)
	fd.close()
	# write config file
	configFilePath = os.path.join(launchDir, '%s.cfg' %(projectName))
	fd = open(configFilePath, 'w')
	fd.write(configFileStr %(projectName, projectName))
	fd.close()
	# create dfa file for julius
	mkdfaCmd = 'mkdfa %s' %(projectName)
	runCmd(mkdfaCmd, pwd=launchDir)
	# launch julius in backgroud
	juliusCmd = 'julius -C %s.cfg' %(projectName)
	(juliusPid, juliusStdin, juliusStdout) = runBg(juliusCmd, pwd=launchDir)
	pi('Launched julius with Pid: %d', juliusPid)
	juliusStdout = os.fdopen(juliusStdout)
	return(juliusStdout)

def readVoiceCmd(juliusStdout):
	import re
	expr = re.compile('sentence1:.*> ([A-Z]*) <.*')
	while (True):
		line = juliusStdout.readline()
		pd(line)
		match = expr.match(line)
		if (match != None):
			cmd = match.group(1)
			pv(cmd)
			return(cmd)

def launchFestival():
	festivalCmd = ['festival', '--pipe']
	(festivalPid, festivalStdin, festivalStdout) = runBg(festivalCmd)
	return(festivalStdin)
	
def speakText(festivalStdin, text):
	cmd = '(SayText '%s')\n' %(text)
	os.write(festivalStdin, cmd)
	return(True)

VOL_DOWN = chr(57)
VOL_UP = chr(48)
PAUSE = chr(32)
QUIT = chr(113)
def sendMplayer(mplayerStdinW, key):
	try:
		os.write(mplayerStdinW, key)
		return(True)
	except:
		return(False)

def main():
	musicDir = os.path.join(HOME, 'music')
	musicDataFile = os.path.join(ALPT, 'musicDataFile.tmp')
	# launch julius
	juliusStdout = launchJulius()
	# launch festival
	festivalStdin = launchFestival()
	# launch mplayer
	getMusicDb()
	data = readDataFile(musicDataFile)
	musicDict = data.musicDict
	fileList = list(musicDict.keys())
	count = 0
	i = 0
	while (i < len(fileList)):
		mp3File = fileList[i]
		if (musicDict[mp3File][1] != 'N'):
			i += 1
			continue
		mp3FilePath = os.path.join(musicDir, mp3File)
		pi('playing: %s', mp3FilePath)
		mplayerCmd = ['mplayer', '-ss', '10', '-volume', '80', '-msglevel', 'all=-1', mp3FilePath]
		(mplayerPid, mplayerStdinW, mplayerStdoutR) = runBg(mplayerCmd)
		while (True):
			voiceCmd = readVoiceCmd(juliusStdout)
			if (voiceCmd == 'NO'):
				sendMplayer(mplayerStdinW, QUIT)
				musicDict[mp3File][1] = 'D'
				speakText(festivalStdin, 'deleted')
				break
			elif (voiceCmd == 'YES'):
				sendMplayer(mplayerStdinW, QUIT)
				musicDict[mp3File][1] = 'L'
				speakText(festivalStdin, 'going to next')
				break
			elif (voiceCmd == 'STOP'):
				sendMplayer(mplayerStdinW, PAUSE)
				pi('Processed: %d', count)
				speakText(festivalStdin, 'keeping silence')
				musicDict
				data.musicDict = musicDict
				writeDataFile(musicDataFile, data)
				preCmd = ''
				while (True):
					voiceCmd = readVoiceCmd(juliusStdout)
					if (preCmd == voiceCmd == 'PLAY'):
						speakText(festivalStdin, 'going to play')
						sendMplayer(mplayerStdinW, PAUSE)
						break
					else:
						preCmd = voiceCmd
			elif (voiceCmd == 'UNDONE'):
				sendMplayer(mplayerStdinW, QUIT)
				musicDict[fileList[i-1]][1] = 'N'
				i -= 2
				count -= 2
				speakText(festivalStdin, 'back to previous')
				break
#			elif (voiceCmd == 'PLAY'):
#				os.read(mplayerStdoutR, 1024 * 32)
#			elif (voiceCmd == 'PREV'):
#				sendMplayer(mplayerStdinW, QUIT)
#				speakText(festivalStdin, 'going to previous')
#				i -= 3
#				break
#			elif (voiceCmd == 'INFO'):
#				sendMplayer(mplayerStdinW, PAUSE)
#				speakText(festivalStdin, 'playing %s' %(mp3File))
#				sendMplayer(mplayerStdinW, PAUSE)
#			elif (voiceCmd == 'UPDATE'):
#				sendMplayer(mplayerStdinW, PAUSE)
#				data.musicDict = musicDict
#				writeDataFile(musicDataFile, data)
#				speakText(festivalStdin, 'updated')
#				sendMplayer(mplayerStdinW, PAUSE)
#			elif (voiceCmd == 'STOP'):
#				sendMplayer(mplayerStdinW, QUIT)
#				speakText(festivalStdin, 'Exiting')
#				i = len(fileList)
#				break
		os.waitpid(mplayerPid, 0)
		i += 1
		count += 1
		speakText(festivalStdin, str(count))
	data.musicDict = musicDict
	writeDataFile(musicDataFile, data)
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
