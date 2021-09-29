# see https://www.codewars.com/kata/5dad6e5264e25a001918a1fc

from TestFunction import Test

def pyramid(n):
  if n == 0: return []
  ret = []
  for i in range(1, n+1):
    ret.append([1 for j in range(i)])
  return ret

test = Test(None)
test.describe('Sample Tests')
test.assert_equals(pyramid(0), [])
test.assert_equals(pyramid(1), [[1]])
test.assert_equals(pyramid(2), [[1], [1, 1]])
test.assert_equals(pyramid(3), [[1], [1, 1], [1, 1, 1]])