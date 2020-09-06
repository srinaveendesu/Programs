#!/usr/bin/python
import os
import sys
import re

USERNAME = 'mkasula'
logFile = '/tmp/applyCtPatch.log'
logFd = None
def printLog(string):
	global logFd
	if (logFd == None):
		logFd = open(logFile, 'w')
	logFd.write('%s\n' %(string))
	logFd.flush()
	sys.stdout.write('%s\n' %(string))
	sys.stdout.flush()
	return(True)

def runCmd(cmd):
	global logFd
	if (logFd == None):
		logFd = open(logFile, 'w')
	printLog('Runinng Cmd: %s' %(cmd))
	ret = os.system(cmd + '\n')
	if (ret != 0):
		return(False)
	else:
		return(True)

def checkEnv():
	cwd = os.getcwd()
	if (cwd != '/vobs/goahead'):
		printLog('Current Dir is not: /vobs/goahead')
		return(False)
	return(True)

# dirTree = {
#	'checkOutStatus': False,
#	'filesList': {'filename': None, 'folderName': dirTree, ...},
#}
def buildDirTree(patchFile):
	e = re.compile('^diff --git a/(.*) b/.*$')
	dirTree = {'checkOutStatus': False, 'filesList': {}}
	patchFileFd = open(patchFile, 'r')
	for line in patchFileFd:
		match = e.match(line)
		if (match != None):
			fp = match.group(1)
			printLog('fp: %s' %(fp))
			dirList = fp.split('/')
			td = dirTree
			for dirName in dirList[:-1]:
				if (dirName not in td['filesList'].keys()):
					td['filesList'][dirName] = {'checkOutStatus': False, 'filesList': {}}
				td = td['filesList'][dirName]
			td['filesList'][dirList[-1]] = None
	return(dirTree)
	
def printDirTree(dirTree, tabCount=0):
	for fp in dirTree['filesList'].keys():
		for i in range(tabCount):
			sys.stdout.write('  ')
		sys.stdout.write(fp + '\n')
		if (type(dirTree['filesList'][fp]) == dict):
			printDirTree(dirTree['filesList'][fp], tabCount+1)

def createBranch(patchFile):
	bugId = os.path.splitext(os.path.basename(patchFile))[0]
	branchName = '%s_%s' %(USERNAME, bugId)
	customConfigSpecTemplate = '''\
element * CHECKEDOUT
element * .../%s/LATEST
element * .../ocsa_3.3_mp/LATEST  -mkbranch %s
element * .../saffire_II/SAFFIRE_3.3_052312_RC4  -mkbranch ocsa_3.3_mp
element * /main/SAFFIRE_3.3_052312_RC4 -mkbranch ocsa_3.3_mp
element * /main/LATEST -mkbranch ocsa_3.3_mp
'''
	customConfigSpec = customConfigSpecTemplate %(branchName, branchName)
	customConfigSpecFile = '%s/customConfigSpecFile.txt' %(HOME)
	fd = open(customConfigSpecFile, 'w')
	fd.write(customConfigSpec)
	fd.close()
	runCmd('cleartool setcs %s' %(customConfigSpecFile))
	runCmd('cleartool mkbrtype -nc %s_%s' %(USERNAME, bugId))
	return(branchName)

def isClearCaseFile(filePath):
	import commands
	cmd = 'cleartool ls %s' %(filePath)
	(ret, out) = commands.getstatusoutput(cmd)
	if (ret != 0):
		return(False)
	elif (out.find('@@/main') != -1) and (out.find('Rule:') != -1):
		return(True)
	else:
		printLog('%s: File exists, but not been tracked by ClearCase' %(filePath))
		return(False)

def createDirTree(dirTree, parentPath='.'):
	for f in dirTree['filesList'].keys():
		fullpath = os.path.join(parentPath, f)
		currentDirCheckoutFlag = False
		if (isClearCaseFile(fullpath) == False):
			if (dirTree['checkOutStatus'] == False):
				runCmd('cleartool co -nc %s' %(parentPath))
				dirTree['checkOutStatus'] = True
			if (type(dirTree['filesList'][f]) == dict):
				runCmd('cleartool mkdir -nc %s' %(fullpath))
				dirTree['filesList'][f]['checkOutStatus'] = True
			else:
				runCmd('cleartool mkelem -nc %s' %(fullpath))
		if (type(dirTree['filesList'][f]) == dict):
			createDirTree(dirTree['filesList'][f], fullpath)

def patchDryRun(patchFile):
	patchCmd = 'patch --dry-run -g1 -p1 < %s' %(patchFile)
	if (runCmd(patchCmd) != True):
		sys.exit(1)

def applyPatch(patchFile):
	patchCmd = 'patch -g1 -p1 < %s' %(patchFile)
	runCmd(patchCmd)

def checkIn(dirTree, basePath='.'):
	for fp in dirTree['filesList'].keys():
		fullpath = os.path.join(basePath, fp)
		if (type(dirTree['filesList'][fp]) == dict):
			checkIn(dirTree['filesList'][fp], fullpath)
		else:
			runCmd('cleartool ci -nc %s' %(fullpath))
	if (dirTree['checkOutStatus'] == True):
		runCmd('cleartool ci -nc %s' %(basePath))

def printCtls(dirTree, currentPath=''):
	import commands
	for fp in dirTree['filesList'].keys():
		fullPath = os.path.join(currentPath, fp)
		if (dirTree['filesList'][fp] == None):
			cmd = 'cleartool ls %s' %(fullPath)
			(ret, out) = commands.getstatusoutput(cmd)
			print(out.split()[0])
		elif (type(dirTree['filesList'][fp]) == dict):
			printCtls(dirTree['filesList'][fp], fullPath)

def main():
	if (len(sys.argv) < 2):
		printLog('Usage: %s <patchfile>' %(sys.argv[0]))
		sys.exit(1)
	patchFile = sys.argv[1]
	if (checkEnv() != True):
		sys.exit(1)
	branchName = createBranch(patchFile)
	patchDryRun(patchFile)
	dirTree = buildDirTree(patchFile)
	printDirTree(dirTree)
	createDirTree(dirTree)
	applyPatch(patchFile)
	checkIn(dirTree)
	print('CheckedIn ClearCase Branch: %s' %(branchName))
	print('Files Changed:')
	printCtls(dirTree)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
