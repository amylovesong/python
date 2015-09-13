#!/usr/bin/env python
# -*- coding: utf-8 -*-

'multi_threading exercise'

__author__ = 'sunxiaoling'

import time, threading

def e_thread():
	def loop():
		print 'thread %s is running...' % threading.current_thread().name
		n = 0
		while n < 5:
			n = n + 1
			print 'thread %s >>> %s' % (threading.current_thread().name, n)
			time.sleep(1)
		print 'thread %s ended.' % threading.current_thread().name


	print 'thread %s is running...' % threading.current_thread().name
	t = threading.Thread(target=loop, name='LoopThread')
	t.start()
	t.join()
	print 'thread %s ended.' % threading.current_thread().name

balance = 0
def e_lock():
	lock = threading.Lock()

	def change_it(n):
		global balance
		balance = balance + n
		balance = balance - n

	def run_thread(n):
		for i in range(100000):
			lock.acquire()
			try:
				change_it(i)
			finally:
				lock.release()

	t1 = threading.Thread(target=run_thread, args=(5,))
	t2 = threading.Thread(target=run_thread, args=(8,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print balance

def e_dead_loop():
	import threading, multiprocessing
	def loop():
		x = 0
		while True:
			x = x ^ 1

	print 'cpu_count:', multiprocessing.cpu_count()
	for i in range(multiprocessing.cpu_count()):
		t = threading.Thread(target=loop)
		t.start()

if __name__ == '__main__':
#	e_thread()
#	e_lock()
	e_dead_loop()









