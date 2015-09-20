#!/usr/bin/env python
# -*- coding:utf-8 -*-

'DB ORM in python: SQLAlchemy'

__author__ = 'sunxiaoling'

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))

	books = relationship('Book')

class Book(Base):
	__tablename__ = 'book'

	id = Column(String(20), primary_key=True)
	name = Column(String(20))
	user_id = Column(String(20), ForeignKey('user.id'))

engine = create_engine('mysql+mysqlconnector://roo:@localhost:3307/test')
DBSession = sessionmaker(bind=engine)

def orm_add_user():
	session = DBSession()
	new_user = User(id='5', name='Bob')
	new_user = User(id='2', name='dabeibi')
	session.add(new_user)
	session.commit()
	session.close()

def orm_add_book():
	session = DBSession()
#	new_book = Book(id='1', name='Python', user_id='5')
#	new_book = Book(id='2', name='Head First Java', user_id='5')
	new_book = Book(id='3', name='Java', user_id='2')
	session.add(new_book)
	session.commit()
	session.close()

def orm_query():
	session = DBSession()
	user = session.query(User).filter(User.id=='2').one()
	print 'type:', type(user)
	print 'name:', user.name
	print 'books:'
	for book in user.books:
		print '	', book.name
	session.close()

if __name__ == '__main__':
#	orm_add_user()
	orm_add_book()
	orm_query()