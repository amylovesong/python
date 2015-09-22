#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Database operation module.
'''

import time, uuid, functools, threading, logging

# Dict object:

class Dict(dict):
	'''
	Simple dict but support access as x.y style.
	TODO: doctest here
	'''
	
	def __init__(self, names=(), values=(), **kw):
		super(Dict, self).__init__(**kw)
		for k, v in zip(names, values):
			self[k] = v
	
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	
	def __setattr__(self, key, value):
		self[key] = value

class _Engine(object):
	def __init__(self, connect):
		self._connect = connect
	def connect(self):
		return self._connect()
		
engine = None

class _DbCtx(threading.local):
	def __init__(self):
		self.connection = None
		self.transactions = 0
	
	def is_init(self):
		return not self.connection is None
	
	def init(self):
		self.connection = _LasyConnection()
		self.transactions = 0
		
	def cleanup(self):
		self.connection.cleanup()
		self.connection = None
		
	def cursor(self):
		return self.connection.cursor()
		
_db_ctx = _DbCtx()

class _ConnectionCtx(object):
	def __enter__(self):
		global _db_ctx
		self.should_cleanup = False
		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_cleanup = True
		return self
		
	def __exit__(self, exctype, excvalue, traceback):
		global _db_ctx
		if self.shoud_cleanup:
			_db_ctx.cleanup()
			
def connection():
	return _ConnectionCtx()
	
class _TransactionCtx(object):
	def __enter__(self):
		global _db_ctx
		self.should_close_conn = False
		if not _db_ctx.is_init():
			_db_ctx.init()
			self.should_close_conn = True
		_db_ctx.transactions = _db_ctx.transactions + 1
		return self
		
	def __exit__(self, exctype, excvalue, traceback):
		global _db_ctx
		_db_ctx.transactions = _db_ctx.transactions - 1
		try:
			if _db_ctx.transactions == 0:
				if exctype is None:
					self.commit()
				else:
					self.rollback()
		finally:
			if self.should_close_conn:
				_db_ctx.cleanup()

	def commit(self):
		global _db_ctx
		try:
			_db_ctx.connection.commit()
		except:
			_db_ctx.connection.rollback()
			raise
			
	def rollback(self):
		global _db_ctx
		_db_ctx.connection.rollback()







