# see https://www.codewars.com/kata/5effa412233ac3002a9e471d/solutions/python

from TestFunction import Test

def add(num1, num2):
  num1, num2 = str(num1), str(num2)
  if len(num1) > len(num2):
    pad = len(num1) - len(num2)
    num2 = '0'*pad + num2
  else:
    pad = len(num2) - len(num1)
    num1 = '0'*pad + num1
  rv = ''
  for digit1, digit2 in zip(reversed(num1), reversed(num2)):
    rv = str(int(digit1) + int(digit2)) + rv
  return int(rv)


test = Test(None)
test.assert_equals(add(2,11), 13)
test.assert_equals(add(0,1), 1)
test.assert_equals(add(0,0), 0)
test.assert_equals(add(16,18), 214)
test.assert_equals(add(26,39), 515)
test.assert_equals(add(122,81), 1103)
