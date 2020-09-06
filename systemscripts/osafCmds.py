#!/usr/bin/python
'''
This script is written to have shortcuts commands to do some of the operation
of opensaf on the cluster. This script is provided with the self explanatary
documentation printed if it is used with wrong arguments

To configure the setup details:
	* open the script in any editor and change the values of dictonary as
	  'username@machine_ip': 'node_name' 		# for each node
	  Ex: 'root@192.168.56.101': 'SC-1'			# for SC-1 node
	  some other examples of node entries were there in the script

To run the script for the first time after configuration:
	$ cd /script/dir/path
	$ ./osafCmds.py
		* this will print some cmds that need to be executed on the same terminal
		  -> alias cmd for easy access to the script
			 # it will add shortcut alias 'o' to the full path of the script
		  -> export cmd for bash completion delimiter
		  -> complete cmd for bash completion of the script's internal cmds
			 # adds bash completions so that the script internal commands can be
		       completed with double tab key (like command completion in linux terminal)
		* execute the commands returned by the script
	$ o sshKeySend
		* this will sends ssh keys to all the cluster nodes
		* just follow the ssh terminal and input the passwords of each node

To use the internal commands of the script
	$ o <any_internal_cmd>
		* will print full detailed description of its usage
'''

import os
import sys
import time
import commands
import traceback

# give the details of cluster
machines = { \
'root@192.168.56.101': 'SC-1',
'root@192.168.56.102': 'SC-2',
'root@192.168.56.103': 'PL-3'
}
inv_machines = dict(zip(machines.values(), machines.keys()))

## for debug ####################################################
#def _getstatusoutput(cmd):
#	print 'running cmd:', cmd
#	return('0', 'output')
#commands.getstatusoutput = _getstatusoutput
#def _system(cmd):
#	print 'running cmd:', cmd
#	return('0', 'output')
#os.system = _system
#################################################################

def sshKeySend():
	'''
	sshKeySend
	  * this will sends ssh keys to the remote machines
	  Ex: o sshKeySend
		  # this may ask for the remote machine's passwords
	'''
	homeDir = HOME
	sshKeyFile = os.path.join(homeDir, '.ssh/id_rsa.pub')
	if(not os.path.exists(sshKeyFile)):
		cmd = 'ssh-keygen -t rsa'
		sys.stdout.write(BLUE)
		sys.stdout.write('Running cmd: %s\n' %(cmd))
		sys.stdout.write(NORMAL)
		os.system(cmd)
	for machine in machines:
		cmd = 'ssh-copy-id -i ~/.ssh/id_rsa.pub %s' %(machine)
		sys.stdout.write(BLUE)
		sys.stdout.write('Running cmd: %s\n' %(cmd))
		sys.stdout.write(NORMAL)
		os.system(cmd)

def sshKeyClean():
	'''
	sshKeyClean
	  * this will clean up the ssh keys entries from all machines which
	    were send by the 'sshKeySend' 
	  Ex: o sshKeyClean
	'''
	(ret, out) = commands.getstatusoutput('hostname')
	hostName = out.strip()
	cmd1 = 'sed -e '/%s/ d' ~/.ssh/authorized_keys > /tmp/delme' %(hostName)
	cmd2 = 'mv /tmp/delme ~/.ssh/authorized_keys'
	for machine in machines:
		_runCmd(machine, cmd1)
		_runCmd(machine, cmd2) 

def _runCmd(machine, cmd):
	''' _runCmd <machine> <cmd> '''
	cmd = 'ssh %s '%s'' %(machine, cmd)
	sys.stdout.write(BLUE)
	sys.stdout.write('Running cmd[%s]: %s\n' %(machines[machine], cmd))
	sys.stdout.write(NORMAL)
	sys.stdout.flush()
	ret = os.system(cmd)
	return(ret)

