#!/usr/bin/env python
# -*- coding: utf-8 -*-

'IO example'

__author__ = 'sunxiaoling'

def io_write():
	with open('./files/test_write.txt', 'w') as f:# or 'wb'
		f.write('Hello, amy!')

def read():
	with open('./files/test_write.txt', 'r') as f:
		print f.read()

if __name__ == '__main__':
	io_write()
	read()