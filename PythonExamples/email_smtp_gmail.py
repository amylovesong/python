#!/usr/bin/env python
# -*- coding:utf-8 -*-

'SMTP exercise'

__author__ = 'sunxiaoling'

from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = raw_input('From: ')
password = raw_input('Password: ')
to_addr = raw_input('To: ')
smtp_server = 'smtp.gmail.com'
smtp_port = 587

from_addr = 'amylovesong.sun@gmail.com'
password = 'hjbj1110'
to_addr = 'forever-yongyuan@163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# 加密SMTP
server = smtplib.SMTP(smtp_server, smtp_port) # The default port is 25
server.starttls()
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()