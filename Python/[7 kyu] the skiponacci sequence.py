# see https://www.codewars.com/kata/580777ee2e14accd9f000165/train/python

memo = {}
def fib(n):
  if n in memo:
    value = memo[n]
  else:
    if n <= 1:
      value = 1
    else: 
      value = fib(n-1) + fib(n-2)
      memo[n] = value
  return value

def skiponacci(n):
  return ' '.join([str(fib(i)) if i%2 == 0 else 'skip' for i in range(n)])

from TestFunction import Test
Test = Test(None)
Test.assert_equals(skiponacci(1), "1")
Test.assert_equals(skiponacci(5), "1 skip 2 skip 5")
Test.assert_equals(skiponacci(7), "1 skip 2 skip 5 skip 13")