#!/usr/bin/python3
import os
import sys

import os
import sys
import time
import android

host = 'localhost'
port = '59898'
def main():
	# start server
	android.startServer()
	droid = android.Android()

	# sl4a api help: http://www.mithril.com.au/android/doc/index.html

	# text to voice
	ret = droid.ttsSpeak('Hi Nandhu')
	pv(ret)

	# bluetooth
	droid.toggleBluetoothState(True, False)
	droid.bluetoothGetLocalName()
	droid.checkBluetoothState()

	# stop server
	android.stopServer()
	return(True)

if (__name__ == '__main__'):
	ret = main()
	sys.exit((1, 0)[ret])
