# see https://www.codewars.com/kata/59f38b033640ce9fc700015b/solutions/python

from TestFunction import Test

def is_prime(num):
  for i in range(2,num):
    if (num % i) == 0:
      return False    
  else:
    return True       


def total(arr):
  _sum = 0
  for i, value in enumerate(arr):
    if i >= 2 and is_prime(i):
      _sum += value
  return _sum


Test = Test(None)
Test.assert_equals(total([]),0)
Test.assert_equals(total([1,2,3,4]),7)
Test.assert_equals(total([1,2,3,4,5,6]),13)
Test.assert_equals(total([1,2,3,4,5,6,7,8]),21)
Test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11]),21)
Test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11,12,13]),33)
Test.assert_equals(total([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]),47)
