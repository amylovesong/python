#!/usr/bin/env python
# -*- coding: utf-8 -*-

'html parse Python Events exercise'

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import os

class PythonEventsHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print('<%s>' % tag)
		print 'attrs', attrs
		if tag == 'h3' and attrs[0]['class'] == 'event-title':
			print 'event title'

	def handle_endtag(self, tag):
		print('</%s>' % tag)

	def handle_startendtag(self, tag, attrs):
		print('<%s/>' % tag)

	def handle_data(self, data):
		print('data: %s' % data)

	def handle_comment(self, data):
		print('<!-- -->')

	def handle_entityref(self, name):
		print ('&%s;' % name)

	def handle_charref(self, name):
		print('&#%s;' % name)

class PythonEvent(object):
	def set_time(self, time):
		self.__time = time

	def set_title(self, title):
		self.__title = title

	def set_location(self, location):
		self.__location = location

	def get_event_info(self):
		return 'time:' + self.__time + '\ntitle:' 
		+ self.__title + '\nlocation:' + self.__location

python_events = []

html = ''
with open(os.path.join('.', 'files', 'python_events_for_html_parser.txt'), 'r') as f:
	html = f.read()

parser = PythonEventsHTMLParser()
parser.feed(html)


