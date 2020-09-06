#!/usr/bin/python3
import os
import sys
import time
import socket
import json

DEBUG = False
from mcommon import *

# sl4a api help
## http://www.mithril.com.au/android/doc/index.html

# set sl4a port number
## Menu -> Preferences -> Server Port

# to start sl4a server
## Menu -> View -> Interpreters -> Menu -> Start Server -> Public
## am start --user 0 -a com.googlecode.android_scripting.action.LAUNCH_SERVER -n com.googlecode.android_scripting/.activity.ScriptingLayerServiceLauncher --ez com.googlecode.android_scripting.extra.USE_PUBLIC_IP true --ei com.googlecode.android_scripting.extra.USE_SERVICE_PORT 59898

# to stop sl4a server
## am start --user 0 -a com.googlecode.android_scripting.action.KILL_PROCESS -n com.googlecode.android_scripting/.activity.ScriptingLayerServiceLauncher --ei com.googlecode.android_scripting.extra.PROXY_PORT 59898

package = 'com.googlecode.android_scripting'
component = '%s/.activity.ScriptingLayerServiceLauncher' %(package)
host = '0.0.0.0'
port = 59898
def startServer():
	cmd = ('am', 'start', '--user', '0',
		'-n', component,
		'-a', '%s.action.LAUNCH_SERVER' %(package),
		'--ez', '%s.extra.USE_PUBLIC_IP' %(package), 'true',
		'--ei', '%s.extra.USE_SERVICE_PORT' %(package), str(port),
	)
	ret = runCmd(cmd)
	if (ret != 0):
		pi('Failed to start Sl4a server')
		return(False)
	time.sleep(3)
	pi('Sl4a server started')
	return(True)


def stopServer():
	cmd = ('am', 'start', '--user', '0',
		'-n', component,
		'-a', '%s.action.KILL_PROCESS' %(package),
		'--ei', '%s.extra.PROXY_PORT' %(package), str(port),
	)
	ret = runCmd(cmd)
	if (ret != 0):
		pi('Failed to stop Sl4a server')
		return(False)
	pi('Sl4a server stoped')
	return(True)


class Android(object):
	def __init__(self, host=host, port=port):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.connect((host, port))
		self.id = -1

	def _rpc(self, method, *args):
		self.id += 1
		data = {
			'id': self.id,
			'method': method,
			'params': args
		}
		request = json.dumps(data) + '\n'
		self.client.send(request.encode())
		response = self.client.recv(1024)
		pv(response)
		result = json.loads(response)
		if (result['error'] != None):
			pe('Android Api Error: %s', result['error'])
		return (result['id'], result['result'], result['error'])

	def __getattr__(self, name):
		def rpc_call(*args):
			return self._rpc(name, *args)
		return rpc_call
