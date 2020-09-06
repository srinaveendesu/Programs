#!/usr/bin/python3
import ctypes

import os
import sys
import time

cFileCode = \
r'''
#include <stdio.h>

struct structureName {
	int interger;
	char character;
	float floatValue;
};

int changeStructureValues(struct structureName *s)
{
	s->interger = 10;
	s->character = 'm';
	s->floatValue = 11.11;
	printf('Successfully executed: changeStructureValues()\n');
}
'''
def compileCfile(cFileName):
	# write c file
	fd = open('%s.c' %(cFileName), 'w')
	fd.write(cFileCode)
	fd.close()
	# compile this c file as a shared lib using
	ret = runCmd('gcc -fPIC -c %s.c' %(cFileName))
	if (ret != 0):
		return(False)
	ret = runCmd('gcc -shared %s.o -o lib%s.so' %(cFileName, cFileName))
	if (ret != 0):
		return(False)
	os.environ['LD_LIBRARY_PATH'] = os.getcwd()

def clean(cFileName):
	os.unlink('%s.c' %(cFileName))
	os.unlink('%s.o' %(cFileName))
	os.unlink('lib%s.so' %(cFileName))
	return(True)

class structureName(ctypes.Structure):
	_fields_ = [('interger', ctypes.c_int),
				('character', ctypes.c_char),
				('floatValue', ctypes.c_float)]

def main():
	# compile c file
	cFileName = 'cfile'
	ret = compileCfile(cFileName)
	if (ret == False):
		return(1)
	# calling c function
	libc = ctypes.CDLL('./libcfile.so')
	s = structureName(5, b's', 5.5)
	print('before calling: s')
	pv(s.interger)
	pv(s.character)
	pv(s.floatValue)
	setTtyColor('YELLOW')
	total = libc.changeStructureValues(ctypes.byref(s))
	setTtyColor('NORMAL')
	print('after calling: s')
	pv(s.interger)
	pv(s.character)
	pv(s.floatValue)
	pv(total)
	# clean the files
	clean(cFileName)
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)

