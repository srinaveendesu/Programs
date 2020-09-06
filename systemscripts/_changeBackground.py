#!/usr/bin/python
# for automatically changing desktop background wallpaper through script
import random
import signal

import os
import sys
import time

TIME_LIMIT = 60
BREAK_TIME = 600
TERMINAL = False
DESKTOP = True
cmdFile = os.path.join('/', 'tmp', 'changeBackground')

def setPictureOption(option):
	if (TERMINAL == True):
		return()
	# sets the picture options
	# we have four options	
	# 'wallpaper', 'centered', 'scaled', 'stretched'
	gconftoolCmd = 'gconftool-2 -t str'
	pictureOptionGnomeKey = '/desktop/gnome/background/picture_options'
	cmd = '%s -s %s '%s'' %(gconftoolCmd, pictureOptionGnomeKey, option)
	runCmd(cmd)

def setImage(fullImagePath):
	if (TERMINAL == True):
		pictureOptionGnomeKey = '/apps/gnome-terminal/profiles/Profile0/background_image'
	else:
		pictureOptionGnomeKey = '/desktop/gnome/background/picture_filename'
	gconftoolCmd = 'gconftool-2 -t str'
	cmd = '%s -s %s '%s'' %(gconftoolCmd, pictureOptionGnomeKey, fullImagePath)
	runCmd(cmd)
	
def checkScreenSaver():
	while (True):
		(ret, out) = runCmdGetOutput('gnome-screensaver-command --query')
		status = out.splitlines()[0].split()[3]
		if (status == 'active'):
			pd('waiting for screen to unlock')
			time.sleep(TIME_LIMIT)
		elif (status == 'inactive'):
			pd('screen got unlock')
			break
	return(True)

def startChangingDesktop(imageFolderList, loop=False):
	# to run this process always as background
	childPid = os.fork()
	if (childPid != 0):
		# for parent process
		pi('changeBackground[PID]: %d', childPid)
		return(0)
	# child process starts here
	previousFile = ''
	currentImage = ''
	# default background image
	machineType = getMachine()
	if (machineType == OFFICE_LAPTOP):
		defaultDesktopImage = '/home/mkasula/pictures/3d_wallpapers/3d_9999733.jpg'
	elif (machineType == HL):
		defaultDesktopImage = '/usr/share/backgrounds/Life_by_Paco_Espinoza.jpg'
	# to disown from the shell
	signal.signal(signal.SIGHUP, signal.SIG_IGN)
	# exit signal handling
	def exitSignalHandler(signum, frame):
		setPictureOption('stretched')
		setImage(defaultDesktopImage)
		sys.exit(0)
	signal.signal(signal.SIGINT, exitSignalHandler)
	signal.signal(signal.SIGQUIT, exitSignalHandler)
	signal.signal(signal.SIGABRT, exitSignalHandler)
	signal.signal(signal.SIGTERM, exitSignalHandler)
	# command signal handling
	def cmdSignalHandler(signum, frame):
		cmdFd = open(cmdFile, 'r')
		cmd = cmdFd.read().strip()
		cmdFd.close()
		os.unlink(cmdFile)
		pv('Got Signal')
		pv(cmd)
		if (cmd == 'skip'):
			pass # signal interrupt is enough for skipping the image
		elif (cmd == 'delete'):
			pd('Deleting: %s', currentImage)
			os.unlink(currentImage)
		elif (cmd == 'prev'):
			pd('PrevFile: %s', previousFile)
			cmdFd = open(cmdFile, 'w')
			cmdFd.write(previousFile)
			cmdFd.close()
		elif (cmd == 'break'):
			setPictureOption('stretched')
			setImage(defaultDesktopImage)
			while(1):
				time.sleep(BREAK_TIME)
				cmd = 'gdialog --separate-output --yesno 'Can I start' 10 10'
				if (runCmd(cmd) == 0):
					break
				pd('Going to sleep again')
			setPictureOption('scaled')
		elif (cmd == 'kill'):
			os.kill(os.getpid(), signal.SIGINT)
		else:
			pe('Unknown signalString')
		return True
	signal.signal(signal.SIGUSR1, cmdSignalHandler)
	# get all the supported files from the given directory recursively
	imageList = []
	for imageFolder in imageFolderList:
		for fileType in ['*.jpg', '*.png', '*.bmp', '*.JPG', '*.PNG', '*.BMP']:
			imageList.extend([os.path.join(imageFolder, f) \
					for f in findFiles(fileType, imageFolder)])
	# sort randomly
	random.shuffle(imageList, random=random.random)
	# start rendering background images
	setPictureOption('scaled')
	imageListLen = len(imageList)
	i = 0
	while (i < imageListLen):
		# pause if screen-saver got active
		checkScreenSaver()
		# render the images
		currentImage = os.path.abspath(imageList[i])
		setImage(currentImage)
		time.sleep(TIME_LIMIT)
		previousFile = currentImage
		i += 1
		# looping the images
		if (loop == True) and (i == imageListLen):
			random.shuffle(imageList, random=random.random)
			i = 0
	notifySend(S, 'Images Completed', 'changeBackground')
	setPictureOption('stretched')
	setImage(defaultDesktopImage)
	os._exit(0)

def sendCmd(cmd):
	# write the command into the command file
	cmdFd = open(cmdFile, 'w')
	cmdFd.write(cmd)
	cmdFd.close()
	# send sigusr1 signal to the main process
	mainProcessPid = getMainProcessPid()
	if (mainProcessPid == False):
		sys.exit(1)
	os.kill(mainProcessPid, signal.SIGUSR1)
	if (cmd == 'prev'):
		time.sleep(1)
		cmdFd = open(cmdFile, 'r')
		previousFile = cmdFd.read().strip()
		cmdFd.close()
		os.unlink(cmdFile)
		pv(previousFile)
	return(0)

def usage():
	pe('Usage: %s [-t|-skip|-delete|-break|-kill|-prev|-loop] [folderPaths...]')
	return True

def main():
	if (len(sys.argv) < 2):
		usage()
		sys.exit(1)
	# launch program on terminal/desktop
	if ('-t' in sys.argv):
		global DESKTOP
		global TERMINAL
		DESKTOP = False
		TERMINAL = True
		# delete the -t option
		index = sys.argv.index('-t')
		del sys.argv[index]
	# set the timelimit as per the arg
	if ('-tl' in sys.argv):
		global TIME_LIMIT
		index = sys.argv.index('-tl')
		TIME_LIMIT = int(sys.argv[index + 1])
		del sys.argv[index]
		del sys.argv[index]
	# here the branching of programs occurs
	if (sys.argv[1] == '-skip'): # alt+S
		ret = sendCmd('skip')
	elif (sys.argv[1] == '-prev'):
		ret = sendCmd('prev')
	elif (sys.argv[1] == '-delete'): # alt+D
		ret = sendCmd('delete')
	elif (sys.argv[1] == '-break'): # alt+B
		ret = sendCmd('break')
	elif (sys.argv[1] == '-kill'):
		ret = sendCmd('kill')
	elif (sys.argv[1] == '-loop'):
		ret = startChangingDesktop(sys.argv[2:], loop=True)
	else:
		ret = startChangingDesktop(sys.argv[1:])
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
