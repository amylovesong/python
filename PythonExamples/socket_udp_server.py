#!/usr/bin/env python
# -*- coding:utf-8 -*-

'UDP socket exercise: server'

__author__ = 'sunxiaoling'

import socket

# SOCK_DGRAM指定socket的类型是UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))
print 'Bind UDP on 9999...'
while True:
	data, addr = s.recvfrom(1024)
	print 'Received from %s:%s.' % addr
	s.sendto('Hello, %s!' % data, addr)