# see

from TestFunction import Test

def is_prime(num):
  if num % 2 == 0: return False
  for i in range(3, int(num**0.5+1), 2):
    if (num % i) == 0:
      return False
  else:
    return True        
  return False

def generator_primes(n):
  yield 2
  for x in range(3, n, 2):
    if is_prime(x):
      yield x

def solve(a, b):
  prime_indexed = 0
  primes = []
  gen = generator_primes(450000)
  for prime in gen:
    primes.append(prime)
    if prime >= b: break
    if prime >= a and len(primes) in primes:
      prime_indexed += prime
  return prime_indexed


Test = Test(None)
Test.assert_equals(solve(0,10),8)
Test.assert_equals(solve(2,200),1080)
Test.assert_equals(solve(200,2000),48132)
Test.assert_equals(solve(500,10000),847039)
Test.assert_equals(solve(4000,450000),806250440)
