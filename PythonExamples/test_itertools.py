#!/usr/bin/env python
# -*- coding: utf-8 -*-

'inner module: itertools'

__author__ = 'sunxiaoling'

import itertools

def e_count():
    naturals = itertools.count(1)
    for n in naturals:
        print n
#        if n==50:
#            break;

def e_cycle():
    cs = itertools.cycle('ABC')# 重复序列
    for c in cs:
        print c

def e_repeat():
    ns = itertools.repeat('A', 10)# 第二个参数限定重复次数
    for n in ns:
        print n

def e_takewhile():
    naturals = itertools.count(1)
    ns = itertools.takewhile(lambda x: x <= 10, naturals)
    for n in ns:
        print n

def e_chain():
    for c in itertools.chain('ABC', 'XYZ'):
        print c

def e_groupby():
    for key, group in itertools.groupby('AAABBBCCAAA'):
        print key, list(group)
#        print key, group

def e_groupby_case_insensitive():
    for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
        print key, list(group)

def e_imap():
    for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
        print x

def e_compare_imap_map():
    r = map(lambda x: x * x, [1, 2, 3])
    print r
    r = itertools.imap(lambda x: x * x, [1, 2, 3])
    print r
    for x in r:
        print x

#---“惰性计算”
    print ''
    r = itertools.imap(lambda x: x * x, itertools.count(1))
    for n in itertools.takewhile(lambda x: x < 100, r):
        print n

#----MemoryError
#    print '\n'
#    r = map(lambda x: x * x, itertools.count(1))
#    for n in itertools.takewhile(lambda x: x < 100, r):
#        print n

def e_compare_ifilter_filter():
    def is_odd(n):# 奇数
        return n % 2 == 1

    f = filter(is_odd, [1, 2, 3, 4, 5, 6])
    print f
    f = itertools.ifilter(is_odd, [1, 2, 3, 4, 5, 6])
    print f
    for x in f:
        print x

#---“惰性计算”
    print ''
    f = itertools.ifilter(is_odd, itertools.count(1))
    for n in itertools.takewhile(lambda x: x < 30, f):
        print n

#---MemoryError
#    print ''
#    f = filter(is_odd, itertools.count(1))
#    for x in itertools.takewhile(lambda x: x < 30, f):
#        print x

if __name__ == '__main__':
#    e_count()
#    e_cycle()
#    e_repeat()
#    e_takewhile()
#    e_chain()
#    e_groupby()
#    e_groupby_case_insensitive()
#    e_imap()
#    e_compare_imap_map()
    e_compare_ifilter_filter()
