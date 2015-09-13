#!/usr/bin/env python
# -*- coding: utf-8 -*-

'multi_processing exercise'

__author__ = 'sunxiaoling'

import os

def e_fork():
	print 'Process (%s) start...' % os.getpid()
	pid = os.fork()
	if pid==0:
		print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
	else:
		print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

from multiprocessing import Process

def run_proc(name):
	print 'Run child process %s (%s)...' % (name, os.getpid())

def e_process():
	print 'Parent process %s.' % os.getpid()
	p = Process(target=run_proc, args=('test',))
	print 'Process will start.'
	p.start()
	p.join() #--可以等待子进程结束后再继续往下运行，通常用于进程间同步
	print 'Process end.'

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
	print 'Run task %s (%s)...' % (name, os.getpid())
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print 'Task %s runs %0.2f seconds.' % (name, (end - start))

def e_pool():
	print 'Parent process %s.' % os.getpid()
	p = Pool()# the default size of pool is the core numbers of CPU
	for i in range(5):
		p.apply_async(long_time_task, args=(i,))
	print 'Waiting for all subprocesses done...'
	p.close()
	p.join()
	print 'All subprocesses done.'

from multiprocessing import Process, Queue
import os, time, random

def write(q):
	for value in ['A', 'B', 'C']:
		print 'Put %s to queue...' % value
		q.put(value)
		time.sleep(random.random())

def read(q):
	while True:
		# Queue.get([block[, timeout]])
		# If optional args block is true and timeout is None (the default), block if necessary until an item is available.
		value = q.get(True)
		print 'Get %s from queue.' % value

def e_queue():
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()

if __name__ == '__main__':
#	e_fork()
#	e_process()
#	e_pool()
	e_queue()