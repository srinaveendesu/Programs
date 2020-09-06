#!/usr/bin/python3
import os
import sys
import socket
import select
import evdev

# http://www.comptechdoc.org/os/linux/howlinuxworks/linux_hlkeycodes.html
KEY_MAP = {
	0x1B  : (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_ESC,),
	0x601B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_GRAVE,),
	0x311B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_1,),
	0x321B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_2,),
	0x331B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_3,),
	0x341B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_4,),
	0x351B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_5,),
	0x361B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_6,),
	0x371B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_7,),
	0x381B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_8,),
	0x391B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_9,),
	0x301B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_0,),
	0x2D1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_MINUS,),
	0x3D1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_EQUAL,),
	0x7F1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_BACKSPACE,),
	0x091B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_TAB,),
	0x711B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_Q,),
	0x771B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_W,),
	0x651B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_E,),
	0x721B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_R,),
	0x741B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_T,),
	0x791B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_Y,),
	0x751B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_U,),
	0x691B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_I,),
	0x6F1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_O,),
	0x701B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_P,),
	0x5B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_LEFTBRACE,),
	0x5D1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_RIGHTBRACE,),
	0x5C1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_BACKSLASH,),
	0x611B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_A,),
	0x731B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_S,),
	0x641B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_D,),
	0x661B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F,),
	0x671B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_G,),
	0x681B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_H,),
	0x6A1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_J,),
	0x6B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_K,),
	0x6C1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_L,),
	0x3B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_SEMICOLON,),
	0x271B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_APOSTROPHE,),
	0x0D1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_ENTER,),
	0x7A1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_Z,),
	0x781B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_X,),
	0x631B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_C,),
	0x761B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_V,),
	0x621B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_B,),
	0x6E1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_N,),
	0x6D1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_M,),
	0x2C1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_COMMA,),
	0x2E1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_DOT,),
	0x2F1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_SLASH,),
	0x201B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_SPACE,),
	0x44333B315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_LEFT,),
	0x42333B315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_DOWN,),
	0x43333B315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_RIGHT,),
	0x41333B315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_UP,),
	0x7E333B325B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_INSERT,),
	0x7E333B335B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_DELETE,),
	0x48333B315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_HOME,),
	0x46333B315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_END,),
	0x7E333B355B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_PAGEUP,),
	0x7E333B365B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_PAGEDOWN,),
	0x415B5B1B      : (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F1,),
	0x425B5B1B      : (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F2,),
	0x435B5B1B      : (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F3,),
	0x445B5B1B      : (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F4,),
	0x455B5B1B      : (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F5,),
	0x7E333B37315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F6,),
	0x7E333B38315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F7,),
	0x7E333B39315B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F8,),
	0x7E333B30325B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F9,),
	0x7E333B31325B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F10,),
	0x7E333B33325B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F11,),
	0x7E333B34325B1B: (evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_F12,),

	0x11: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_Q,),
	0x17: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_W,),
	0x05: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_E,),
	0x12: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_R,),
	0x14: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_T,),
	0x19: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_Y,),
	0x15: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_U,),
	0x09: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_I,),
	0x0F: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_O,),
	0x10: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_P,),
	0x01: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_A,),
	0x13: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_S,),
	0x04: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_D,),
	0x06: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_F,),
	0x07: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_G,),
	0x08: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_H,),
	0x0A: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_J,),
	0x0B: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_K,),
	0x0C: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_L,),
	0x1A: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_Z,),
	0x18: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_X,),
	0x03: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_C,),
	0x16: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_V,),
	0x02: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_B,),
	0x0E: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_N,),
	0x0D: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_M,),

	0x7E: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_GRAVE,), # `~`
	0x21: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_1,), # `!`
	0x40: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_2,), # `@`
	0x23: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_3,), # `#`
	0x24: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_4,), # `$`
	0x25: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_5,), # `%`
	0x5E: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_6,), # `^`
	0x26: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_7,), # `&`
	0x2A: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_8,), # `*`
	0x28: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_9,), # `(`
	0x29: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_0,), # `)`
	0x5F: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_MINUS,), # `_`
	0x2B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_EQUAL,), # `+`
	0x51: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_Q,), # `Q`
	0x57: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_W,), # `W`
	0x45: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_E,), # `E`
	0x52: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_R,), # `R`
	0x54: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_T,), # `T`
	0x59: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_Y,), # `Y`
	0x55: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_U,), # `U`
	0x49: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_I,), # `I`
	0x4F: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_O,), # `O`
	0x50: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_P,), # `P`
	0x7B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_LEFTBRACE,), # `{`
	0x7D: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_RIGHTBRACE,), # `}`
	0x7C: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_BACKSLASH,), # `|`
	0x41: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_A,), # `A`
	0x53: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_S,), # `S`
	0x44: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_D,), # `D`
	0x46: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F,), # `F`
	0x47: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_G,), # `G`
	0x48: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_H,), # `H`
	0x4A: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_J,), # `J`
	0x4B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_K,), # `K`
	0x4C: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_L,), # `L`
	0x3A: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_SEMICOLON,), # `:`
	0x22: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_APOSTROPHE,), # `'`
	0x5A: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_Z,), # `Z`
	0x58: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_X,), # `X`
	0x43: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_C,), # `C`
	0x56: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_V,), # `V`
	0x42: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_B,), # `B`
	0x4E: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_N,), # `N`
	0x4D: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_M,), # `M`
	0x3C: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_COMMA,), # `<`
	0x3E: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_DOT,), # `>`
	0x3F: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_SLASH,), # `?`
	0x50323B315B1B  : (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F1,),
	0x51323B315B1B  : (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F2,),
	0x52323B315B1B  : (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F3,),
	0x53323B315B1B  : (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F4,),
	0x7E323B35315B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F5,),
	0x7E323B37315B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F6,),
	0x7E323B38315B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F7,),
	0x7E323B39315B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F8,),
	0x7E323B30325B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F9,),
	0x7E323B31325B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F10,),
	0x7E323B33325B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F11,),
	0x7E323B34325B1B: (evdev.ecodes.KEY_LEFTSHIFT, evdev.ecodes.KEY_F12,),

	0x1B: (evdev.ecodes.KEY_ESC,), # `esc,`
	0x60: (evdev.ecodes.KEY_GRAVE,), # ```
	0x31: (evdev.ecodes.KEY_1,), # `1`
	0x32: (evdev.ecodes.KEY_2,), # `2`
	0x33: (evdev.ecodes.KEY_3,), # `3`
	0x34: (evdev.ecodes.KEY_4,), # `4`
	0x35: (evdev.ecodes.KEY_5,), # `5`
	0x36: (evdev.ecodes.KEY_6,), # `6`
	0x37: (evdev.ecodes.KEY_7,), # `7`
	0x38: (evdev.ecodes.KEY_8,), # `8`
	0x39: (evdev.ecodes.KEY_9,), # `9`
	0x30: (evdev.ecodes.KEY_0,), # `0`
	0x2D: (evdev.ecodes.KEY_MINUS,), # `-`
	0x3D: (evdev.ecodes.KEY_EQUAL,), # `=`
	0x7F: (evdev.ecodes.KEY_BACKSPACE,), # `backspace`
	0x09: (evdev.ecodes.KEY_TAB,), # `tab`
	0x71: (evdev.ecodes.KEY_Q,), # `q`
	0x77: (evdev.ecodes.KEY_W,), # `w`
	0x65: (evdev.ecodes.KEY_E,), # `e`
	0x72: (evdev.ecodes.KEY_R,), # `r`
	0x74: (evdev.ecodes.KEY_T,), # `t`
	0x79: (evdev.ecodes.KEY_Y,), # `y`
	0x75: (evdev.ecodes.KEY_U,), # `u`
	0x69: (evdev.ecodes.KEY_I,), # `i`
	0x6F: (evdev.ecodes.KEY_O,), # `o`
	0x70: (evdev.ecodes.KEY_P,), # `p`
	0x5B: (evdev.ecodes.KEY_LEFTBRACE,), # `[`
	0x5D: (evdev.ecodes.KEY_RIGHTBRACE,), # `]`
	0x5C: (evdev.ecodes.KEY_BACKSLASH,), # `\`
	0x61: (evdev.ecodes.KEY_A,), # `a`
	0x73: (evdev.ecodes.KEY_S,), # `s`
	0x64: (evdev.ecodes.KEY_D,), # `d`
	0x66: (evdev.ecodes.KEY_F,), # `f`
	0x67: (evdev.ecodes.KEY_G,), # `g`
	0x68: (evdev.ecodes.KEY_H,), # `h`
	0x6A: (evdev.ecodes.KEY_J,), # `j`
	0x6B: (evdev.ecodes.KEY_K,), # `k`
	0x6C: (evdev.ecodes.KEY_L,), # `l`
	0x3B: (evdev.ecodes.KEY_SEMICOLON,), # `;`
	0x27: (evdev.ecodes.KEY_APOSTROPHE,), # `'`
	0x0D: (evdev.ecodes.KEY_ENTER,), # `enter`
	0x7A: (evdev.ecodes.KEY_Z,), # `z`
	0x78: (evdev.ecodes.KEY_X,), # `x`
	0x63: (evdev.ecodes.KEY_C,), # `c`
	0x76: (evdev.ecodes.KEY_V,), # `v`
	0x62: (evdev.ecodes.KEY_B,), # `b`
	0x6E: (evdev.ecodes.KEY_N,), # `n`
	0x6D: (evdev.ecodes.KEY_M,), # `m`
	0x2C: (evdev.ecodes.KEY_COMMA,), # `,`
	0x2E: (evdev.ecodes.KEY_DOT,), # `.`
	0x2F: (evdev.ecodes.KEY_SLASH,), # `/`
	0x20: (evdev.ecodes.KEY_SPACE,), # `space`
	0x445B1B: (evdev.ecodes.KEY_LEFT,), # `left_arraw`
	0x425B1B: (evdev.ecodes.KEY_DOWN,), # `down_arrow`
	0x435B1B: (evdev.ecodes.KEY_RIGHT,), # `right_arrow`
	0x415B1B: (evdev.ecodes.KEY_UP,), # `up_arrow`
	0x7E325B1B: (evdev.ecodes.KEY_INSERT,), # `insert`
	0x7E335B1B: (evdev.ecodes.KEY_DELETE,), # `delete`
	0x7E315B1B: (evdev.ecodes.KEY_HOME,), # `home`
	0x7E345B1B: (evdev.ecodes.KEY_END,), # `end`
	0x7E355B1B: (evdev.ecodes.KEY_PAGEUP,), # `page_up`
	0x7E365B1B: (evdev.ecodes.KEY_PAGEDOWN,), # `page_down`
	0x415B5B1B  : (evdev.ecodes.KEY_F1,), # `F1,`
	0x425B5B1B  : (evdev.ecodes.KEY_F2,), # `F2,`
	0x435B5B1B  : (evdev.ecodes.KEY_F3,), # `F3,`
	0x445B5B1B  : (evdev.ecodes.KEY_F4,), # `F4,`
	0x455B5B1B  : (evdev.ecodes.KEY_F5,), # `F5,`
	0x7E37315B1B: (evdev.ecodes.KEY_F6,), # `F6,`
	0x7E38315B1B: (evdev.ecodes.KEY_F7,), # `F7,`
	0x7E39315B1B: (evdev.ecodes.KEY_F8,), # `F8,`
	0x7E30325B1B: (evdev.ecodes.KEY_F9,), # `F9,`
	0x7E31325B1B: (evdev.ecodes.KEY_F10,), # `F10`
	0x7E33325B1B: (evdev.ecodes.KEY_F11,), # `F11,`
	0x7E34325B1B: (evdev.ecodes.KEY_F12,), # `F12,`
}

