#!/usr/bin/python

"""
Unit tests for hexer module
"""

import hexer
import unittest

class TestRGB(unittest.TestCase):

    def setUp(self):

      self.hex = {
        'black' : hexer.RGB('#000'),
        'white' : hexer.RGB('#fff'),
        'yellow' : hexer.RGB('#ffff00')
      }

      self.rgb = {
        'black' : hexer.RGB('rgb(0,0,0)'),
        'white' : hexer.RGB('rgb(255,255,255)'),
        'yellow' : hexer.RGB('rgb(255,255,0)')
      }

    def testHexer(self):

      self.assertEqual(self.hex['black'].hex(), '#000000')
      self.assertEqual(self.hex['black'].rgb(), 'rgb(0,0,0)')
      self.assertEqual(self.hex['black'].toggle(), 'rgb(0,0,0)')

      self.assertEqual(self.hex['white'].hex(), '#FFFFFF')
      self.assertEqual(self.hex['white'].rgb(), 'rgb(255,255,255)')
      self.assertEqual(self.hex['white'].toggle(), 'rgb(255,255,255)')

      self.assertEqual(self.hex['yellow'].hex(), '#FFFF00')
      self.assertEqual(self.hex['yellow'].rgb(), 'rgb(255,255,0)')
      self.assertEqual(self.hex['yellow'].toggle(), 'rgb(255,255,0)')

      self.assertEqual(self.rgb['black'].hex(), '#000000')
      self.assertEqual(self.rgb['black'].rgb(), 'rgb(0,0,0)')
      self.assertEqual(self.rgb['black'].toggle(), '#000000')

      self.assertEqual(self.rgb['white'].hex(), '#FFFFFF')
      self.assertEqual(self.rgb['white'].rgb(), 'rgb(255,255,255)')
      self.assertEqual(self.rgb['white'].toggle(), '#FFFFFF')

      self.assertEqual(self.rgb['yellow'].hex(), '#FFFF00')
      self.assertEqual(self.rgb['yellow'].rgb(), 'rgb(255,255,0)')
      self.assertEqual(self.rgb['yellow'].toggle(), '#FFFF00')

if __name__ == '__main__':
    unittest.main()
