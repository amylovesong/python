#!/usr/bin/env python
# -*- coding:utf-8 -*-

'DB MySQL exercise'

__author__ = 'sunxiaoling'

import mysql.connector

def db_insert_user():
	conn = mysql.connector.connect(user='root', password='', database='test', use_unicode=True, port=3307)
	cursor = conn.cursor()
	cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
	cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'sxl'])
	print cursor.rowcount
	conn.commit()
	cursor.close()
	conn.close()

def db_create_book_table():
	conn = mysql.connector.connect(user='root', password='', database='test', use_unicode=True, port=3307)
	cursor = conn.cursor()
	cursor.execute('create table book (id varchar(20) primary key, name varchar(20), user_id varchar(20), foreign key (user_id) references user(id))')
	conn.commit()
	cursor.close()
	conn.close()

def db_delete_book_table():
	conn = mysql.connector.connect(user='root', password='', database='test', use_unicode=True, port=3307)
	cursor = conn.cursor()
	cursor.execute('drop table book')
	conn.commit()
	cursor.close()
	conn.close()

def db_select_book():
	conn = mysql.connector.connect(user='root', password='', database='test', use_unicode=True, port=3307)
	cursor = conn.cursor()
#	cursor.execute('select * from book where id = %s', ['1'])
	cursor.execute('select * from book')
	values = cursor.fetchall()
	print values
	cursor.close()
	conn.close()

def db_select_user():
	conn = mysql.connector.connect(user='root', password='', database='test', use_unicode=True, port=3307)
	cursor = conn.cursor()
#	cursor.execute('select * from user where id = %s', ['1'])
	cursor.execute('select * from user')
	values = cursor.fetchall()
	print values
	cursor.close()
	conn.close()

if __name__ == '__main__':
#	db_insert_user()
	db_select_user()
#	db_create_book_table()
	db_select_book()
#	db_delete_book_table()

