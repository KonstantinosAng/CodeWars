# see https://www.codewars.com/kata/57d448c6ba30875437000138/solutions/python

from TestFunction import Test
import math

def roots(a,b,c):
  d = b**2 - 4*a*c
  if d >= 0:
    return float("%.2f" % sum([(-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)]))
  else:
    return  None


Test = Test(None)
Test.assert_equals(roots(6,3,8),None)
Test.assert_equals(roots(2,11,-6),-5.5)
Test.assert_equals(roots(5,-8,3),1.6)
Test.assert_equals(roots(6,4,9),None)
Test.assert_equals(roots(1,-2,-5.25),2)
Test.assert_equals(roots(3,-10,5),3.33)
Test.assert_equals(roots(5,2,4),None)
Test.assert_equals(roots(1,4,3),-4)
Test.assert_equals(roots(2,3,1),-1.5)
Test.assert_equals(roots(1,-4,4),4)
Test.assert_equals(roots(1,3,9),None)
Test.assert_equals(roots(1,-1,-20),1)
Test.assert_equals(roots(2,-4,-2),2)
Test.assert_equals(roots(6,11,-35),-1.83)
Test.assert_equals(roots(3,4,9),None)
Test.assert_equals(roots(-4,-7,12),-1.75)
Test.assert_equals(roots(1,-1,-3),1)
Test.assert_equals(roots(5,-2,-9),0.4)
Test.assert_equals(roots(2,8,0),-4)
Test.assert_equals(roots(3,5,10),None)
