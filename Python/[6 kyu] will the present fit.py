# see https://www.codewars.com/kata/52b23340c65ea422b1000045/solutions/python

from TestFunction import Test

def will_fit(present, box):
  present, box = sorted(present), sorted(box)
  for dim1, dim2 in zip(present, box):
    if dim1 > dim2 - 2: return False
  return True


Test = Test(None)
Test.assert_equals(will_fit((10, 2, 4), (6, 4, 12)), True)
Test.assert_equals(will_fit((1, 2, 3), (2, 1, 3)), False)