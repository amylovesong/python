#!/usr/bin/env python
# -*- coding: utf-8 -*-

'multi inherit example'

__author__ = 'sunxiaoling'

class Animal(object):
	pass

#大类：
class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class RunnableMixin(object):
	def run(self):
		print('Running...')

class FlyableMixin(object):
	def fly(self):
		print('Flying...')

#各种动物：
class Dog(Mammal, RunnableMixin):
	pass

class Bat(Mammal, FlyableMixin):
	pass

class Parrot(Bird, FlyableMixin):
	pass

class Ostrich(Bird, RunnableMixin):
	pass


		