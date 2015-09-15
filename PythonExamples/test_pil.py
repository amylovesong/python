#!/usr/bin/env python
# -*- coding: utf-8 -*-

'PIL exercise'

__author__ = 'sunxiaoling'

import Image, ImageFilter
import os

def e_pil_scale():
	im = Image.open(os.path.join('.', 'files', 'img.jpg'))
	w, h = im.size
	print 'w:', w, 'h:', h
	im.thumbnail((w//2, h//2))
	im.save(os.path.join('.', 'files', 'img_thumbnail.jpg'), 'jpeg')
	print 'scale success!'
	
def e_pil_filter():
	im = Image.open(os.path.join('.', 'files', 'img.jpg'))
	im2 = im.filter(ImageFilter.BLUR)
	im2.save(os.path.join('.', 'files', 'img_blur.jpg'), 'jpeg')
	
if __name__ == '__main__':
#	e_pil_scale()
	e_pil_filter()