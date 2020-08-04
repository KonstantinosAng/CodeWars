# see https://www.codewars.com/kata/59b2883c5e2308b54d000013/solutions/python

from TestFunction import Test

def is_onion_array(a):
  i = 0; j = -1
  while i != len(a)//2:
    if a[i] + a[j] > 10:
      return False
    i += 1
    j -= 1
  return True

Test = Test(None)
Test.assert_equals(is_onion_array([6, 0, 4]), True)
Test.assert_equals(is_onion_array([1, 1, 15, 10, -1]), False)
