#!/usr/bin/env python
# -*- coding: utf-8 -*-

'inner module: struct'

__author__ = 'sunxiaoling'

import struct, os

def _32bit_int_to_str():
    n = 10240099
    b1 = chr((n & 0xff000000) >> 24)
    b2 = chr((n & 0xff0000) >> 16)
    b3 = chr((n & 0xff00) >> 8)
    b4 = chr(n & 0xff)
    print 'b1:%s b2:%s b3:%s b4:%s' % (b1, b2, b3, b4)
    s = b1 + b2 + b3 + b4
    print 's:', s

def struct_pack():
    # >：big-endian，I：4字节无符号整数
    print struct.pack('>I', 10240099)

def struct_unpack():
    # H：2字节无符号整数
    print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')

def struct_bmp():
    path = os.path.join('.', 'files', 'for_struct.bmp')
    print path
    with open(path, 'rb') as f:
        s = f.read(30)
    print 's:', s
    print 'unpack result:', struct.unpack('<ccIIIIIIHH', s)

def bmpinfo(file_path):
    abs_file_path = os.path.abspath(file_path)
    with open(file_path) as f:
        s = f.read(30)
    info = struct.unpack('<ccIIIIIIHH', s)
    if info[0]=='B' and info[1] == ('M' or 'A'):
        print 'the file (%s) info:\nsize: %d * %d' % (abs_file_path, info[6], info[7])
        print 'color count:', info[9]
        return
    print 'The file (%s) is not bmp!' % abs_file_path
    
if __name__ == '__main__':
#    _32bit_int_to_str()
#    struct_pack()
#    struct_unpack()
#    struct_bmp()
    bmpinfo(os.path.join('.', 'files', 'for_struct.bmp'))
    bmpinfo(os.path.join('.', 'files', 'img.jpg'))
