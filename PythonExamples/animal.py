#!/usr/bin/env python
# -*- coding: utf-8 -*-

'inherit'

class Animal(object):
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
	def run(self):
		print 'Dog is running...'

	def eat(self):
		print 'Eating meat...'

class Cat(Animal):
	def  run(self):
		print 'Cat is running...'

def run_twice(animal):
	animal.run()
	animal.run()

class Tortoise(Animal):
	def run(self):
		print 'Tortoise is running slowly...'

def test():
#	dog = Dog()
#	dog.run()

#	cat = Cat()
#	cat.run()

#	run_twice(Animal())
#	run_twice(Cat())
	run_twice(Tortoise())

if __name__ == '__main__':
	test()