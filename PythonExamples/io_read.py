#!/usr/bin/env python
# -*- coding: utf-8 -*-

'IO example'

__author__ = 'sunxiaoling'

def io_try():
	try:
		f = open('./files/test.txt')
		print f.read()
	finally:
		if f:
			f.close()

def io_with():
	with open('./files/test.txt') as f:
		print f.read()

def io_read_size():
	with open('./files/test.txt') as f:
		print f.read(5)

def io_readline():
	with open('./files/test.txt') as f:
		print f.readline()
		print f.readline()

def io_readlines():
	with open('./files/test.txt') as f:
		for line in f.readlines():
			print(line.strip())

def io_rb():
	with open('./files/img.jpg', 'rb') as f:
		print f.read(200)

def io_decode():
	with open('./files/gbk.txt', 'rb') as f:
		print f.read()
		#.decode('gbk')

def io_codecs():
	import codecs
	with codecs.open('./files/gbk.txt', 'r', 'gbk') as f:
		f.read()


if __name__ == '__main__':
#	io_try()
#	io_with()
#	io_read_size()
#	io_readline()
#	io_readlines()
#	io_rb()
#	io_decode()
	io_codecs()










