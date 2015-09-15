#!/usr/bin/env python
# -*- coding: utf-8 -*-

'html parse Python Events exercise'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import os

class PythonEventsHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.__pe = None
		self.__tag = ''
		self.__temp = ''

	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)
		print 'attrs', attrs
		if tag == 'h3':
			for attr in attrs:
				if attr[1] == 'event-title':
					self.__pe = PythonEvent()
					self.__tag = 'title'
					break;
		if tag == 'time':
			self.__tag = 'time'
		if tag == 'span':
			for attr in attrs:
				if attr[1] == 'event-location':
					self.__tag = 'location'
					break;

	def handle_endtag(self, tag):
		print('</%s>' % tag)
		if tag == 'li':
			python_events.append(self.__pe)

	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print('data: %s' % data)
#		print 'handle_data tag:', self.__tag
		if self.__tag == 'title':
			self.__pe.set_title(data)
			self.__tag = ''
		if self.__tag == 'time':
			if self.__temp == '':
				self.__temp = data
			else:
				self.__temp += '-'
				self.__temp += data
				self.__pe.set_time(self.__temp)
				self.__temp = ''
				self.__tag = ''
		if self.__tag == 'location':
			self.__pe.set_location(data)
			self.__tag = ''

	def handle_comment(self, data):
		print('<!-- -->')

	def handle_entityref(self, name):
		print 'handle_entityref:', name
		print ('&%s;' % name)

	def handle_charref(self, name):
		print 'handle_charref:', name
		print('&#%s;' % name)

class PythonEvent(object):
	def set_time(self, time):
#		print 'set_time:', time
		self.__time = time

	def set_title(self, title):
#		print 'set_title:', title
		self.__title = title

	def set_location(self, location):
#		print 'set_location:', location
		self.__location = location

	def get_event_info(self):
		return 'time: ' + self.__time + '	title: ' + self.__title + '\nlocation: ' + self.__location

python_events = []
def show_python_events(p_events):
	print '\nPython Events:'
	for pe in p_events:
		print '\n' + pe.get_event_info()

def decode(s):
	return s.replace('&ndash;', '-')

html = ''
with open(os.path.join('.', 'files', 'python_events_for_html_parser.txt'), 'r') as f:
	html = f.read()

parser = PythonEventsHTMLParser()
parser.feed(html)
show_python_events(python_events)



