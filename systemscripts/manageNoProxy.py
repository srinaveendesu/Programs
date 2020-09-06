#!/usr/bin/python3
import gi.repository.Gio

import os
import sys
import time

def usage():
	pe('Usage: %s <-a|-r> <ips/hostnames...>', sys.argv[0])

def main():
	schema = 'org.gnome.system.proxy'
	key = 'ignore-hosts'
	gsettings = gi.repository.Gio.Settings.new(schema)
	ignoreList = gsettings.get_strv(key)
	# print the ignore list if no option found
	if (len(sys.argv) == 1):
		for host in ignoreList:
			writeLog('%s\n' %(host), 'BLUE')
		return(0)
	# add or delete the host from ignore list
	option = sys.argv[1]
	hostsList = sys.argv[2:]
	if (option == '-a'):
		ignoreList.extend(sys.argv[2:])
	elif (option == '-r'):
		for host in hostsList:
			if (host in ignoreList):
				ignoreList.remove(host)
			else:
				pe('host doesn't exits: %s', host)
	else:
		pe('Unknown option: %s', option)
		usage()
		return(1)
	gsettings.set_strv(key, ignoreList)
	gsettings.apply()
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
