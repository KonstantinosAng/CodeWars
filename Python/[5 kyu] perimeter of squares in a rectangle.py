# see https://www.codewars.com/kata/559a28007caad2ac4e000083/solutions/python

fibonacci_cache = {}

def fib(n):
  if n in fibonacci_cache:
     return fibonacci_cache[n]
  if n == 1: return 0
  if n == 2: return 1
  else: 
    value = fib(n-1) + fib(n-2)
    fibonacci_cache[n] = value
    return value

def perimeter(n):
  n_fib = [fib(i) for i in range(1, n+3)]
  return 4*sum([x for x in n_fib])

from TestFunction import Test
test = Test(None)
test.assert_equals(perimeter(5), 80)
test.assert_equals(perimeter(7), 216)
test.assert_equals(perimeter(20), 114624)
test.assert_equals(perimeter(30), 14098308)
test.assert_equals(perimeter(100), 6002082144827584333104)
