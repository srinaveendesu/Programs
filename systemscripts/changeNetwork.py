#!/usr/bin/python3
import gi.repository.Gio
import dbus

import os
import sys
import time

ROUTER_NETWORK = 0
DIRECT_NETWORK = 1

def usage():
	pe('Usage: %s <router|direct>', sys.argv[0])

def setProxy(choice):
	proxyTypeList = ['http', 'https', 'ftp', 'socks']
	proxyHost = 'www-proxy.us.oracle.com'
	proxyPort = 80
	# set the dconf configuration values
	mainSchema = 'org.gnome.system.proxy'
	if (choice == True):
		modeValue = 'manual'
		for proxyType in proxyTypeList:
			schema = '%s.%s' %(mainSchema, proxyType)
			gsettings = gi.repository.Gio.Settings.new(schema)
			gsettings.set_string('host', proxyHost)
			gsettings.set_int('port', proxyPort)
	else:
		modeValue = 'none'
	gsettings = gi.repository.Gio.Settings.new(mainSchema)
	gsettings.set_string('mode', modeValue)
	gsettings.apply()
	# set the dbus configuration
	qdbusCmd = ('pudo', 'qdbus', '--system', 'com.ubuntu.SystemService', '/', 'com.ubuntu.SystemService.set_proxy')
	for proxyType in proxyTypeList:
		cmd = qdbusCmd + (proxyType, )
		if (choice == True):
			cmd += ('%s://%s:%d' %(proxyType, proxyHost, proxyPort),)
		else:
			cmd += ('',)
		runCmd(cmd)
	return(True)
	
def changeNetworkConfig(choice):
	systemBus = dbus.SystemBus()
	proxyObject = systemBus.get_object('org.freedesktop.NetworkManager', '/org/freedesktop/NetworkManager/Settings/8')
#	settings = proxyObject.GetSettings()
	if (choice == ROUTER_NETWORK):
		settings = dbus.Dictionary({dbus.String(u'802-3-ethernet'): dbus.Dictionary({dbus.String(u'duplex'): dbus.String(u'full', variant_level=1), dbus.String(u's390-options'): dbus.Dictionary({}, signature=dbus.Signature('ss'), variant_level=1), dbus.String(u'mac-address'): dbus.Array([dbus.Byte(212), dbus.Byte(190), dbus.Byte(217), dbus.Byte(30), dbus.Byte(213), dbus.Byte(199)], signature=dbus.Signature('y'), variant_level=1)}, signature=dbus.Signature('sv')), dbus.String(u'connection'): dbus.Dictionary({dbus.String(u'timestamp'): dbus.UInt64(1403959433, variant_level=1), dbus.String(u'type'): dbus.String(u'802-3-ethernet', variant_level=1), dbus.String(u'id'): dbus.String(u'Wired Connection 1', variant_level=1), dbus.String(u'uuid'): dbus.String(u'2958a863-c599-4f01-81ff-d0b20ff0fae7', variant_level=1)}, signature=dbus.Signature('sv')), dbus.String(u'ipv4'): dbus.Dictionary({dbus.String(u'routes'): dbus.Array([], signature=dbus.Signature('au'), variant_level=1), dbus.String(u'addresses'): dbus.Array([dbus.Array([dbus.UInt32(373974026), dbus.UInt32(24), dbus.UInt32(21652490)], signature=dbus.Signature('u'))], signature=dbus.Signature('au'), variant_level=1), dbus.String(u'dns'): dbus.Array([dbus.UInt32(61739702), dbus.UInt32(78516918)], signature=dbus.Signature('u'), variant_level=1), dbus.String(u'method'): dbus.String(u'manual', variant_level=1)}, signature=dbus.Signature('sv')), dbus.String(u'ipv6'): dbus.Dictionary({dbus.String(u'routes'): dbus.Array([], signature=dbus.Signature('(ayuayu)'), variant_level=1), dbus.String(u'addresses'): dbus.Array([], signature=dbus.Signature('(ayuay)'), variant_level=1), dbus.String(u'dns'): dbus.Array([], signature=dbus.Signature('ay'), variant_level=1), dbus.String(u'method'): dbus.String(u'auto', variant_level=1)}, signature=dbus.Signature('sv'))}, signature=dbus.Signature('sa{sv}'))
		pi('Setting ROUTER_NETWORK')
	else:
		settings = dbus.Dictionary({dbus.String(u'802-3-ethernet'): dbus.Dictionary({dbus.String(u'duplex'): dbus.String(u'full', variant_level=1), dbus.String(u's390-options'): dbus.Dictionary({}, signature=dbus.Signature('ss'), variant_level=1), dbus.String(u'mac-address'): dbus.Array([dbus.Byte(212), dbus.Byte(190), dbus.Byte(217), dbus.Byte(30), dbus.Byte(213), dbus.Byte(199)], signature=dbus.Signature('y'), variant_level=1)}, signature=dbus.Signature('sv')), dbus.String(u'connection'): dbus.Dictionary({dbus.String(u'timestamp'): dbus.UInt64(1403959433, variant_level=1), dbus.String(u'type'): dbus.String(u'802-3-ethernet', variant_level=1), dbus.String(u'id'): dbus.String(u'Wired Connection 1', variant_level=1), dbus.String(u'uuid'): dbus.String(u'2958a863-c599-4f01-81ff-d0b20ff0fae7', variant_level=1)}, signature=dbus.Signature('sv')), dbus.String(u'ipv4'): dbus.Dictionary({dbus.String(u'routes'): dbus.Array([], signature=dbus.Signature('au'), variant_level=1), dbus.String(u'addresses'): dbus.Array([], signature=dbus.Signature('au'), variant_level=1), dbus.String(u'dns'): dbus.Array([], signature=dbus.Signature('u'), variant_level=1), dbus.String(u'method'): dbus.String(u'auto', variant_level=1)}, signature=dbus.Signature('sv')), dbus.String(u'ipv6'): dbus.Dictionary({dbus.String(u'routes'): dbus.Array([], signature=dbus.Signature('(ayuayu)'), variant_level=1), dbus.String(u'addresses'): dbus.Array([], signature=dbus.Signature('(ayuay)'), variant_level=1), dbus.String(u'dns'): dbus.Array([], signature=dbus.Signature('ay'), variant_level=1), dbus.String(u'method'): dbus.String(u'auto', variant_level=1)}, signature=dbus.Signature('sv'))}, signature=dbus.Signature('sa{sv}'))
		pi('Setting DIRECT_NETWORK')
	proxyObject.Update(settings)
	return(True)
	
def restartNetwork():
	eth0uuid = '2958a863-c599-4f01-81ff-d0b20ff0fae7'
	nmcliCmd = ('nmcli', 'con', 'up', 'uuid', eth0uuid)
	runCmd(nmcliCmd, timeout=2)
	return(True)

def setRouterNetwork():
	pd('changing to router network')
	changeNetworkConfig(ROUTER_NETWORK)
	restartNetwork()

def setDirectNetwork():
	pd('changing to direct network')
	changeNetworkConfig(DIRECT_NETWORK)
	restartNetwork()

def main():
	if (len(sys.argv) < 2):
		usage()
		return(1)
	selectedNetwork = sys.argv[1]
	if (selectedNetwork == 'router'):
		setRouterNetwork()
	elif (selectedNetwork == 'direct'):
		setDirectNetwork()
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
