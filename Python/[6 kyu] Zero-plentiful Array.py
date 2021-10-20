# see https://www.codewars.com/kata/59e270da7997cba3d3000041/train/python

def zero_plentiful(arr):
  if 0 in arr:
    pointer = 0
    length = 0
    count = 0
    while pointer < len(arr):
      if arr[pointer] == 0:
        length += 1
      else:
        if length >= 4:
          count += 1
          length = 0
        else:
          if length > 0: return 0
      pointer += 1
    if length < 4 and length > 0: return 0
    return count if arr[-1] != 0 else count + 1
  return 0
  

from TestFunction import Test
test = Test(None)

test.it("Basic tests")
test.assert_equals(zero_plentiful([3]),0);
test.assert_equals(zero_plentiful([0,0,0,0,0,0]),1);
[1, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0]