# see https://www.codewars.com/kata/5511b2f550906349a70004e1/train/python

def last_digit(n1, n2):
  return pow(n1, n2, 10)

from TestFunction import Test

test = Test(None)
test.it("Example tests")
test.assert_equals(last_digit(4, 1), 4)
test.assert_equals(last_digit(4, 2), 6)
test.assert_equals(last_digit(9, 7), 9)
test.assert_equals(last_digit(10, 10 ** 10), 0)
test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)
test.it("x ** 0")
for number in range(1, 9):
  a = number ** number
  test.it("Testing %d and %d" % (a, 0))
  test.assert_equals(last_digit(a, 0), 1, "x ** 0 must return 1")
