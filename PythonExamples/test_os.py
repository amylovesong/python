#!/usr/bin/env python
# -*- coding:utf-8 -*-

'os example'

__author__ = 'sunxiaoling'

import os
#print os.name
#print os.uname() #Windows不提供。os模块的某些函数跟操作系统相关

#print os.environ
#print os.getenv('PATH')

#print os.path.abspath('.') #查看当前目录的绝对路径

newdir = os.path.join(os.path.abspath('.'), 'testdir')
#print 'newdir is:\n%s' % newdir
#os.mkdir(newdir)
#os.rmdir(newdir)

newfile = os.path.join(newdir, 'file.txt')
#print os.path.split(newfile)
#print os.path.splitext(newfile)

#os.rename('test.txt', 'test.py')
#os.remove('test.py')

import shutil
#shutil.copyfile('test.txt', 'test_copy.txt')

#print [x for x in os.listdir('.') if os.path.isdir(x)]
#print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

def search(s):
	print 'search for "%s"' % s
	listdir('.', s)

def listdir(path, s):
#	print 'listdir path: %s' % path
	import pdb
	for x in os.listdir(path):
#		print '----before join:%s' % x
		if path !='.':
			x = os.path.join(path, x)
#		print '----after  join:%s' % x
		if os.path.isfile(x):
#			print '--file:"%s"' % x
			if s in x:
				print x
#				print '========%s is a match' % x
		elif os.path.isdir(x):
#			print '--dir:"%s"' % x
			listdir(x, s)
		else:
			print '%s is file?%s' % (x, os.path.isfile(x))
			print '%s is dir?%s' % (x, os.path.isdir(x))
		
if __name__=='__main__':
#	search('test')
	search('py')
#	search('h')
#	search('_')