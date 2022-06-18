# see https://www.codewars.com/kata/5877e7d568909e5ff90017e6/train/python

from TestFunction import Test

def find_ascending(d, start=1):
  if d == 1:
    for x in range(start, 10):
      yield [x]
  else:
    for x in range(start, 10):
      for y in find_ascending(d - 1, x):
        yield [x] + y

def find_all(sum_dig, digs):
  numbers = [x for x in find_ascending(digs) if sum(x) == sum_dig]
  if not numbers: return []  
  return [len(numbers), int("".join(map(str, numbers[0]))), int("".join(map(str, numbers[-1])))]



test = Test(None)
test.describe("Example Tests")
test.assert_equals(find_all(10, 3), [8, 118, 334])
test.assert_equals(find_all(9, 2), [4, 18, 45])
test.assert_equals(find_all(27, 3), [1, 999, 999])
test.assert_equals(find_all(84, 4), [])
test.assert_equals(find_all(35, 6), [123, 116999, 566666])