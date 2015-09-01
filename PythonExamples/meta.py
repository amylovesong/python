#!/usr/bin/env python
# -*- coding: utf-8 -*-

'metaclass example'

__author__ = 'sunxiaoling'

class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class MyList(list):
	__metaclass__ = ListMetaclass