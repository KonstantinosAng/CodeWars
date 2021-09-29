# see https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

from TestFunction import Test

def unique_in_order(iterable):
  pointer = 0
  iterable = [x for x in iterable]
  while pointer < len(iterable) - 1:
    if iterable[pointer] == iterable[pointer+1]:
      iterable.pop(pointer + 1)
    else:
      pointer += 1
  return iterable

test = Test(None)
test.assert_equals(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
