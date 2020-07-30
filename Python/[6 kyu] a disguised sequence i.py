# see https://www.codewars.com/kata/563f0c54a22b9345bf000053/solutions/python

from TestFunction import Test

"""def fcn(n):
  u_values = [1, 2]
  if n == 0: return 1
  if n == 1: return 2
  for i in range(n-2):
    u_next = (6*u_values[i]*u_values[i+1]) / (5*u_values[i] - u_values[i+1])
    u_values.append(u_next)
  print(u_values)
  return int(sum(u_values)+1)"""


def fcn(n):
  return sum([2**i for i in range(n)]) + 1

Test = Test(None)
Test.assert_equals(fcn(17), 131072)
Test.assert_equals(fcn(21), 2097152)
Test.assert_equals(fcn(14), 16384)
Test.assert_equals(fcn(43), 8796093022208)
Test.assert_equals(fcn(19), 524288)
