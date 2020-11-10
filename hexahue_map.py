#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import yaml

class HexahueMap():
	
	def __init__(self, space_color):
		pink   = (255, 0, 255)
		red    = (255, 0, 0)
		green  = (0, 255, 0)
		yellow = (255, 255, 0)
		blue   = (0, 0, 255)
		sky    = (0, 255, 255)
		white  = (255, 255, 255)
		gray   = (128, 128, 128)
		black  = (0, 0, 0)
		
		self.hmap = {}
		self.hmap[(pink, red, green, yellow, blue, sky)] = 'A'
		self.hmap[(red, pink, green, yellow, blue, sky)] = 'B'
		self.hmap[(red, green, pink, yellow, blue, sky)] = 'C'
		self.hmap[(red, green, yellow, pink, blue, sky)] = 'D'
		self.hmap[(red, green, yellow, blue, pink, sky)] = 'E'
		self.hmap[(red, green, yellow, blue, sky, pink)] = 'F'
		self.hmap[(green, red, yellow, blue, sky, pink)] = 'G'
		self.hmap[(green, yellow, red, blue, sky, pink)] = 'H'
		self.hmap[(green, yellow, blue, red, sky, pink)] = 'I'
		self.hmap[(green, yellow, blue, sky, red, pink)] = 'J'
		self.hmap[(green, yellow, blue, sky, pink, red)] = 'K'
		self.hmap[(yellow, green, blue, sky, pink, red)] = 'L'
		self.hmap[(yellow, blue, green, sky, pink, red)] = 'M'
		self.hmap[(yellow, blue, sky, green, pink, red)] = 'N'
		self.hmap[(yellow, blue, sky, pink, green, red)] = 'O'
		self.hmap[(yellow, blue, sky, pink, red, green)] = 'P'
		self.hmap[(blue, yellow, sky, pink, red, green)] = 'Q'
		self.hmap[(blue, sky, yellow, pink, red, green)] = 'R'
		self.hmap[(blue, sky, pink, yellow, red, green)] = 'S'
		self.hmap[(blue, sky, pink, red, yellow, green)] = 'T'
		self.hmap[(blue, sky, pink, red, green, yellow)] = 'U'
		self.hmap[(sky, blue, pink, red, green, yellow)] = 'V'
		self.hmap[(sky, pink, blue, red, green, yellow)] = 'W'
		self.hmap[(sky, pink, red, blue, green, yellow)] = 'X'
		self.hmap[(sky, pink, red, green, blue, yellow)] = 'Y'
		self.hmap[(sky, pink, red, green, yellow, blue)] = 'Z'
		self.hmap[(black, white, white, black, black, white)] = '.'
		self.hmap[(white, black, black, white, white, black)] = ','
		if space_color == 'black':
			self.hmap[(black, black, black, black, black, black)] = ' '
		elif space_color == 'white':
			self.hmap[(white, white, white, white, white, white)] = ' '
		elif space_color == 'all':
			self.hmap[(black, black, black, black, black, black)] = ' '
			self.hmap[(white, white, white, white, white, white)] = ' '
		else:
			raise Exception('[Error] invalid space setting: ' + space_color)
		self.hmap[(black, gray, white, black, gray, white)] = '0'
		self.hmap[(gray, black, white, black, gray, white)] = '1'
		self.hmap[(gray, white, black, black, gray, white)] = '2'
		self.hmap[(gray, white, black, gray, black, white)] = '3'
		self.hmap[(gray, white, black, gray, white, black)] = '4'
		self.hmap[(white, gray, black, gray, white, black)] = '5'
		self.hmap[(white, black, gray, gray, white, black)] = '6'
		self.hmap[(white, black, gray, white, gray, black)] = '7'
		self.hmap[(white, black, gray, white, black, gray)] = '8'
		self.hmap[(black, white, gray, white, black, gray)] = '9'