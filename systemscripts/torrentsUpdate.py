#!/usr/bin/python3
import urllib.request
import bs4
import re

import os
import sys
import time


def getNewTorrentList(url, lastTorrent):
	pv(url)
	req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	response = urllib.request.urlopen(req)
	urlData = response.read().decode()
	pv(urlData)
	response.close()
	#urlData = open('torrentz.html', 'r').read()
	torrentList = []
	soup = bs4.BeautifulSoup(urlData, 'lxml')
	parseError = False
	for dl in soup.findAll('dl'):
		if (dl == None) or (dl.dt == None) or (dl.dd == None):
			continue
		name = dl.dt.text.strip()
		pv(name)
		if (name == lastTorrent):
			pd('Found last torrent: %s', lastTorrent)
			break
		spanList = dl.dd.findAll('span')
		pv(spanList)
		sizeTag = seedersTag = leechersTag = None
		if (len(spanList) > 1):
			(sizeTag, seedersTag, leechersTag) = spanList[2:5]
		#sizeTag = dl.dd.find('span', attrs={'class':'s'})
		#seedersTag = dl.dd.find('span', attrs={'class':'u'})
		#leechersTag = dl.dd.find('span', attrs={'class':'d'})
		if (None in [sizeTag, seedersTag, leechersTag]):
			pw('size/seeders/leechers: value is None')
			parseError = True
			continue
		size = sizeTag.text.strip()
		seeders = seedersTag.text.strip()
		leechers = leechersTag.text.strip()
		#pv((name, size, seeders, leechers))
		torrentList.append((name, size, seeders, leechers))
	if (parseError == True) and (len(torrentList) == 0):
		errorFile = os.path.join('/', 'tmp', 'error.html')
		pe('Error in parsing, Dump the html to: %s', errorFile)
		fd = open(errorFile, 'w')
		fd.write(soup.prettify())
		fd.close()
		sys.exit(0)
	return(torrentList)

def filterTorrentList(torrentList):
	videoTorrentsList = []
	audioTorrentsList = []
	qualityExpr = 'web|bd|bluray|hd|tv|dvd'
	unqualityExpr = 'pdvd|cam|scr| ts '
	mp3Expr = 'kbps'
	for (name, size, seeders, leechers) in torrentList:
		if (re.search(unqualityExpr, name, flags=re.IGNORECASE) == None):
			if (re.search(mp3Expr, name, flags=re.IGNORECASE) != None):
				audioTorrentsList.append((name, size, seeders, leechers))
			else:
				videoTorrentsList.append((name, size, seeders, leechers))
	return(videoTorrentsList, audioTorrentsList)
		
def printTorrentList(torrentList):
	for (name, size, seeders, leechers) in torrentList:
		writeLog('%s ' %(name)) #, color='CYAN')
		writeLog('%s ' %(size), color='MAGENTA')
		writeLog('%s ' %(seeders), color='GREEN')
		writeLog('%s\n' %(leechers), color='BLUE')

def main():
	tmpFile = os.path.join(ALPT, 'torrentsUpdateData.tmp')
	tmpData = readDataFile(tmpFile)
	if (tmpData == False):
		tmpData = getNewDataModule()
		tmpData.searchDict = {}
	searchDict = tmpData.searchDict
	searchStrList = ['telugu', 'hindi']
	pageDepth = 1
	for searchStr in searchStrList:
		lastTorrent = searchDict.get(searchStr, '')
		pv(lastTorrent)
		torrentList = []
		for pageCount in range(pageDepth):
			url = 'https://torrentz2.eu/searchA?f=%s&p=%d' %(searchStr, pageCount)
			torrentList += getNewTorrentList(url, lastTorrent)
		(videoTorrentsList, audioTorrentsList) = filterTorrentList(torrentList)
		writeLog('=========: %s:video :==========\n' %(searchStr), color='CYAN')
		printTorrentList(videoTorrentsList)
		writeLog('=========: %s:audio :==========\n' %(searchStr), color='CYAN')
		printTorrentList(audioTorrentsList)
		sys.stdout.flush()
		if (len(torrentList) > 0):
			searchDict[searchStr] = torrentList[0][0]
	writeDataFile(tmpFile, tmpData)
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
