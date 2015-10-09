#!/usr/bin/env python
# -*- coding:utf-8 -*-

def list_arrangement(list):
	length = len(list)
	print 'length of original list:', length
	list_results = []
	list_size = range(1, length + 1)
	print 'list_size:', list_size, '\n'

	for size in list_size:
		temp = ''
		print '--size:', size
		for i, value in enumerate(list):
			print '----i:%s value:%s' % (i, value)
			e_start = value
			e_next = ''
			temp = e_start
			if len(temp) < size:
				for gap in range(1, length-i):
					print 'gap:', gap
					e_next = list[i + gap]
					print 'e_start:', e_start, 'e_next:', e_next
					temp += e_next
					if len(temp) == size:
						print '------temp:', temp
						list_results.append(temp)
						temp = e_start
			else:
				print '------temp:', temp
				list_results.append(temp)
	return list_results



if __name__ == '__main__':
	l = ['a', 'b', 'c', 'd']
	print list_arrangement(l)