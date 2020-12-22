# see https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/train/python

from TestFunction import Test

def shifted_diff(first, second):
  if len(first) != len(second): return -1
  count = 0
  while count <= len(first):
    if first == second:
      return count
    first = first[::-1][0] + first[:-1]
    count += 1
  return -1

test = Test(None)
test.assert_equals(shifted_diff("eecoff","coffee"), 4)
test.assert_equals(shifted_diff("Moose","moose"), -1)
test.assert_equals(shifted_diff("isn't","'tisn"), 2)
test.assert_equals(shifted_diff("Esham","Esham"), 0)
test.assert_equals(shifted_diff(" "," "), 0)
test.assert_equals(shifted_diff("hoop","pooh"), -1)
test.assert_equals(shifted_diff("  "," "), -1)
