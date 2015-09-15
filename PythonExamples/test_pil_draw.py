#!/usr/bin/env python
# -*- coding: utf-8 -*-

'PIL ImageDraw exercise'

__author__ = 'sunxiaoling'

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
	rnd_char = chr(random.randint(65, 90))
	print rnd_char
	return rnd_char

def rndColor():
	return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	
def rndColor2():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
	for y in range(height):
		draw.point((x, y), fill=rndColor())
#输出文字
for t in range(4):
	print 't:', t
	draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
image = image.filter(ImageFilter.BLUR)
image.save('pil_code.jpg', 'jpeg')



