#!/usr/bin/env python
# -*- coding: utf-8 -*-

'custom class using special method'

__author__ = 'sunxiaoling'

#__str__
#__getattr__
#__call__
class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' % self.name

	__repr__ = __str__

	def __getattr__(self, attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda:25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
	def __call__(self):
		print('My name is %s.' % self.name)

class Chain(object):
	def __init__(self, path=''):
		self.__path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self.__path, path))

	def __str__(self):
		return self.__path

	def __call__(self, name):
		return Chain('%s/:%s' % (self.__path, name))

#__iter__
#__getitem__
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1 #初始化两个计数器

	def __iter__(self):
		return self #迭代对象是实例本身

	def next(self):
		self.a, self.b = self.b, self.a + self.b #计算下一个值
		if self.a > 100000: #退出循环的条件
			raise StopIteration();
		return self.a

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L
