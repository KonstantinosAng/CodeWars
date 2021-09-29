# see https://www.codewars.com/kata/5274e122fc75c0943d000148/train/python

from TestFunction import Test

def group_by_commas(n):
  pass



test = Test(None)
test.assert_equals(group_by_commas(1), '1')
test.assert_equals(group_by_commas(10), '10')
test.assert_equals(group_by_commas(100), '100')
test.assert_equals(group_by_commas(1000), '1,000')
test.assert_equals(group_by_commas(10000), '10,000')
test.assert_equals(group_by_commas(100000), '100,000')
test.assert_equals(group_by_commas(1000000), '1,000,000')
test.assert_equals(group_by_commas(35235235), '35,235,235')