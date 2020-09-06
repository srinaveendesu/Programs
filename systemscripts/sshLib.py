#!/usr/bin/python3
import os
import sys
import pexpect

from mcommon import *

class InteractiveSession(pexpect.spawn):
	def __init__(self, sName):
		machineDict = getMachine(sName)
		self.ip = machineDict['ip']
		self.port = machineDict['port']
		self.user = machineDict['user']
		self.passwd = machineDict['passwd']
		self.userHostCmd = '%s@%s' %(self.user, self.ip)

	def login(self):
		self.expectCmd = 'ssh -o UserKnownHostsFile=/dev/null -p %d %s' %(self.port, self.userHostCmd)
		self._runExpect()

	def sendFiles(self, filePaths, dstPath):
		filePaths = '" "'.join(filePaths)
		self.expectCmd = 'scp -P %d -r "%s" %s:"%s"' %(self.port, filePaths, self.userHostCmd, dstPath)
		self._runExpect()

	def getFiles(self, filePaths, dstPath):
		if (len(filePaths) == 1):
			filePaths = filePaths[0]
		else:
			filePaths = '{%s}' %(','.join(filePaths))
		self.expectCmd = 'scp -P %d -r %s:"%s" "%s"' %(self.port, self.userHostCmd, filePaths, dstPath)
		self._runExpect()

	def runCmd(self, cmd):
		self.expectCmd = "ssh -o UserKnownHostsFile=/dev/null -p %d %s '%s'" %(self.port, self.userHostCmd, cmd)
		self._runExpect()

	def xlogin(self):
		self.expectCmd = 'ssh -o UserKnownHostsFile=/dev/null -p %d -X %s' %(self.port, self.userHostCmd)
		self._runExpect()

	def _runExpect(self):
		import re
		# spawning the cmd
		pv(self.expectCmd)
		pexpect.spawn.__init__(self, self.expectCmd)
		self.timeout = 60
		while (True):
			try:
				content = self.read_nonblocking(1024, 25).decode()
			except pexpect.exceptions.EOF:
				pd('reached EOF')
				break
			sys.stdout.write(content)
			if (re.search('Are you sure you want to continue connecting', content) != None):
				self.sendline('yes')
				pd('sent "yes" to authorisation')
			elif (re.search('[pP]assword', content) != None):
				self.sendline(self.passwd)
				pd('sent password')
			elif (re.search('[\$#>] ?', content) != None):
				self.sendline('')
				pd('Logged in')
				self._interact()
				return(0)
		return(0)

	def _interact(self):
		import struct
		import fcntl
		import termios
		import signal
		# signal handler for window size changes in interact mode
		def sigwinch_handler (sig, data):
			s = struct.pack('HHHH', 0, 0, 0, 0)
			termData = fcntl.ioctl(sys.stdout.fileno(), termios.TIOCGWINSZ, s)
			a = struct.unpack('hhhh', termData)
			self.setwinsize(a[0],a[1])
			pd('terminal size changed to %dx%d', a[0], a[1])
		sigwinch_handler(signal.SIGWINCH, [])
		signal.signal(signal.SIGWINCH, sigwinch_handler)
		self.interact()


class UninteractiveSession():
	def __init__(self, sName):
		import pyssh
		machineDict = getMachine(sName)
		ip = machineDict['ip']
		port = machineDict['port']
		user = machineDict['user']
		passwd = machineDict['passwd']
		self.session = pyssh.session.Session(hostname=ip, port=port, username=user, password=passwd)

	def runCmd(self, cmd):
		if (type(cmd) in (list, tuple)):
			cmd = ' '.join(cmd)
		pi('RemoteCmd: %s', cmd)
		chan = self.session.execute(cmd)
		ret = chan.return_code
		out = chan.as_str()
		pd('ret: %s', ret)
		pd('output:\n%s', out)
		return(ret, out)
