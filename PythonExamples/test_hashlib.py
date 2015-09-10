#!/usr/bin/env python
# -*- coding: utf-8 -*-

'inner module: hashlib'

__author__ = 'sunxiaoling'

import hashlib

def e_md5():
    md5 = hashlib.md5()
    md5.update('how to use md5 in python hashlib?')
    print md5.hexdigest()
    
    md5 = hashlib.md5()
    md5.update('how to use md5 in ')
    md5.update('python hashlib?')
    print md5.hexdigest()

def e_sha1():
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in ')
    sha1.update('python hashlib?')
    print sha1.hexdigest()

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password)
    r = md5.hexdigest()
    print 'password:%s after md5 is %s' % (password, r)
    return r

db = {
    'sxl':'a152e841783914146e4bcd4f39100686',#asdfgh
    'amy':'fa08615aeb8e661a6f452ce4dadf7f2a',#hjbj
    'dbb':'4baaa0a54cff85e11820e2fef0a12839'#199046
}

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password)
    if user in db:
        if db[user] == md5.hexdigest():
            print 'The user(%s) login success!' % user
            return True
        else:
            print 'The user(%s) login failed because the password is wrong!' % user
            return False
    else:
        print 'The user(%s) has not been registered!' % user
        return False

db_new = {}

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    without_salt = get_md5(password)
    print 'without_salt:%s\nwith_salt:   %s' % (without_salt, db[username])

def get_md5(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()

def login_new(username, password):
    if username in db:
        if db[username] == get_md5(password + username + 'the-Salt'):
            print 'The user(%s) login success!' % username
            return True
        else:
            print 'The user(%s) login failed because the password is wrong!' % username
            return False
    else:
        print 'The user(%s) has not been registered!' % username
        return False

if __name__ == '__main__':
#    e_md5()
#    e_sha1()
#    calc_md5('199046')
#    print login('sxl', 'asdfgh')
#    print login('amy', 'hbhb')
#    print login('sabb', '1001')
    register('sxl', '1111')
    print login_new('sxl', '1110')
