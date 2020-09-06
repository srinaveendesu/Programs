#!/usr/bin/python

import os
import sys
import time

confStr = '''\
Dir::Etc::Main '%s/conf';
Dir::Etc::Parts '%s/conf';
APT::Architecture 'amd64';
Dir::Etc::SourceList '%s/sources_list_laptop';
Dir::Etc::SourceParts '%s/sources_list_laptop';
Dir::Etc::Preferences '%s/preferences';
Dir::Etc::PreferencesParts '%s/preferences.d';
Dir::Cache::Archives '%s/amd64_archives';
APT::Archives::MaxAge '0';
APT::Archives::MinAge '0';
APT::Archives::MaxSize '0';
Dir::State::Lists '%s/amd64_lists';
Dir::State::status '%s/status_laptop_amd64';
APT::Clean-Installed 'off';
APT::Get::Assume-Yes 'true';
APT::Get::Fix-Broken 'true';
APT::Get::Download-Only 'true';
APT::Get::ReInstall 'true';
'''

sourceList = '''\
deb http://id.archive.ubuntu.com/ubuntu/ precise main restricted universe multiverse
deb-src http://id.archive.ubuntu.com/ubuntu/ precise multiverse

deb http://packages.medibuntu.org/ precise free non-free
deb-src http://packages.medibuntu.org/ precise free non-free

deb http://archive.canonical.com/ precise partner
deb-src http://archive.canonical.com/ precise partner

deb http://ppa.launchpad.net/ferramroberto/gnome3/ubuntu precise main
deb-src http://ppa.launchpad.net/ferramroberto/gnome3/ubuntu precise main

deb http://ppa.launchpad.net/ferramroberto/java/ubuntu oneiric main
deb-src http://ppa.launchpad.net/ferramroberto/java/ubuntu oneiric main

deb http://ppa.launchpad.net/gnome3-team/gnome3/ubuntu precise main
deb-src http://ppa.launchpad.net/gnome3-team/gnome3/ubuntu precise main

deb http://ppa.launchpad.net/noobslab/gnome/ubuntu precise main
deb-src http://ppa.launchpad.net/noobslab/gnome/ubuntu precise main

deb http://ppa.launchpad.net/ricotz/testing/ubuntu precise main
deb-src http://ppa.launchpad.net/ricotz/testing/ubuntu precise main

deb http://ppa.launchpad.net/webupd8team/gnome3/ubuntu precise main
deb-src http://ppa.launchpad.net/webupd8team/gnome3/ubuntu precise main

deb http://download.virtualbox.org/virtualbox/debian precise contrib
'''

def runSysCmd(cmd):
	pi('Running cmd: %s', cmd)
	ret = os.system(cmd)
	return ret

def main():
	pwd = os.getcwd()
	# create neccessary files and folders
	try:
		os.makedirs('amd64_archives/partial')
		os.makedirs('./amd64_lists/partial')
		fd = open('preferences', 'w')
		fd.close()
		os.mkdir('preferences.d')
	except Exception as e:
		pv(e)
		sys.exit(0)
	# writing source list file
	fd = open('sources_list_laptop', 'w')
	fd.write(sourceList)
	fd.close()
	# writing dpkg status file
	fd = open('status_laptop_amd64', 'w')
	fd.close()
	# writing apt conf file
	fd = open('conf', 'w')
	fd.write(confStr %(pwd, pwd, pwd, pwd, pwd, pwd, pwd, pwd, pwd))
	fd.close()
	pi('Setup succussfully completed')
	runSysCmd('apt-get -c=conf update')
	runSysCmd('apt-get -c=conf --yes -q --allow-unauthenticated install medibuntu-keyring')
	runSysCmd('apt-get -c=conf update')
	
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
