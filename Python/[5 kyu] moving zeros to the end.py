# see https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(array):
  i, zeroes = 0, 0
  while i < len(array):
    if array[i] == 0:
      array.pop(i)
      zeroes += 1
      continue
    i += 1
  return array+[int(x) for x in '0'*zeroes]


from TestFunction import Test

test = Test(None)
test.assert_equals(move_zeros([1, 2, 0, 2, 3, 5, 0, 0, 2, 0, 5]), [1, 2, 2, 3, 5, 2, 5, 0, 0, 0, 0])
test.assert_equals(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]), [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
test.assert_equals(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]), [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
test.assert_equals(move_zeros([0, 0]), [0, 0])
test.assert_equals(move_zeros([0]), [0])
test.assert_equals(move_zeros([]), [])
