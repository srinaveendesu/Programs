#!/usr/bin/python3
import evdev
import evdev.ecodes as e

import os
import sys
import time

def sendKey(remote, key, code, value):
	#pi('Output(%d, %d, %d)', key, code, value)
	remote.write(key, code, value)
	remote.syn()

(UP, DOWN, HOLD) = (0, 1, 2)
def main():
	for devPath in evdev.list_devices():
		device = evdev.InputDevice(devPath)
		#pv(device.name)
		if (17 in device.capabilities()): # EV_LED in device.capabilities()
			keyboardDevice = device
			break
	events = {
		e.EV_KEY: e.keys.keys(),
		e.EV_REL: (
			e.REL_X,
			e.REL_Y,
			e.REL_WHEEL
		),
	}
	remote = evdev.UInput(events)
	deviceGrabbed = False
	keyMap = {
		# mouse movement
		e.KEY_L: (e.EV_REL, ((e.REL_X,  8),)),
		e.KEY_H: (e.EV_REL, ((e.REL_X, -8),)),
		e.KEY_J: (e.EV_REL, ((e.REL_Y,  8),)),
		e.KEY_K: (e.EV_REL, ((e.REL_Y, -8),)),
		# diagonal mouse movement
		e.KEY_U: (e.EV_REL, ((e.REL_X, -8), (e.REL_Y, -8))),
		e.KEY_M: (e.EV_REL, ((e.REL_X,  8), (e.REL_Y,  8))),
		e.KEY_O: (e.EV_REL, ((e.REL_X,  8), (e.REL_Y, -8))),
		e.KEY_N: (e.EV_REL, ((e.REL_X, -8), (e.REL_Y,  8))),
		# mouse buttons
		e.KEY_S: (e.EV_KEY, ((e.BTN_LEFT, 1),)),
		e.KEY_D: (e.EV_KEY, ((e.BTN_MIDDLE, 1),)),
		e.KEY_F: (e.EV_KEY, ((e.BTN_RIGHT, 1),)),
		# mouse scroll
		e.KEY_E: (e.EV_REL, ((e.REL_WHEEL,  1),)),
		e.KEY_C: (e.EV_REL, ((e.REL_WHEEL, -1),)),
		# ctrl for block selection
		e.KEY_A: (e.EV_KEY, ((e.KEY_LEFTCTRL,  1),)),
	}
	for event in keyboardDevice.read_loop():
		if (event.type != e.EV_KEY):
			continue
		#pi('Input(%d, %d, %d)', event.type, event.code, event.value)
		if (event.code == e.KEY_LEFTMETA) and (event.value == UP):
			keyboardDevice.grab()
			deviceGrabbed = True
			#pi('grab()')
			continue
		if (deviceGrabbed != True):
			continue
		if (event.code not in keyMap):
			keyboardDevice.ungrab()
			deviceGrabbed = False
			#pi('ungrab()')
			sendKey(remote, event.type, event.code, event.value)
			#if (event.code not in (e.KEY_LEFTCTRL, e.KEY_LEFTALT, e.KEY_RIGHTCTRL, e.KEY_RIGHTALT)):
			sendKey(remote, event.type, event.code, not event.value)
			continue
		(key, codes) = keyMap[event.code]
		for (code, direction) in codes:
			sendKey(remote, key, code, (event.value * direction))
		remote.syn()
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
