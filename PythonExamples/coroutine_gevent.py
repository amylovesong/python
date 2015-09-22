#!/usr/bin/env python
# -*- coding:utf-8 -*-

'Coroutine exercise: gevent'

__author__ = 'sunxiaoling'

def e_gevent():
	from gevent import monkey; monkey.patch_socket()
	import gevent

	def f(n):
		for i in range(n):
			print gevent.getcurrent(), i
			gevent.sleep(0)

	g1 = gevent.spawn(f, 5)
	g2 = gevent.spawn(f, 5)
	g3 = gevent.spawn(f, 5)
	g1.join()
	g2.join()
	g3.join()

def e_gevent_example():
	from gevent import monkey; monkey.patch_all()
	import gevent
	import urllib2

	def f(url):
		print('GET: %s' % url)
		resp = urllib2.urlopen(url)
		data = resp.read()
		print('%s bytes received from %s.' % (len(data), url))

	gevent.joinall([
		gevent.spawn(f, 'http://www.python.org/'),
		gevent.spawn(f, 'https://www.yahoo.com/'),
		gevent.spawn(f, 'https://github.com/'),
	])

if __name__ == '__main__':
#	e_gevent()
	e_gevent_example()