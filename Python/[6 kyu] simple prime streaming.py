# see https://www.codewars.com/kata/5a908da30025e995880000e3/solutions/python

from TestFunction import Test

def prime_series(number):
  is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
  ret = ''
  for n in range(2, number):
    if is_prime(n) == True:
      ret += str(n)      
  return ret               

def solve(a, b):
    c = prime_series(round((a + b)*2.12))
    return c[a:a+b]

Test = Test(None)
Test.assert_equals(solve(2,2),'57')
Test.assert_equals(solve(10,3),'192')
Test.assert_equals(solve(20,9),'414347535')
Test.assert_equals(solve(30,12),'616771737983')
Test.assert_equals(solve(40,8),'83899710')
Test.assert_equals(solve(50,6),'031071')
Test.assert_equals(solve(10000,5),'02192')
Test.assert_equals(solve(20000,5),'09334')
