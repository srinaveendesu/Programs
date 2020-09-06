#!/usr/bin/python3

import os
import sys
import time

def usage():
	pe('Usage: %s <cmd> <args>...', sys.argv[0])

startUpFileTemplate = '''\
[Desktop Entry]
Type=Application
Exec=%s %s
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_IN]=%s
Name=%s
Comment[en_IN]=%s
Comment=startup for '%s'
'''

def main():
	if (len(sys.argv) < 2):
		usage()
		return(1)
	# find full path of execFile
	execFile = sys.argv[1]
	if (os.path.exists(execFile)):
		execFullPath = os.path.realpath(execFile)
		baseName = os.path.basename(execFullPath)
		(execName, execExt) = os.path.splitext(baseName)
	else:
		(ret, out) = runCmdGetOutput('which %s' %(execFile))
		if (ret != 0):
			pe('full path of execFile not found: %s', execFile)
			return(1)
		execFullPath = out.strip()
		(execName, execExt) = os.path.splitext(execFile)
	# get other options
	if (len(sys.argv) > 2):
		args = ' '.join(sys.argv[2:])
	else:
		args = ''
	# create startUp entry
	autoStartDir = os.path.join(HOME, '.config', 'autostart')
	if (not os.path.isdir(autoStartDir)):
		os.makedirs(autoStartDir)
	startUpFile = '%s.desktop' %(execName)
	startUpFilePath = os.path.join(autoStartDir, startUpFile)
	fd = open(startUpFilePath, 'w')
	startUpStr = startUpFileTemplate %(execFullPath, args, execName, execName, execName, execName)
	fd.write(startUpStr)
	fd.close()
	pi('Successfully Created: %s', startUpFilePath)
	pi('File Content: \n%s', startUpStr)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
