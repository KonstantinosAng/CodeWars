# see https://www.codewars.com/kata/56efab15740d301ab40002ee/train/python

from math import gcd

def gcdi(x,y):
  return gcd(x, y)

def lcmu(a, b):
  return abs(a*b) // gcd(a, b)

def som(a, b):
  return a + b

def maxi(a, b):
  return max(a, b)

def mini(a, b):
  return min(a, b)

def oper_array(fct, arr, init): 
  retArray = []
  for i, item in enumerate(arr): retArray.append(fct(retArray[-1], item) if i != 0 else fct(init, item))
  return retArray

  

from TestFunction import Test
test = Test(None)

      
test.describe("Reducing by steps")
def testing(actual, expected):
  test.assert_equals(actual, expected)
test.it("basic tests gcdi, lcmu, som, mini, maxi")
a = [ 18, 69, -90, -78, 65, 40 ]
r = [ 18, 3, 3, 3, 1, 1 ]
op = oper_array(gcdi, a, a[0])
testing(op, r)
r = [ 18, 414, 2070, 26910, 26910, 107640 ]
op = oper_array(lcmu, a, a[0])
testing(op, r)
# r = [ 18, 87, -3, -81, -16, 24 ]
# op = oper_array(som, a, 0)
# testing(op, r)
# r = [ 18, 18, -90, -90, -90, -90 ]
# op = oper_array(mini, a, a[0])
# testing(op, r)
# r = [ 18, 69, 69, 69, 69, 69 ]
# op = oper_array(maxi, a, a[0])
# testing(op, r)

        
        
        