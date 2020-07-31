# see 

from TestFunction import Test

from math import factorial

def going(n):
  upper = 1/factorial(n)
  down = sum([factorial(i) for i in range(1, n+1)])
  rv = "%.6f" % upper*down
  while rv[-1] == '0':
    rv = rv[:-1]
  return f'{rv}'
    

test = Test(None)
test.assert_equals(going(5), 1.275)
test.assert_equals(going(6), 1.2125)
test.assert_equals(going(7), 1.173214)
