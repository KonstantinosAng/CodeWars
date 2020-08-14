# see https://www.codewars.com/kata/555f43d8140a6df1dd00012b/train/python

import math

def coordinates(degrees, radius):
  x, y = math.cos(degrees*math.pi/180)*radius, math.sin(degrees*math.pi/180)*radius
  return (round(x, 10), round(y, 10))

from TestFunction import Test
Test = Test(None)
Test.assert_equals(coordinates(90, 1), (0.0, 1.0))
