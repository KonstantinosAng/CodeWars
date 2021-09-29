# see https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/python

from TestFunction import Test

def fold(arr):
  if len(arr) % 2 == 0:
    pass
  else:
    pass

def fold_array(array, runs):
  for i in range(runs):
    arr = fold(array)
  pass

test = Test(None)
arr = [1, 2, 3, 4, 5]

tests = [
  [[arr, 1], [6, 6, 3]],
  [[arr, 2], [9, 6]],
  [[arr, 3], [15]],
  [[[-9, 9, -8, 8, 66, 23], 1], [14, 75, 0]],
]

for inp, exp in tests:
  test.assert_equals(fold_array(*inp), exp)