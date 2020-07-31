# see https://www.codewars.com/kata/55a29405bc7d2efaff00007c/train/python

from TestFunction import Test

from math import factorial
from decimal import localcontext

"""def going(n):
  with localcontext() as ctx:
    ctx.prec = 32  # desired precision
    upper = 1/factorial(n)
    down = sum([factorial(i) for i in range(1, n+1)])
    #print(upper, down)
    rv = str(upper*down)
    integer, decimals = rv.split(".")
    if len(decimals) >= 6:
      return float('.'.join([integer, decimals[:6]]))
    else:
      return float(rv)"""

def going(n):  
    s = 1.0
    for i in range(2, n + 1):
        s = s/i + 1
    return int(s * 1e6) / 1e6

test = Test(None)
test.assert_equals(going(5), 1.275)
test.assert_equals(going(6), 1.2125)
test.assert_equals(going(7), 1.173214)
test.assert_equals(going(8), 1.146651)
test.assert_equals(going(20), 1.052786)
test.assert_equals(going(50), 1.020416)
test.assert_equals(going(10110), 1.000098)
