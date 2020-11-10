#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image
import math
import yaml
from hexahue_map import HexahueMap

def hexahue_decode(img, settings):
	hexahue_map = HexahueMap('all')
	padding = settings['image']['padding']
	width, height = img.size
	decoded = ''
	for hi in range((height-padding['top']-padding['bottom']) // 3):
	    for wi in range((width-padding['left']-padding['right']) // 2):
	    	block = (img.getpixel((wi*2+0+padding['left'],hi*3+0+padding['top'])),
	    	 		 img.getpixel((wi*2+1+padding['left'],hi*3+0+padding['top'])),
	    	 		 img.getpixel((wi*2+0+padding['left'],hi*3+1+padding['top'])),
	    	 		 img.getpixel((wi*2+1+padding['left'],hi*3+1+padding['top'])),
	    			 img.getpixel((wi*2+0+padding['left'],hi*3+2+padding['top'])),
	    	 		 img.getpixel((wi*2+1+padding['left'],hi*3+2+padding['top'])))
	    	try:
	    		decoded += hexahue_map.hmap[block]
	    	except KeyError:
	    		raise Exception('[Error] Current decode message: ' + decoded
	    						 + '\nNo Hexahue Mapping found: ' + repr(block))
	
	return decoded

def hexahue_encode(message, settings):
	hexahue_map = HexahueMap(settings['hexahue']['space'])
	padding = settings['image']['padding']
	# check message
	for m in message:
		if not (m.isalpha() or m.isdigit() or (m in [',','.',' '])):
			raise Exception('[Error] invalid message input: ' + m)
	# create image
	w_num = min((settings['image']['max_width']-padding['right']-padding['left']) // 2,
				len(message))
	h_num = math.ceil(len(message) / w_num)
	width = w_num*2 + padding['right'] + padding['left']
	height = h_num*3 + padding['top'] + padding['bottom']
	img = Image.new('RGB', (width, height), [k for k, v in hexahue_map.hmap.items() if v == ' '][0][0])
	for i in range(len(message)):
		m = message[i]
		if m.islower():
			m = m.upper()
		block = [k for k, v in hexahue_map.hmap.items() if v == m][0]
		hi = i // w_num
		wi = i % w_num
		for h in range(3):
	    		for w in range(2):
	    			img.putpixel((wi*2+w+padding['left'],hi*3+h+padding['top']), block[h*2+w])
	return img

if __name__ == '__main__':
	with open('settings.yaml', 'r') as f:
		settings = yaml.safe_load(f)
	mode = input('input mode (d: decode, e: encode) > ')
	if mode == 'd' or mode == 'D' or mode == 'decode':
		filename = input('input source filename > ')
		img = Image.open(filename)
		print(hexahue_decode(img, settings))
	elif mode == 'e' or mode == 'E' or mode == 'encode':
		filename = input('input output image filename > ')
		message = input('input message for encript > ')
		output_img = hexahue_encode(message, settings)
		output_img.save(filename)
	else:
		raise Exception('[Error] invalid mode input!')