def _getFile(machine, src, dest):
	''' _getFile <machine> <src> <dest> '''
	cmd = 'scp -r %s:%s %s' %(machine, src, dest)
	print('Running cmd[%s]: %s' %(machines[machine], cmd))
	(ret, out) = commands.getstatusoutput(cmd)
	if (ret == 0):
		print('Succuss')
	else:
		print('Err Output:\n%s' %(out))

def _sendFile(machine, src, dest):
	''' _sendFile <machine> <src> <dest> '''
	cmd = 'scp -r %s %s:%s' %(src, machine, dest)
	print('Running cmd[%s]: %s' %(machines[machine], cmd))
	(ret, out) = commands.getstatusoutput(cmd)
	if (ret == 0):
		print('Succuss')
	else:
		print('Err Output:\n%s' %(out))

def runOnOneMachine(machineNo, cmd):
	'''
	$ runOnOneMachine <machineNo> <cmd>
		* this will run cmd on the selected remote machine 
		* machineNo: is a suffix count of the node name
					 ex: 1 for SC-1
						 2 for SC-2
						 3 for PL-3
						 4 for PL-4
						 and so on... 
		* cmd: is a cmd string in quotation marks
		Ex: $ o runOnOneMachine 1 'ls /'
			# to get the list of file at the / on SC-1 machine
	'''
	for machineName in inv_machines.keys():
		if (machineName.find(machineNo) != -1):
			machine = inv_machines[machineName]
			_runCmd(machine, cmd)

def runOnControllers(cmd):
	'''
	runOnControllers <cmd>
		* this will run cmd on two controller machines at the same time
		* cmd: is a cmd string in quotation marks
		Ex: $ o runOnControllers 'ls /'
		    # to get the list of files at the / on SC-1 and SC-2 machine
	'''
	for m in inv_machines.keys():
		if (m.startswith('SC')):
			machine = inv_machines[m]
			_runCmd(machine, cmd)

def runOnAllMachines(cmd):
	'''
	runOnAllMachines <cmd>
	  * this will run cmd on all machines at the same time
	  * cmd: is a cmd string in quotation marks
	  Ex: $ o runOnAllMachines 'ls /'
	      # to get the list of files at the / on all machines
	'''
	for m in machines.keys():
		_runCmd(m, cmd)

def getFileFromOneMachine(machineNo, src, dest):
	'''
	getFileFromOneMachine <machineNo> <src> <dest>
	  * this will get file from one selected remote machine 
	  * machineNo: is a suffix count of the node name
	  * src: source location on the remote machine
	  * dest: destination location of the current machine
	  Ex: $ o getFileFromOneMachine 3 /source/dir/File.txt /destination/dir/File.txt
	      # to get File.txt from PL-3 machine
	'''
	for machineName in inv_machines.keys():
		if (machineName.find(machineNo) != -1):
			machine = inv_machines[machineName]
			_getFile(machine, src, dest)

def getFileFromControllers(src, dest):
	'''
	getFileFromControllers <src> <dest>
	  * this will get file from two controller machines
	  * src: source location on the remote machine
	  * dest: destination location of the current machine
	  Ex: $ o getFileFromControllers /source/dir/File.txt /destination/dir/File.txt
	      # this will get file from SC-1 and SC-2 machines and the machine name will be
	  	  appended to the file name for identification, like: File.txt_SC-1, File.txt_SC-2
	'''
	for m in inv_machines.keys():
		if (m.startswith('SC')):
			machine = inv_machines[m]
			_getFile(machine, src, '%s_%s' %(dest, m))

def getFileFromAll(src, dest):
	'''
	getFileFromAll <src> <dest>
	  * this will get file from all machine 
	  * src: source location on the remote machine
	  * dest: destination location of the current machine
	  Ex: $ o getFileFromAll /source/dir/File.txt /destination/dir/File.txt
	      # this will get file from all machines and the machine name will be
		    appended to the file name for identification, like: File.txt_SC-1, File.txt_SC-2
	'''
	for m in machines.keys():
		_getFile(m, src, '%s_%s' %(dest, machines[m]))

