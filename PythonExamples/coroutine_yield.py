#!/usr/bin/env python
# -*- coding: utf-8 -*-

'Coroutine exercise: yield'

__author__ = 'sunxiaoling'

import time

def consumer():
	r = ''
	while True:
		n = yield r
#		print n
		if not n:
			return
		print('[CONSUMER] Consuming %s...' % n)
		time.sleep(1)
		r = '200 OK'

def produce(c):
#	c.next()
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('[PRODUCER] Producing %s...' % n)
		r = c.send(n)
#		r = c.next()
		print('[PRODUCER] Consumer return: %s' % r)
	c.close()
	
if __name__ == '__main__':
	c = consumer()
	produce(c)