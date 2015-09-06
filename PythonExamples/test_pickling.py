#!usr/bin/env python
# -*- coding: utf-8 -*-

'pickling and unpickling'

__author__ = 'sunxiaoling'

try:
	import cPickle as pickle
except ImportError:
	import pickle

import json

def pickle_dump():
	d = dict(name='Bob', age=20, score=88)
	print pickle.dumps(d)
	
	f = open('dump_pickle.txt', 'wb')
	pickle.dump(d, f)
	f.close
	
def pickle_load():
	f = open('dump_pickle.txt', 'rb')
	d = pickle.load(f)
	f.close()
	print d
	
def json_dump():
	d = dict(name='Bob', age=20, score=88)
	print json.dumps(d)
	
	f = open('dump_json.txt', 'wb')
	json.dump(d, f)
	f.close()

def json_loads():
	json_str = '{"age":20, "score":88, "name":"Bob"}'
	print json.loads(json_str)
	
class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def json_dumps_custom_class():
	s = Student('Bob', 20, 88)
#	print json.dumps(s, default=student2dict)
	print json.dumps(s, default=lambda obj: obj.__dict__)

def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
	
def json_loads_custom_class():
	json_str = '{"age":20, "score":88, "name":"Bob"}'
	print json.loads(json_str, object_hook=dict2student)

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])
	
if __name__ == '__main__':
#	pickle_dump()
#	pickle_load()
#	json_dump()
#	json_loads()
#	json_dumps_custom_class()
	json_loads_custom_class()