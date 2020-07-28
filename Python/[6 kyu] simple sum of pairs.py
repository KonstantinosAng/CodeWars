# see https://www.codewars.com/kata/5bc027fccd4ec86c840000b7/solutions

from TestFunction import Test
import time

def solve(n):
  if n%2 == 0:
    a, b = n//2, n//2
  else:
    a, b = n//2, n//2 + 1
  max_sum = 0
  count = 0
  while a >= 0:
    if a + b == n:
      _sum = sum([int(digit) for digit in str(a)]) + sum([int(digit) for digit in str(b)])
      if _sum >= max_sum:
        max_sum = _sum
    a -= 1
    b += 1
    count += 1
    if count >= 3**len(str(n)):
      break
  return max_sum

def solve(n):
    if n < 10:
        return n
    a = int((len(str(n)) - 1) * '9')
    b = n - a
    return sum([int(i) for i in (list(str(a)) + list(str(b)))])


Test = Test(None)
Test.assert_equals(solve(18),18)
Test.assert_equals(solve(0),0)
Test.assert_equals(solve(29),11)
Test.assert_equals(solve(45),18)
Test.assert_equals(solve(1140),33)
Test.assert_equals(solve(7019),35)
Test.assert_equals(solve(15569047737), 144)
Test.assert_equals(solve(2452148459), 116)