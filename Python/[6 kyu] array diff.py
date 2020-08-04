# see https://www.codewars.com/kata/523f5d21c841566fde000009/solutions/python

from TestFunction import Test

def not_equal(x1, b):
  for x2 in b:
    if x1 == x2: return False
  return True

def array_diff(a, b):
  if a == []: return []
  if b == []: return a
  rv = []
  for x in a:
    if not_equal(x, b):
      rv.append(x)
  return rv

Test = Test(None)
Test.assert_equals(array_diff([1,2], [1]), [2])
Test.assert_equals(array_diff([1,2,2], [1]), [2,2])
Test.assert_equals(array_diff([1,2,2], [2]), [1])
Test.assert_equals(array_diff([1,2,2], []), [1,2,2])
Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
