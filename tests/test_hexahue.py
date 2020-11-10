#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image
from PIL import ImageChops
import yaml
import copy
import unittest
import hexahue

IMG_PREFIX = './tests/testimg/'

class TestHexahue(unittest.TestCase):

	def compare_message(self, m1, m2):
		if m1.upper() == m2.upper():
			return True
		if m1[:len(m2)].upper() != m2.upper():
			return False
		if all([m == ' ' for m in m1[len(m2):]]):
			return True
		return False
		
	def test_normal(self):
		test_patterns = [
			# padding, message, space_clor, max_width, expected_filename
			({'top':0,'right':0,'bottom':0,'left':0}, 'th1s 1s t3st.', 'white', 1200, 'test_normal1.png'),
			({'top':0,'right':0,'bottom':0,'left':0}, 'Hello, '*100, 'white', 1200, 'test_normal2.png'),
			({'top':10,'right':1,'bottom':0,'left':2}, 'th1s 1s t3st.', 'white', 1200, 'test_normal3.png'),
			({'top':0,'right':10,'bottom':7,'left':3}, 'Hello, '*100, 'white', 1200, 'test_normal4.png'),
			({'top':0,'right':0,'bottom':0,'left':0}, 'th1s 1s t3st.', 'black', 1200, 'test_normal5.png'),
			({'top':0,'right':0,'bottom':0,'left':0}, 'Hello, '*100, 'black', 1200, 'test_normal6.png'),
			({'top':0,'right':0,'bottom':0,'left':0}, 'th1s 1s t3st.', 'white', 60, 'test_normal7.png'),
			({'top':0,'right':0,'bottom':0,'left':0}, 'Hello, '*100, 'white', 60, 'test_normal8.png')
			]
		for padding, message, space_clor, max_width, expected_filename in test_patterns:
			with self.subTest(expected_filename = expected_filename):
				with open('settings.yaml', 'r') as f:
					settings = yaml.safe_load(f)
				settings['image']['padding'] = padding
				settings['hexahue']['space'] = space_clor
				settings['image']['max_width'] = max_width
				encoded = hexahue.hexahue_encode(message, settings)
				expected_img = Image.open(IMG_PREFIX + expected_filename)
				self.assertFalse((ImageChops.difference(encoded, expected_img)).getbbox())
				decoded = hexahue.hexahue_decode(expected_img, settings)
				self.assertTrue(self.compare_message(decoded, message))

if __name__ == "__main__":
	unittest.main()