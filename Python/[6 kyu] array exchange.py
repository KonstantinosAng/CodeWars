# see https://www.codewars.com/kata/5353212e5ee40d4694001114/solutions

from TestFunction import Test

def exchange_with(a, b):
  #globals()['b'], globals()['a'] = [x for x in reversed(args[0])], [x for x in reversed(args[1])]
  #b, a = [x for x in reversed(args[0])], [x for x in reversed(args[1])]
  a[:], b[:] = b[::-1], a[::-1]

Test = Test(None)
a = ["1", "2", "3", "4", "5", "6", "7"]
b = ["a", "b", "c"]
exchange_with(a, b)
Test.assert_equals(a, ["c", "b", "a"])
Test.assert_equals(b, ["7", "6", "5", "4", "3", "2", "1"])
