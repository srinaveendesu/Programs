#!/usr/bin/python
import urllib

import os
import sys
import time

'''
other commands:

indirect way to contact way2sms site:
curl -d 'uid=99&pwd=mm&provider=WAY2SMS&phone=9989225538&msg=hello world' 'http://www.webfrnd.com/smsNew.php'
'''

def sendRequest(phone, msg):
	(username, password) = getPass('way2sms')
	pd('Sending sms to: %s', phone)
	pd('Msg:\n%s', msg)
	#url = 'http://www.webfrnd.com/smsNew.php'
	#url = 'http://mixmasala.orgfree.com/smslite.php'
	url = 'http://smsapi.ueuo.com/smslite.php'
	data = urllib.urlencode({'uid': username, \
							'pwd': password, \
							'provider': 'WAY2SMS', \
							'phone': phone, \
							'msg': msg})
	pi('Sending sms...')
	socket = urllib.urlopen(url, data)
	out = socket.read()
	pv(out)
	if (out.find('Logging in... Sending SMS ... Message Sent... Logging Out...') == -1):
		pe('Sms sending faliled')
	else:
		pi('Successfully Sent to: %s', phone)
		
'''
directly to way2sms site:
curl -c madhu.cookie -d 'username=99999999&password=mmmmm' 'http://site7.way2sms.com/auth.cl'
curl -b madhu.cookie 'http://site7.way2sms.com/jsp/Main.jsp'
'''
def way2smsRequest(phone, msg):
	pass

def usage():
	pi('Usage: %s <phone;phone;phone;...> [<msg>]', sys.argv[0])

def msgSplit(msg):
	maxStringLength = 140
	strlen = len(msg)
	msgs = []
	if (strlen <= maxStringLength):
		msgs.append(msg)
		return msgs
	i = 0
	while (i < strlen):
		if (i+maxStringLength < strlen) and (msg[i+maxStringLength] != ' '):
			# find first space just before the slice point
			#+ this is to terminate the string exactly at the word end.
			j = i + maxStringLength - 1
			while (j > i):
				if (msg[j] == ' '):
					break
				j -= 1
			msgs.append(msg[i:j])
			i = j
		else:
			msgs.append(msg[i:i+maxStringLength])
			i += maxStringLength
	return msgs

def getMobileNos(names, contactStatusFile):
	names = names.split(';')
	phones = []
	(controlInfo, [nameContact, numberContact]) = readStatusFile(contactStatusFile)
	for name in names:
		try:
			index = nameContact.index(name)
			phones.append(numberContact[index])
		except:
			if (name.isdigit()):
				phones.append(name)
			else:
				pe('contact not found: %s', name)
	phones = ';'.join(phones)
	pv(phones)
	return(phones)	

def syncMobileContacts(contactStatusFile):
	mobileRawContactsFile = os.path.join(HOME, 'workspace',
			'madhusudhan', 'mobileContent/contacts/contacts')
	mobileRawContactsFileFd = open(mobileRawContactsFile, 'r')
	name = []
	number = []
	for contact in mobileRawContactsFileFd:
		t = contact.split(';')
		name.append(formatString(t[0]))
		number.append(t[1])
		pd('%s: %s', name[-1], number[-1])
	writeStatusFile(contactStatusFile, [name, number])
	return(0)

def main():
	if (len(sys.argv) < 2):
		usage()
		sys.exit(0)
	option = sys.argv[1]
	contactStatusFile = os.path.join(ALPT, 'smsSend_contacts')	
	if (option == '-s'):
		syncMobileContacts(contactStatusFile)
		return(0)
	phone = getMobileNos(option, contactStatusFile)
	try:
		msg = sys.argv[2]
	except:
		print 'write your msg: '
		msg = sys.stdin.read()
	# calulate msg limit as 140 char
	msgs = msgSplit(msg)
	# send msgs
	for msg in msgs:
		sendRequest(phone, msg)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)

