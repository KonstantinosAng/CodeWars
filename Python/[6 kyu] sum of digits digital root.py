# see https://www.codewars.com/kata/541c8630095125aba6000c00/solutions/python

from TestFunction import Test

def digital_root(n):
  rv = str(n)
  while len(rv) != 1:
    rv = str(sum(int(x) for x in str(rv)))
  return int(rv)


Test = Test(None)
Test.assert_equals(digital_root(16), 7)
Test.assert_equals(digital_root(942), 6)
Test.assert_equals(digital_root(132189), 6)
Test.assert_equals(digital_root(493193), 2)