KEY_MAP.update({
	0x6C1B: (evdev.ecodes.KEY_LEFTCTRL, evdev.ecodes.KEY_LEFTALT, evdev.ecodes.KEY_L,), # alt+l => ctrl+atl+l
})

BIND_IP = '0.0.0.0' # all available ips
PORT = 9999
def droidKeyboardServer():
	# socket initialization
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	sock.bind((BIND_IP, PORT))
	# input device initialization
	keyboard = evdev.uinput.UInput()
	# blocking for ever
	while (True):
		(rfds, wfds, xfds) = select.select([sock], [], [], 120)
		if (rfds == []):
			print('Timeout')
			break
		(keyBytes, clientAddr) = sock.recvfrom(8)
		keyInt = int.from_bytes(keyBytes, byteorder=sys.byteorder)
		print('keyInt: 0x%X' %(keyInt))
		if (keyInt not in KEY_MAP):
			print('Not Supported')
			continue
		keyTuple = KEY_MAP[keyInt]
		print('keyTuple: %s' %(repr(keyTuple)))
		# send key down event
		for key in keyTuple:
			keyboard.write(evdev.ecodes.EV_KEY, key, 1)
		# send key up event
		for key in reversed(keyTuple):
			keyboard.write(evdev.ecodes.EV_KEY, key, 0)
		# key sync
		keyboard.syn()
	return(True)

def main():
	ret = droidKeyboardServer()
	return(ret)

if (__name__ == '__main__'):
	ret = main()
	sys.exit((1, 0)[ret])


'''
# mouse sample code
from evdev import UInput, ecodes as e

mouseCapabilities = {
	e.EV_KEY: (e.BTN_LEFT, e.BTN_RIGHT, e.BTN_MIDDLE),
	e.EV_REL: (e.REL_X, e.REL_Y, e.REL_WHEEL),
}


ui = UInput(mouseCapabilities)
ui.write(e.EV_REL, e.REL_X, 10)
ui.write(e.EV_REL, e.REL_Y, 10)

ui.write(e.EV_REL, e.REL_WHEEL, 10)
ui.write(e.EV_REL, e.REL_WHEEL, -10)

ui.write(e.EV_KEY, e.BTN_LEFT, 1)
ui.syn()
'''
