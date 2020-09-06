#!/usr/bin/python3
import evdev

import os
import sys
import time

def main():
	for devPath in evdev.list_devices():
		device = evdev.InputDevice(devPath)
		pv(device.name)
		if (17 in device.capabilities()): # EV_LED in device.capabilities()
			keyboardDevice = device
			break
	for event in keyboardDevice.read_loop():
		if event.type == evdev.ecodes.EV_KEY:
			print(evdev.categorize(event))
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
