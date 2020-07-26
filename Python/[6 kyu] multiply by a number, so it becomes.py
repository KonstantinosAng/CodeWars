# see https://www.codewars.com/kata/566be96bb3174e155300001b/solutions/python

from TestFunction import Test
from time import time

def mul_power(n, k):
  start_time = time()
  if n%2 == 0: start = 2
  else: start = 1
  is_perfect = lambda x, power: int(round(abs(x) ** (1. / power))) ** power == abs(x)
  if is_perfect(n, k):
      return 1
  for i in range(start, 10**22, 2):
    if is_perfect(i*n, k):
      print(f"Time {time() - start_time}")
      return i
  return False

Test = Test(None)
Test.assert_equals(mul_power(100, 3), 10)
Test.assert_equals(mul_power(36, 2), 1)
Test.assert_equals(mul_power(72, 4), 18)
Test.assert_equals(mul_power(1152, 3), 12)
Test.assert_equals(mul_power(115520, 8), 14701837812500)
Test.assert_equals(mul_power(194338 , 5), 1426365795268985963536)
Test.assert_equals(mul_power(525622, 5), 76329802314912560029456)