def pullFromOneMachine(machineNo, basename):
	'''
	pullFromOneMachine <machineNo> <basename>
	  * this will get a file from one selected remote machine and the source location
	    will be taken as current $PWD/basename
	  * machineNo: is a suffix count of the node name
	  * basename: basename of the file
	  Ex: $ o pullFromOneMachine 3 File.txt
	      # to get file from PL-3 machine
	'''
	pwd = os.getcwd()
	src = os.path.join(pwd, basename)
	getFileFromOneMachine(machineNo, src, basename)

def pullFromControllers(basename):
	'''
	pullFromControllers <basename>
	  * this will get a file from two controller machines and the source location
	    will be taken as current $PWD/basename
	  * machineNo: is a suffix count of the node name
	  * basename: basename of the file
	  Ex: $ o pullFromControllers File.txt
	      # this will get files from SC-1 and SC-2 machines and the machine name will be
		    appended to the file name for identification, like: File.txt_SC-1, File.txt_SC-2
	'''
	pwd = os.getcwd()
	src  = os.path.join(pwd, basename)
	getFileFromControllers(src, basename)

def pullFromAll(basename):
	'''
	pullFromAll <basename>
	  * this will get a file from all machines and the source location
	  will be taken as current $PWD/basename
	  * machineNo: is a suffix count of the node name
	  * basename: basename of the file
	  Ex: $ o pullFromAll File.txt
	      # this will get files from all machines and the machine name will be
		    appended to the file name for identification, like: File.txt_SC-1, File.txt_SC-2
	'''
	pwd = os.getcwd()
	src  = os.path.join(pwd, basename)
	getFileFromAll(src, basename)

def sendFileToOneMachine(machineNo, src, dest):
	'''
	sendFileToOneMachine <machineNo> <src> <dest>
	  * this will send file to selected remote machine 
	  * machineNo: is a suffix count of the node name
	  * src: source location on the current machine
	  * dest: destination location of the remote machine
	  Ex: $ o sendFileToOneMachine 3 source/dir/File.txt /destination/dir/File.txt
	      # to send source file to PL-3 machine
	'''
	for machineName in inv_machines.keys():
		if (machineName.find(machineNo) != -1):
			machine = inv_machines[machineName]
			_sendFile(machine, src, dest)

def sendFileToControllers(src, dest):
	'''
	sendFileToControllers <src> <dest>
	  * this will send file to two controller machines
	  * src: source location on the current machine
	  * dest: destination location of the remote machine
	  Ex: $ o sendFileToControllers source/dir/File.txt /destination/dir/File.txt
	      # to send source file to SC-1 and SC-2 machines
	'''
	for m in inv_machines.keys():
		if (m.startswith('SC')):
			machine = inv_machines[m]
			_sendFile(machine, src, dest)

def sendFileToAll(src, dest):
	'''
	sendFileToAll <src> <dest>
	  * this will send file to all machines
	  * src: source location on the current machine
	  * dest: destination location of the remote machine
	  Ex: $ o sendFileToAll source/dir/File.txt /destination/dir/File.txt
	      # to send source file to all machines
	'''
	for m in machines.keys():
		_sendFile(m, src, dest)

def pushToOneMachine(machineNo, basename):
	'''
	pushToOneMachine <machineNo> <basename>
	  * this will send file to selected remote machine and places the file at the 
	    same current pwd location, that is why destination if not required here
	  * machineNo: is a suffix count of the node name
	  * basename: basename of the file
	  Ex: $ o pushToOneMachine 3 File.txt
	      # to send source file to PL-3 machine and places the file at $PWD/File.txt
	'''
	pwd = os.getcwd()
	dest = os.path.join(pwd, basename)
	sendFileToOneMachine(machineNo, basename, dest)

def pushToControllers(basename):
	'''
	pushToControllers <basename>
	  * this will send file to two controller machines and places the file at the 
	    same current pwd location, that is why destination if not required here
	  * machineNo: is a suffix count of the node name
	  * basename: basename of the file
	  Ex: $ o pushToControllers File.txt
	      # to send source file to controller machines and places the file at $PWD/File.txt
	'''
	pwd = os.getcwd()
	dest = os.path.join(pwd, basename)
	sendFileToControllers(basename, dest)

