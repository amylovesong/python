#!/usr/bin/env python
# -*- coding:utf-8 -*-

'WSGI exercise'

__author__ = 'sunxiaoling'

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
#	print environ['PATH_INFO']
	return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')