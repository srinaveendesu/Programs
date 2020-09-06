#!/usr/bin/python

import os
import sys
import time

import HTMLParser
class parserTemplate(HTMLParser.HTMLParser):
	def handle_charref(self, name):
		pd('=============: in handle_charref :=============')
		pv(name)

	def handle_comment(self, data):
		pd('=============: in handle_comment :=============')
		pv(data)

	def handle_decl(self, decl):
		pd('=============: in handle_decl :=============')
		pv(decl)

	def handle_pi(self, data):
		pd('=============: in handle_pi :=============')
		pv(data)

	def handle_startendtag(self, tag, attrs):
		pd('=============: in handle_startendtag :=============')
		pv(tag)
		pv(attrs)

	def handle_starttag(self, tag, attrs):
		pd('=============: in handle_starttag :=============')
		pv(tag)
		pv(attrs)

	def handle_data(self, data):
		pd('=============: in handle_data :=============')
		pv(data)

	def handle_entityref(self, name):
		pd('=============: in handle_entityref :=============')
		pv(name)

	def handle_endtag(self, tag):
		pd('=============: in handle_endtag :=============')
		pv(tag)

	def __init__(self, htmlFile):
		HTMLParser.HTMLParser.__init__(self)
		fd = open(htmlFile)
		data = fd.read()
		self.feed(data)
		self.close()

def main():
	htmlFile = sys.argv[1]
	parserTemplate(htmlFile)
	pi('Successfully Completed')
	return(0)

if (__name__ == '__main__'):
	ret = main()
	sys.exit(ret)
