#!/usr/bin/python
import os
import sys
import urllib

import os
import sys
import time

def getResult(ecode, htno):
	pv(ecode)
	pv(htno)
	#jntuLink = 'http://jntu.ac.in/results/results.php'
	jntuLink = 'http://jntu.ac.in/results/htno/%s/%s' %(htno, ecode)
	data = urllib.urlencode({'htno': htno, 'ecode': ecode})
	pv(jntuLink)
	pv(data)
	resultFound = False
	while (resultFound == False):
		pi('Trying for %s: ...', htno)
		socket = urllib.urlopen(jntuLink, data)
		out = socket.read()
		pv(out)
		if (out.find('HTNO :') != -1):
			outFile = '%s_%s.html' %(htno, ecode)
			fd = open(outFile, 'w')
			fd.write(out)
			fd.close()
			resultFound = True
	
def main():
	###############
	# for getting results of siri's all classmates
	#htnos = []
	#inValidHtno = [14, 15, 20, 41, 50, 53]
	#for i in range(1,60):
		#if ( not i in inValidHtno):
			#htnos.append('08m31a12%02d' %(i))
	#allData = {'1027': htnos}
	###############
	allData = {
		# use R07 result link
		# (siri, sai, rikvitha, sowmya, harish)
		#'1010': ['08m31a1230', '08k91a0339', '08m31a1207', '08m31a1242'], # 1-0 regular (may2009)
        #'1005': ['08m31a1230', '08k91a0339', '08m31a1207', '08m31a1242'], # 2-1 regular (nov2009)
        #'1012': ['08m31a1230', '08k91a0339', '08m31a1207', '08m31a1242'], # 2-2 regular (may2010)
        #'1019': ['08m31a1230', '08k91a0339', '08m31a1207', '08m31a1242'], # 3-1 regular (nov2010)
        #'1027': ['08m31a1230', '08k91a0339', '08m31a1207', '08m31a1242'], # 3-2 regular (may2011)
        #'VjMANVBnVWc': ['08m31a1230', '08k91a0339', '08m31a1207', '08m31a1242', '09k95a0502'], # 4-1 regular (may2011)
		# use R09 result link
		# (bharath, srikanth)
		#'1021': ['10h65a0501', '10n85a0301'], # 2-1 regular (nov2010)
		#'1031': ['10h65a0501', '10n85a0301'], # 2-1 supply (may2011)
		#'1029': ['10h65a0501', '10n85a0301'], # 2-2 regular (may2011)
	}
	for ecode in allData.keys():
		for htno in allData[ecode]:
			getResult(ecode, htno)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
