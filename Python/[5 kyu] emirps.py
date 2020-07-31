# see https://www.codewars.com/kata/55a29405bc7d2efaff00007c/train/python

from TestFunction import Test

def is_prime(num):
  if num % 2 == 0: return False
  for i in range(3, int(num**0.5+1), 2):
    if (num % i) == 0:
      return False
  else:
    return True        
  return False

def is_emrip(num):
  s = int(''.join([s for s in reversed(str(num))]))
  if s == num: return False
  return is_prime(s)

def primes(n):
  return [x for x in range(3, n, 2) if is_prime(x)]

def find_emirp(n):
  generator = set(primes(10**6))
  primes_ = [num for num in generator if num < n]
  emrips = [num for num in primes_ if is_emrip(num)]
  return [len(emrips), max(emrips) if emrips != [] else 0, sum(emrips)]


test = Test(None)
test.assert_equals(find_emirp(10), [0, 0, 0])
test.assert_equals(find_emirp(50), [4, 37, 98])
test.assert_equals(find_emirp(100), [8, 97, 418])
test.assert_equals(find_emirp(200), [15, 199, 1489])
test.assert_equals(find_emirp(500), [20, 389, 3232])
test.assert_equals(find_emirp(750), [25, 743, 6857])
test.assert_equals(find_emirp(915505), [9278, 915283, 3303565930])
test.assert_equals(find_emirp(530492), [6700, 399941, 1317845448])
