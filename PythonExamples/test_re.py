#!usr/bin/env python
# -*- coding: utf-8 -*-

'pickling and unpickling'

__author__ = 'sunxiaoling'

import re

# -- match examples

#print re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
#print re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

# -- split examples

#print 'a b   c'.split(' ')
#print re.split(r'\s+', 'a b   c')
#print re.split(r'[\s\,]+', 'a,b, c  d')
#print re.split(r'[\s\,\;]+', 'a,b;; c  d')

# -- group examples

m = re.match(r'^(\d{3})-(\d{3,8})', '010-12345')
#print m
#print m.group(0) # 原始字符串
#print m.group(1) # 第1个子串
#print m.group(2) # 第2个子串

r = r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$'
#t = '19:05:30'
t = '23:00:01'
m = re.match(r, t)
#print m.groups()

r = '^(0[0-9]|1[0-2]|[0-9])-(0[0-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
d = '1-22'
d = '2-30' # illegal date, and the regular can't recognize
m = re.match(r, d)
#print m
#print m.groups()

# -- 贪婪匹配
#print re.match(r'^(\d+)(0*)$', '102300').groups()
#print re.match(r'^(\d+?)(0*)$', '102300').groups()

# -- pre-compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').groups()
print re_telephone.match('010-8086').groups()

# -- exercise
re_email = re.compile(r'^$')
