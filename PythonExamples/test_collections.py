#!/usr/bin/env python
# -*- coding: utf-8 -*-

'inner module: collections'

__author__ = 'sunxiaoling'

def e_namedtuple():
	from collections import namedtuple
	Point = namedtuple('Point', ['x', 'y'])
	p = Point(1, 2)
	print 'p.x:', p.x
	print 'p.y:', p.y
	print 'p is Point?', isinstance(p, Point)
	print 'p is tuple?', isinstance(p, tuple)
	
	Circle = namedtuple('Circle', ['x', 'y', 'r'])
	c = Circle(10, 10, 5)
	print c
	print 'c.x:', c.x
	print 'c.y:', c.y
	print 'c.r:', c.r
	
def e_deque():
	from collections import deque
	q = deque(['a', 'b', 'c'])
	q.append('x')
	q.appendleft('y')
	print q
	q.pop()
	print q
	q.popleft()
	print q
	
def e_defaultdict():
	from collections import defaultdict
	dd = defaultdict(lambda: 'N/A')
	dd['key1'] = 'abc'
	print 'dd[\'key1\']:', dd['key1']
	print 'dd[\'key2\']:', dd['key2']
	
def e_OrderedDict():
	from collections import OrderedDict
	d = dict([('a', 1),('b', 2),('c', 3)])
	print 'd:', d
	od = OrderedDict([('a', 1),('b', 2),('c', 3)])
	print 'od:', od
	
	od = OrderedDict()
	od['z'] = 1
	od['y'] = 2
	od['x'] = 3
	print 'od:', od
	print 'od.keys():', od.keys()
	
from collections import OrderedDict
import logging
logging.basicConfig(level=logging.INFO)# or logging.DEBUG for debug
class LastUpdatedOrderedDict(OrderedDict):
	def __init__(self, capacity):
		super(LastUpdatedOrderedDict, self).__init__()
		self._capacity = capacity
		
	def __setitem__(self, key, value):
		containsKey = 1 if key in self else 0
		logging.debug('--inner log--containsKey: %s' % containsKey)
		logging.debug('--inner log--len(self): %s' % len(self))
		if len(self) - containsKey >= self._capacity:
			# https://docs.python.org/2/library/collections.html?highlight=ordereddict#collections.OrderedDict.popitem
			last = self.popitem(last=False)#last=False FIFO/last=True LIFO and the True is default
			print 'remove:', last
		if containsKey:
			del self[key]
			print 'set:', (key, value)
		else:
			print 'add:', (key, value)
		OrderedDict.__setitem__(self, key, value)
		logging.debug('--inner log-- %s\n' % self)
		
def e_LastUpdatedOrderedDict():
	luod = LastUpdatedOrderedDict(5)
	luod['a'] = 1
	luod['b'] = 2
	luod['c'] = 3
	luod['d'] = 4
	luod['e'] = 5
	luod['f'] = 6
	luod['a'] = 7
	luod['a'] = 1
	
def e_Counter(s):
	print 's:', s
	from collections import Counter
	c = Counter()
	for ch in s:
		c[ch] = c[ch] + 1
	print 'c:', c
	print 'Counter(s):', Counter(s)
	
if __name__ == '__main__':
#	e_namedtuple()
#	e_deque()
#	e_defaultdict()
#	e_OrderedDict()
	e_LastUpdatedOrderedDict()
#	e_Counter('programming')
#	e_Counter('exercise')