def pushToAll(basename):
	'''
	pushToAll <basename>
	  * this will send file to all machines and places the file at the 
	    same current pwd location, that is why destination if not required here
	  * machineNo: is a suffix count of the node name
	  * basename: basename of the file
	  Ex: $ o pushToAll File.txt
	      # to send source file to all machines and places the file at $PWD/File.txt
	'''
	pwd = os.getcwd()
	dest = os.path.join(pwd, basename)
	sendFileToAll(basename, dest)

def killVarlogMessages():
	'''
	killVarlogMessages
	  * this will stop the previously launched 'collectVarLogMessages' tailing
	  Ex: o killVarlogMessages
	'''
	cmd = 'ps -o pid,comm'
	(ret, out)= commands.getstatusoutput(cmd)
	sshPid = []
	for process in out.splitlines():
		t = process.split()
		if (t[1].find('ssh') != -1):
			sshPid.append(int(t[0].strip()))
	for pid in sshPid:
		try:
			os.kill(pid, 9)
			os.waitpid(pid, 0)
		except:
			continue

def _listenVarLogMessages(machine, prefix):
	''' listenVarLogMessages <machine> <prefix> '''
	fileName = '%s_var_log_messages_%s' %(prefix, machines[machine])
	fd = open(fileName, 'a')
	fd.write('=======================================\n')
	fd.close()
	cmd = 'ssh %s 'tail -f /var/log/messages' >> %s' %(machine, fileName)
	childPid = os.fork()
	if (childPid == 0):
		os.system(cmd)
		os._exit(0)
	else:
		print 'childPid:', childPid

def collectVarLogMessages(prefix):
	'''
	collectVarLogMessages <prefix>
	  * this will launch separate /var/log/messages tailing on each remote machine and
	    re-directs the outputs in different files suffixed by node names
	  * prefix: prefix for the logfile name
	  Ex: $ o collectVarLogMessages test1
		  # this will starts tailing of /var/log/messages into a files like: test1_var_log_messages_SC-1
	'''
	for m in machines.keys():
		_listenVarLogMessages(m, prefix)
	
def getCmdLogs(cmd, logFile):
	'''
	getCmdLogs <cmd> <prefix>
	  * this will run cmd on all machines and logs the outputs of the
	    cmds into the file suffixed with node names
	  * cmd: is a cmd string in quotation marks
	  * prefix: prefix for the logfile to be created
	  Ex: $ o getCmdLogs 'ls /' ls_output
	      # this will run 'ls /' cmd on all machines and writes a logfiles of
	  	  cmd outputs in file like: ls_output_SC-1, ls_output_SC-2
	'''
	for m in machines:
		(ret, out) = commands.getstatusoutput(cmd)
		fd = open('%s_%s' %(logFile, machines[m]) , 'w')
		fd.write(out)
		fd.close()

def _sorting(x):
	value = int(x.split('-')[1])
	return(value)

def startOpensaf():
	'''
	startOpensaf
	  * this will starts the opensaf on all the machines from SC-1 to PL-#
	  Ex: o startOpensaf
	'''
	cmd = '/etc/init.d/opensafd start'
	sMachines = inv_machines.keys()
	sMachines = sorted(sMachines, key=_sorting)
	for m in sMachines:
		_runCmd(inv_machines[m], cmd)
		time.sleep(10)
	
def stopOpensaf():
	'''
	stopOpensaf
	  * this will stops the opensaf on all the machines from PL-# to SC-1 
	  Ex: o stopOpensaf
	'''
	cmd = '/etc/init.d/opensafd stop'
	rMachines = inv_machines.keys()
	rMachines = sorted(rMachines, key=_sorting)
	rMachines.reverse()
	for m in rMachines:
		_runCmd(inv_machines[m], cmd)

