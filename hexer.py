#!/usr/bin/python

"""
A simple python script to toggle between hex (#rrggbb/#rgb) colour values and their rgb(rr,gg,bb) equivalents
"""

import sys

class Colour:
  """
  
  """
  def __init__(self, value):

    self.value = value

    if (value[0] == '#'):
 #     print '#' + value
      pass
    elif (value[0:4] == 'rgb('):
#      print 'rgb(' + value + ')'
      pass
    else:
      raise Error, value + "is not a valid colour\n"


  def toHex(self):
    return '#' + value

  def toRGB(self):
    return 'rgb(' + value + ')'

  def __str__(self):
    return self.value



if len(sys.argv) == 1:
  sys.stderr.write("No colour specified\n")

for i in sys.argv[1:]:
  c = Colour(i)
  print c
  