# see https://www.codewars.com/kata/55a29405bc7d2efaff00007c/train/python

from TestFunction import Test

from math import ceil

class Primes:
  @staticmethod
  def stream():
    limit = 15490000
    primes = [True]*limit
    for base in range(2, int(limit**0.5 + 1)):
      if primes[base]:
        primes[base*2:limit:base] = [False]*(ceil(limit / base) - 2)
    primes[0] = primes[1] = False
    p = (num for num, is_prime in enumerate(primes) if is_prime)
    for i in p:
      yield i

def is_prime(num):
  if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
          return False
    else:
      return True        
  else:
    return False

def is_emrip(num):
  s = int(''.join([s for s in reversed(str(num))]))
  if s == num: return False
  return is_prime(s)

"""def find_emirp(n):
  primes_count = []
  for i in range(1, n, 2):
    if is_prime(i) and is_emrip(i):
      primes_count.append(i)
  return [len(primes_count), max(primes_count) if primes_count != [] else 0, sum(primes_count)]
"""

def find_emirp(n):
  primes_sum = 0
  primes_max = 0
  primes_count = 0
  for prime in Primes().stream():
    if prime >= n: break
    if is_emrip(prime):
      primes_sum += prime
      primes_max = prime
      primes_count += 1
  return [primes_count, primes_max, primes_sum]

test = Test(None)
#test.assert_equals(find_emirp(10), [0, 0, 0])
#test.assert_equals(find_emirp(50), [4, 37, 98])
#test.assert_equals(find_emirp(100), [8, 97, 418])
#test.assert_equals(find_emirp(200), [15, 199, 1489])
#test.assert_equals(find_emirp(500), [20, 389, 3232])
#test.assert_equals(find_emirp(750), [25, 743, 6857])
test.assert_equals(find_emirp(915505), [9278, 915283, 3303565930])
test.assert_equals(find_emirp(530492), [6700, 399941, 1317845448])
