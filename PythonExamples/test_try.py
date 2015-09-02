#!/usr/bin/env python
# -*- coding: utf-8 -*-

'error/exception example'

__author__ ='sunxiaoling'

import logging

def test_zerodivision():
	try:
		print 'try...'
#		r = 10 / int('a')
		r = 10 / 2
		print 'result:', r
	except ValueError, e:
		print 'ValueError:', e
	except ZeroDivisionError, e:
		print 'ZeroDivisionError:', e
	else:
		print 'no error!'
	finally:
		print 'finally...'
	print 'END'
	
def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2
	
def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)
#		print 'Error!'
#	finally:
#		print 'finally...'

class FooError(StandardError):
	pass
	
def foo_error_test(s):
	n = int(s)
	if n==0:
		raise FooError('invalid value: %s' % s)
	return 10 / n
	
def convert_error_test():
	try:
		10 / 0
	except ZeroDivisionError, e:
		raise ValueError('input error!')
	
if __name__ == '__main__':
#	test_zerodivision()
#	main()
#	print 'END'
#	foo_error_test(0)
	convert_error_test()
