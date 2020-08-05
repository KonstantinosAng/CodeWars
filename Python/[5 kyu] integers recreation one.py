# see https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

import math

def list_squared(m, n):
  is_square = lambda n: int(math.sqrt(n) + 0.5) ** 2 == n
  rv = []
  for i in range(m, n):
    s = sum([j**2 for j in range(1, i+1) if i%j==0])
    if is_square(s): rv.append([i, s])
  return rv

from TestFunction import Test
Test = Test(None)
Test.assert_equals(list_squared(1, 250), [[1, 1], [42, 2500], [246, 84100]])
Test.assert_equals(list_squared(42, 250), [[42, 2500], [246, 84100]])
Test.assert_equals(list_squared(250, 500), [[287, 84100]])
Test.assert_equals(list_squared(999, 3555), [[1434, 2856100], [1673, 2856100], [1880, 4884100]])
Test.assert_equals(list_squared(322, 2095), [[728, 722500], [1434, 2856100], [1673, 2856100], [1880, 4884100]])
Test.assert_equals(list_squared(213, 2338), [[246, 84100], [287, 84100], [728, 722500], [1434, 2856100], [1673, 2856100], [1880, 4884100]])
Test.assert_equals(list_squared(692, 5442), [[728, 722500], [1434, 2856100], [1673, 2856100], [1880, 4884100], [4264, 24304900]])
Test.assert_equals(list_squared(344, 5401), [[728, 722500], [1434, 2856100], [1673, 2856100], [1880, 4884100], [4264, 24304900]])
