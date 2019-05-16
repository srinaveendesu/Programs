#!/usr/bin/python3
import os
import sys
import time
import csv
from scapy.all import *

resultFile = 'out.csv'

def usage():
	print('Usage: %s <pcap>' %(sys.argv[0]))

def main():
	if (len(sys.argv) < 2):
		usage()
		return(False)
	pcapFile = sys.argv[1]
	fd = open(resultFile, 'w')
	csvFd = csv.writer(fd)
	header = ['COUNT']
	header.extend(['ETHER-DMAC', 'ETHER-SMAC', 'ETHER-TYPE'])
	header.extend(['IP-VERSION', 'IP-IHL', 'IP-TOS', 'IP-LEN', 'IP-ID', 'IP-FLAGS', 'IP-FRAG', 'IP-TTL', 'IP-PROTO', 'IP-CHKSUM', 'IP-SRC', 'IP-DST'])
	header.extend(['TCP-SPORT', 'TCP-DPORT', 'TCP-SEQ', 'TCP-ACK', 'TCP-DATAOFS', 'TCP-RESERVED', 'TCP-FLAGS', 'TCP-WINDOW', 'TCP-CHKSUM', 'TCP-URGPTR', 'TCP-OPTIONS'])
	header.extend(['UDP-SPORT', 'UDP-DPORT', 'UDP-LEN', 'UDP-CHKSUM'])
	header.extend(['ICMP-TYPE', 'ICMP-CODE', 'ICMP-CHKSUM', 'ICMP-UNUSED'])
	header.extend(['PAYLOAD', 'IP-PAYLOAD'])
	csvFd.writerow(header)
	packets = rdpcap(pcapFile)
	for (index, p) in enumerate(packets):
		print('==========: packet [%d] :=============' %(index))
		print(p.show())
		row = [index]
		if (Ether in p):
			row.extend([p.dst, p.src, p.type])
		else:
			row.extend(['', '', ''])
		if (IP in p):
			row.extend([p[IP].version, p[IP].ihl, p[IP].tos, p[IP].len, p[IP].id, p[IP].flags, p[IP].frag, p[IP].ttl, p[IP].proto, p[IP].chksum, p[IP].src, p[IP].dst])
			ipPayloadLen = len(p[type(p[IP].payload)].payload)
		else:
			row.extend(['', '', '', '', '', '', '', '', '', '', '', ''])
			ipPayloadLen = 0
		if (TCP in p):
			row.extend([p[TCP].sport, p[TCP].dport, p[TCP].seq, p[TCP].ack, p[TCP].dataofs, p[TCP].reserved, p[TCP].flags, p[TCP].window, p[TCP].chksum, p[TCP].urgptr, p[TCP].options])
		else:
			row.extend(['', '', '', '', '', '', '', '', '', '', ''])
		if (UDP in p):
			row.extend([p[UDP].sport, p[UDP].dport, p[UDP].len, p[UDP].chksum])
		else:
			row.extend(['', '', '', ''])
		if (ICMP in p):
			row.extend([p[ICMP].type, p[ICMP].code, p[ICMP].chksum, p[ICMP].unused])
		else:
			row.extend(['', '', '', ''])
		row.extend([len(p.payload), ipPayloadLen])
		csvFd.writerow(row)
	fd.close()
	return(True)

if (__name__ == '__main__'):
	ret = main()
	sys.exit((1, 0)[ret])
