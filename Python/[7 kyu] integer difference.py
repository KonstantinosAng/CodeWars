# see https://www.codewars.com/kata/57741d8f10a0a66915000001/train/python


def int_diff(lst, n):
  i, rv = 0, 0
  while i < len(lst):
    for number in range(i+1, len(lst)):
      if abs(lst[number] - lst[i]) == n: rv += 1
    i += 1
  return rv


from TestFunction import Test
Test = Test(None)
Test.assert_equals(int_diff([1, 1, 5, 6, 9, 16, 27], 4), 3)
Test.assert_equals(int_diff([1, 1, 3, 3], 2), 4)
