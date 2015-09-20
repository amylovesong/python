#!/usr/bin/env python
# -*- coding:utf-8 -*-

'DB Sqlite exercise'

__author__ = 'sunxiaoling'

import sqlite3

def db_insert():
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
	cursor.execute('insert into user (id, name) values(\'1\', \'sxl\')')
	print cursor.rowcount
	cursor.close()
	conn.commit()
	conn.close()

def db_select():
	conn = sqlite3.connect('test.db')
	cursor = conn.cursor()
	cursor.execute('select * from user where id=?', '1')
	values = cursor.fetchall()
	print values
	cursor.close()
	conn.close()

if __name__ == '__main__':
#	db_insert()
	db_select()