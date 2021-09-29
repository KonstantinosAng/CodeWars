# see https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python

from TestFunction import Test

def even_or_odd(s):
  odd = 0
  even = 0
  for digit in s:
    if int(digit)%2 == 0: even += int(digit)
    else: odd += int(digit)
  if even > odd: return 'Even is greater than Odd'
  if even < odd: return 'Odd is greater than Even'
  return 'Even and Odd are the same'


test = Test(None)
test.it("Sample tests")
test.assert_equals(even_or_odd('12'), 'Even is greater than Odd')
test.assert_equals(even_or_odd('123'), 'Odd is greater than Even')
test.assert_equals(even_or_odd('112'), 'Even and Odd are the same')