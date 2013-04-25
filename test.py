#!/usr/bin/python

"""
A simple python script to toggle between hex (#rrggbb or #rgb) colour values and their rgb(rr,gg,bb) equivalents
"""

import hexer
import unittest

class TestRGB(unittest.TestCase):

    def setUp(self):
      self.black = hexer.RGB('#000')
      self.white = hexer.RGB('#fff')
      pass

    def testHex(self):
      self.assertEqual(self.black.hex(), '#000')
      self.assertEqual(self.white.hex(), '#000')
#      self.assertRaises(TypeError, random.shuffle, (1,2,3))
      pass

    def testRGB(self):
      self.assertEqual(self.white.rgb(), 'rgb(0,0,0)')
#      self.assertTrue(True)
      pass

if __name__ == '__main__':
    unittest.main()
