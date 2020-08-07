# see https://www.codewars.com/kata/5aa39ba75084d7cf45000008

fib = {}
def solve(n):
  if n in fib: 
    return fib[n]
  else:
    if n == 0: 
      value = '0'
    elif n == 1: 
      value = '01'
    else:
      value = solve(n-1) + solve(n-2)
      fib[n] = value
  return value

from TestFunction import Test
Test = Test(None)
Test.it("Basic tests")
Test.assert_equals(solve(0),'0')
Test.assert_equals(solve(1),'01')
Test.assert_equals(solve(2),'010')
Test.assert_equals(solve(3),'01001')
Test.assert_equals(solve(5),'0100101001001')