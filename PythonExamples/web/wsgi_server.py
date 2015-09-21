#!/usr/bin/env python
# -*- coding: utf-8 -*-

'WSGI exercise: server'

__author__ = 'sunxiaoling'

from wsgiref.simple_server import make_server
from wsgi_hello import application

httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
httpd.serve_forever()