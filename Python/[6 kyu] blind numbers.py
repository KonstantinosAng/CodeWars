# see https://www.codewars.com/kata/5ee044344a543e001c1765b4/train/python
import re

def blind_number(n):
  ret = ['0'*(n-len(str(x)))+str(x) for x in range(10**n) if '00' not in '0'*(n-len(str(x)))+str(x)]
  count = 0
  for number in ret:
    if re.match('^[0-2]+$', number) and '00' not in number:
      count += 1
  return count


from TestFunction import Test
test = Test(None)
test.it("Basic tests")
test.assert_equals(blind_number(1), 3)
test.assert_equals(blind_number(2), 8)
test.assert_equals(blind_number(3), 22)
test.assert_equals(blind_number(5), 164)
test.assert_equals(blind_number(10), 24960)
test.assert_equals(blind_number(4680), 259339709)
test.assert_equals(blind_number(5841), 186405645)