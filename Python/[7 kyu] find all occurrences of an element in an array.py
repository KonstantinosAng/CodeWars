# see https://www.codewars.com/kata/59a9919107157a45220000e1/train/python

def find_all(array, n):
  return [index for index, number in enumerate(array) if number == n]

from TestFunction import Test
test = Test(None)
test.assert_equals(find_all([6, 9, 3, 4, 3, 82, 11], 3), [2, 4])
test.assert_equals(find_all([10, 16, 20, 6, 14, 11, 20, 2, 17, 16, 14], 16), [1, 9])
test.assert_equals(find_all([20, 20, 10, 13, 15, 2, 7, 2, 20, 3, 18, 2, 3, 2, 16, 10, 9, 9, 7, 5, 15, 5], 20), [0, 1, 8])
