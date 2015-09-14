#!/usr/bin/env python
# -*- coding:utf-8 -*-

'xml parse for yahoo weather exercise'

__author__ = 'sunxiaoling'

from xml.parsers.expat import ParserCreate
import os

class Weather(object):
	def __init__(self):
		self.__condition = []
		self.__forecasts = []
		
	def set_temp_unit(self, temp_unit):
		self.__temp_unit = temp_unit
		
	def get_temp_unit(self):
		return self.__temp_unit
		
	def set_condition(self, condition):
		self.__condition = condition
		
	def add_forecast(self, day, forecast):
		self.__forecasts.append((day, forecast))
		
	def get_condition_text(self):
		return self.__condition['text']
		
	def get_condition_temp(self):
		return self.__condition['temp']
		
	def get_condition_date(self):
		return self.__condition['date']

	def get_forecast(self, day):
		for f in self.__forecasts:
			if day == f[0]:
				forecast = f[1]
				return '----day:' + forecast['day'] + '\n----date:' + forecast['date'] + '\n----temp: ' + forecast['low'] + '--' + forecast['high'] + self.get_temp_unit() + '\n' + '----' + forecast['text']
		
	def get_forecasts(self):
		return self.__forecasts

class WeatherSaxHandler(object):
	def start_element(self, name, attrs):
		print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
		if name == 'yweather:condition':
			weather.set_condition(attrs)
		if name == 'yweather:forecast':
			weather.add_forecast(attrs['day'], attrs)
		if name == 'yweather:units':
			weather.set_temp_unit(attrs['temperature'])
	
	def end_element(self, name):
		print('sax:end_element: %s' % name)
		
	def char_data(self, text):
		print('sax:char_data: %s' % text)

def show_weather(wea):
	print '\n--Today:\n----date:%s' % wea.get_condition_date()
	print '----temp:%s%s' % (wea.get_condition_temp(), wea.get_temp_unit())
	print '----%s' % wea.get_condition_text()
	print '\n--Tomorrow:\n%s\n' % wea.get_forecast('Tue')
	print '--Forecast:\n%s' % wea.get_forecast('Wed')
	print '\n%s' % wea.get_forecast('Thu')
	print '\n%s' % wea.get_forecast('Fri')

xml = ''
with open(os.path.join('.', 'files', 'forecastrss.xml'), 'r') as f:
	xml = f.read()
#	print 'xml:\n%s' % xml

weather = Weather()

handler = WeatherSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
show_weather(weather)