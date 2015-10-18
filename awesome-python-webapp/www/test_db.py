#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models import User, Blog, Comment

from transwarp import db

import time

import hashlib

db.create_engine(user='www-data', password='www-data', database='awesome')

u = User(name='Test', email='test@example.com', password=hashlib.md5('1234567890').hexdigest(), image='about:blank')
#u.insert()

u = User(name='Amylovesong', email='amylovesong@example.com', password=hashlib.md5('amylovesong').hexdigest(), image='about:blank')
#u.insert()

#insert into users(`id`, `email`, `password`, `admin`, `name`, `image`, `created_at`) values ('0014442895491183b4dcfc2068e45b39a5e2b5a5f1a96bf000', 'admin@example.com', 'adminpwdsxl', 1, 'Administrator', 'about:blank', 1444288507.812);
u = User(id='0014442895491183b4dcfc2068e45b39a5e2b5a5f1a96bf000', email='admin@example.com', password=hashlib.md5('admin').hexdigest(), admin=1, name='Administrator', image='about:blank', created_at='1444288507.812')
#u.insert()

#print 'new user id:', u.id

u1 = User.find_first('where email=?', 'test@example.com')
print 'find user\'s name:', u1.name

#u1.delete()

u2 = User.find_first('where email=?', 'test@example.com')
print 'find user:', u2

'''b = Blog(name='Test Blog', summary='Test blog to test new update. There has not real data in database yet, so write something here to test blablabla.', content='blabla blabla blabla.', created_at=time.time())
b.insert()
b = Blog(name='Something New', summary='Test blog to test new update. There has not real data in database yet, so write something here to test blablabla.', content='blabla blabla blabla.', created_at=time.time() - 3 * 3600)
b.insert()
b = Blog(name='Learn Python', summary='Test blog to test new update. There has not real data in database yet, so write something here to test blablabla.', content='blabla blabla blabla.', created_at=time.time() - 24 * 2 * 3600)
b.insert()'''

#b1 = Blog.find_first('where content=?', 'blabla blabla blabla.')
#print 'find blog:', b1.name
#b1.delete()



