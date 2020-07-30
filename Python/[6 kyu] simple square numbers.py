# see https://www.codewars.com/kata/5edc8c53d7cede0032eb6029/solutions

from TestFunction import Test
from math import sqrt

"""def solve(n):
  is_perfect_square = lambda number: int(sqrt(number) + 0.5) ** 2 == number
  for i in range(1, 10**(len(str(n))+3)):
    if is_perfect_square((n + i)) and is_perfect_square(i):
      return i
  return -1"""

def solve(n):
  for i in range(int(n**0.5), 0, -1):
    x = n - i**2
    if x > 0 and x % (2*i) == 0:
      return ((n - i ** 2) // (2 * i)) ** 2
  return -1

test = Test(None)
test.assert_equals(solve(1),-1)
test.assert_equals(solve(2),-1)
test.assert_equals(solve(3),1)
test.assert_equals(solve(4),-1)
test.assert_equals(solve(5),4)
test.assert_equals(solve(7),9)
test.assert_equals(solve(8),1)    
test.assert_equals(solve(9),16)
test.assert_equals(solve(10),-1)
test.assert_equals(solve(11),25)
test.assert_equals(solve(13),36)
test.assert_equals(solve(17),64)
test.assert_equals(solve(88901),5428900)
test.assert_equals(solve(290101),429235524)
