#!/usr/bin/env python
# -*- coding:utf-8 -*-

'SMTP exercise'

__author__ = 'sunxiaoling'

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
smtp_server = raw_input('SMTP server: ')
to_addr = raw_input('To: ')

msg = MIMEMultipart()
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 正文
msg.attach(MIMEText('<html><body><h1>Hello</h1>' + '<p><img src="cid:0"></p>' + '</body></html>', 'html', 'utf-8'))
# 附件
import os
img_f_name = 'img_cute.jpg'
with open(os.path.join('.', 'files', img_f_name), 'rb') as f:
	mime = MIMEBase('image', 'jpg', filename=img_f_name)
	mime.add_header('Content-Disposition', 'attachment', filename=img_f_name)
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-ID', '0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25) # The default port is 25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()