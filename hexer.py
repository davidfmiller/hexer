#!/usr/bin/python

"""
A simple python script to toggle between hex (#rrggbb or #rgb) colour values and their rgb(rr,gg,bb) equivalents
"""

import sys, re

class RGB:
  """
  
  """

  def __init__(self, value):
    """

    @param value - the colour value to be parsed
    @raise Exception if an invalid colour value is provided
    """

    self.red = self.blue = self.green = 0
    self.isHex = False

    value = value.strip()

    if (value[0] == '#'):

      self.isHex = True      
      r = g = b = 0;

      if (len(value) == 4):

        r = value[1] * 2
        g = value[2] * 2
        b = value[3] * 2

      elif (len(value) == 7):

        r = value[1:3]
        g = value[3:5]
        b = value[5:7]

      else:
        raise Exception, 'Invalid hex colour: "' + value + '"'

      self.red   = int(r, 16)
      self.green = int(g, 16)
      self.blue  = int(b, 16)

    elif (value[0:4] == 'rgb('):
      reg = re.compile('rgb\((\d+),(\d+),(\d+)\)')
      prog = reg.match(value)

      self.red = int(prog.group(1))
      self.green = int(prog.group(2))
      self.blue = int(prog.group(3))

    else:
      raise Exception, '"' + value + '" is not a valid colour'

    if (self.red > 255 or self.green > 255 or self.blue > 255 or self.red < 0 or self.green < 0 or self.blue < 0):
      raise Exception, '"' + value + '" is not a valid colour'

  def _d2h(self, n):
    """

    @return string - the decimal string representation of integer n
    """

    tmp = "%x" % n
    return ('0' if len(tmp) == 1 else '') + tmp 

  def toggle(self):
    """
    
    @return string
    """
    return self.rgb() if self.isHex else self.hex()

  def hex(self):
    """
    @return string - the colour declaration in #rrggbb format
    """

    return ('#' + self._d2h(self.red) + self._d2h(self.green) + self._d2h(self.blue)).upper()

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

  colours = []
  if not sys.stdin.isatty():
    for line in sys.stdin:
      colours.append(line.strip())

  else:
    for i in sys.argv[1:]:
      colours.append(i)

  if len(colours) == 0:
    sys.stderr.write("No colour specified\n")
    sys.exit(1)

  try:
    for i in colours:
      c = RGB(i)
      print c.toggle()
  except Exception, e:
    sys.stderr.write(i + " is not a valid colour declaration\n")