def restartOpensaf():
	'''
	restartOpensaf
	  * this will restarts the opensaf on all the machines
	    stopping: PL-# to SC-1 
	    starting: SC-1 to PL-#
	  Ex: o restartOpensaf
	'''
	stopOpensaf()
	startOpensaf()

def getOpensafStatus():
	'''
	getOpensafStatus
	  * this get the status of the opensaf
	  * runs the following two cmds on each node
		  cmd1 = 'ps ax | grep saf'
		  cmd2 = '/etc/init.d/opensafd status'
	  Ex: o getOpensafStatus
	'''
	cmd1 = 'ps ax | grep saf'
	cmd2 = '/etc/init.d/opensafd status'
	for m in machines:
		_runCmd(m, cmd1)
		_runCmd(m, cmd2)

def getCrashFileList():
	'''
	getCrashFileList
	  * this will get the list of crash files if created at the location /var/crash/opensaf/
	    along with the date stamp of the remote machine
	  Ex: o getCrashFileList
	'''
	cmd = 'date; ls -l /var/crash/opensaf/'
	for m in machines:
		_runCmd(m, cmd)

def createBaseXml():
	'''
	createBaseXml
	  * this will create a base xml of 4 node setup and copies to the /etc/opensaf/imm.xml
	  * runs the following cmds on each controller node
		  cmd1 = 'cd /usr/share/opensaf/immxml'
		  cmd2 = './immxml-clustersize -s 2 -p 2'
		  cmd3 = './immxml-configure -o standard.xml'
		  cmd4 = 'cp standard.xml /etc/opensaf/imm.xml'
	  Ex: o createBaseXml
	'''
	immDir = '/usr/share/opensaf/immxml'
	cmd1 = 'cd %s; ./immxml-clustersize -s 2 -p 2' %(immDir)
	cmd2 = 'cd %s; ./immxml-configure -o standard.xml' %(immDir)
	cmd3 = 'cp %s/standard.xml /etc/opensaf/imm.xml' %(immDir)
	runOnControllers(cmd1)
	runOnControllers(cmd2)
	runOnControllers(cmd3)
	return(0)

def _initialise(module):
	if ('IFS' in os.environ):
		return(True)
	else:
		completionCmd = ''
		aliasName = 'o'
		functionNames = []
		for function in module.__dict__:
			if (not function.startswith('_')) and \
					(str(module.__dict__[function]).find('function') != -1):
				functionNames.append(function)
		completionCmd += 'alias %s='%s'\n' %(aliasName, os.path.realpath(sys.argv[0]))
		completionCmd += 'export IFS=' '\n'
		completionCmd += 'complete -W '%s' %s' %(' '.join(functionNames), aliasName)
		print('===: Please run these cmds :===\n%s' %(completionCmd))
		sys.exit(0)

BLUE = '%c%s\r' %(27,'[34m')
NORMAL = '%c%s\r' %(27,'[0m')
def _main():
	module = sys.modules['__main__']
	_initialise(module)
	if (len(sys.argv) < 2):
		print('Usage: %s <functionName> <args...>' %(sys.argv[0]))
		sys.exit(1)
	functionName = sys.argv[1]
	functionArgs = sys.argv[2:]
	# get the function name
	try:
		functionPointer = module.__dict__[functionName]
	except Exception, e:
		print('%s: No such internal command in the script\n' %(functionName))
		print('Exception: %s' %(sys.exc_info()[0]))
		print('Exception Msg: %s' %(sys.exc_info()[1]))
		traceback.print_tb(sys.exc_info()[2])
		sys.exit(1)
	# call the function
	try:
		ret = functionPointer(*functionArgs)
	except Exception, e:
		print('Usage: %s' %(functionPointer.__doc__))
		print('Exception from '%s': %s' %(functionName, e))
		print('Exception: %s' %(sys.exc_info()[0]))
		print('Exception Msg: %s' %(sys.exc_info()[1]))
		traceback.print_tb(sys.exc_info()[2])
		sys.exit(1)
	return(ret)

if (__name__ == '__main__'):
	ret = _main()
	sys.exit(ret)
