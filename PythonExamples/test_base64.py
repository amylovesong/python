#!/usr/bin/env python
# -*- coding: utf-8 -*-

'inner module: base64 '

__author__  = 'sunxiaoling'

import base64
print 'encode:', base64.b64encode('binary\x00string')
print 'decode:', base64.b64decode('YmluYXJ5AHN0cmluZw==')

print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print '', base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')

print base64.urlsafe_b64decode('XMTMzMTY1OTc2OA==')

#print base64.b64decode('YWJjZA==')
#print base64.b64decode('YWJjZA')

def safe_b64decode(s):
    import base64
    print 's: %s %d' % (s, len(s))
    while(len(s) % 4 !=0 ):
        s += '='
        print len(s)
    print 's: %s %d' % (s, len(s))
    return base64.b64decode(s)
#    return base64.b64decode(s+'='*(4-len(s)%4))

print safe_b64decode('YWJjZA')
