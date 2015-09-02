#!/usr/bin/env python
# -*- coding: utf-8 -*-

'example for debug'

__author__ = 'sunxiaoling'

import logging
logging.basicConfig(level=logging.INFO)

# assert
def foo(s):
	n = int(s)
	assert n!=0, 'n is zero!'
	return 10 / n

def main():
	foo('0')
	
def test_logging():
	s = '0'
	n = int(s)
	logging.info('n = %d' % n)
	print 10 / n
	
if __name__ == '__main__':
#	main()
	test_logging()