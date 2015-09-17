#!/usr/bin/env python
# -*- coding: utf-8 -*-

'TCP socket exercise'

__author__ = 'sunxiaoling'

import socket
import os

# AF_INET 指定使用IPv4协议，如需使用IPv6，则为AF_INET6
# SOCK_STREAM 指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com.cn', 80))
# 发送数据
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收
buffer = []
while True:
	d = s.recv(1024) # 参数为最多接收的字节数
	if d:
		buffer.append(d)
	else:
		break
data = ''.join(buffer)
s.close()

header, html = data.split('\r\n\r\n', 1)
print header
with open(os.path.join('.', 'files', 'sina.html'), 'wb') as f:
	f.write(html)