#!/usr/bin/python

"""
A simple python script to toggle between hex (#rrggbb or #rgb) colour values and their rgb(rr,gg,bb) equivalents
"""

import sys

class RGB:
  """
  
  """

  def __init__(self, value):
    """
    
    
    @param value - the colour value to be parsed
    @raise Exception if an invalid colour value is provided
    """

    self.isHex = False
    self.red = self.blue = self.green = 0

    if (value[0] == '#'):
      self.isHex = True
      if (len(value) == 4):
        pass
      elif (len(value) == 7):
        pass
      else:
        raise Exception, 'Invalid hex colour: "' + value + '"'

    elif (value[0:4] == 'rgb('):
      pass
    else:
      raise Exception, '"' + value + '" is not a valid colour'

#    if (self.red > 255 or self.green > 255 or self.blue or 255 or self.red < 0 or self.green < 0 or self.blue < 0):
#      raise Exception, value + " is not a valid colour"

  def toggle(self):
    """
    Return the opposite representation of a colour (ie: hex if created as rgb(), or vice-versa) 

    @return string 
    """
    return self.rgb() if self.isHex else self.hex()

  def _d2h(self, n):
    """

    @return string - the hexadecimal string representation of integer n
    """
    return "%X" % n

  def hex(self):
    """
    @return string - the colour declaration in #rrggbb format
    """
    return '#' + self._d2h(self.red) + self._d2h(self.blue) + self._d2h(self.green)

  def rgb(self):
    """
    @return string - the colour declaration in rgb(rr,gg,bb) format
    """
    return 'rgb(' + str(self.red) + ',' + str(self.green) + ',' + str(self.blue) + ')'

  def __str__(self):
    """
    
    @return string
    """
    return self.hex() if self.isHex else self.rgb()


#
#
#

if __name__ == '__main__':

  if len(sys.argv) == 1:
    sys.stderr.write("No colour specified\n")
    sys.exit(1)

  for i in sys.argv[1:]:
    try:
      c = RGB(i)
      print c.hex()
    except Exception, e:
      print e