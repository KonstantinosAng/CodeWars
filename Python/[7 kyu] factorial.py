# see https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python

from TestFunction import Test


def factorial(n):
  s = 1
  for i in range(1, n+1):
    s*=i
  return s

test = Test(None)
test.describe("Fixed Tests")
test.it('Basic Test Cases')
tests = (
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
)

for t in tests:
    inp, exp = t
    test.assert_equals(factorial(inp), exp)
