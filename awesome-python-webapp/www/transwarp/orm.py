#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'sunxiaoling'

'''
Database operation module. This module is independent with web module.
'''

import time, logging

import db

class Field(object):

	_count = 0

	def __init__(self, **kw):
		self.name = kw.get('name', None)
		self._default = kw.get('default', None)
		self.primary_key = kw.get('primary_key', False)
		self.nullable = kw.get('nullable', False)
		self.updatable = kw.get('updatable', True)
		self.insertable = kw.get('insertable', True)
		self.ddl = kw.get('ddl', '')
		self._order = Field._count
		Field._count = Field._count + 1

	@property
	def default(self):
		d = self._default
		return d() if callable(d) else d

	def __str__(self):
		s = ['<%s:%s, %s, default(%s),' % (self.__class__.__name__, self.name, self.ddl, self._default)]
		# TODO

class Model(dict):
	__metaclass__ = ModelMetaclass

	def __init__(self, **kw):
		super(Model, self).__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

	@classmethod
	def get(cls, pk):
		d = db.select_one('select * from %s where %s=?' % (cls.__table__, cls.__primary_key__.name), pk)
		return cls(**d) if d else None

	def insert(self):
		params = []
		for k, v in self.__mapping__.iteritems():
			params[v.name] = getattr(self, k)
		db.insert(self.__table__, **params)
		return self

class ModelMetaclass(type):
	def __new__(cls, name, bases, attrs):
		mapping = ... # 读取cls的Field字段
		primary_key = ... # 查找primary_key字段
		__table__ = cls.__table__ # 读取cls的__table__字段
		# 给cls增加一些字段:
		attrs['__mapping__'] = mapping
		attrs['__primary_key__'] = primary_key
		attrs['__table__'] = __table__
		return type.__new__(cls, name, bases, attrs)