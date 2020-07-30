# see https://www.codewars.com/kata/5592e3bd57b64d00f3000047/solutions/python

from TestFunction import Test

def find_nb(m):
  _sum = 0
  for i in range(1, m):
    _sum += i**3 
    if _sum == m:
      return i
    if _sum > m:
      return -1


test = Test(None)
test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)

