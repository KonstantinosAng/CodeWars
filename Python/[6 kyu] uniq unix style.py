# see https://www.codewars.com/kata/52249faee9abb9cefa0001ee/solutions/python

from TestFunction import Test

def uniq(seq): 
  i = 0
  while i != len(seq) - 1:
    if seq == []: break
    if i == len(seq) - 1: break
    if seq[i] == seq[i+1]: del seq[i+1]
    else:
      i += 1
  return seq

test = Test(None)
test.assert_equals(uniq(['a','a','b','b','c','a','b','c','c']), ['a','b','c','a','b','c'])
test.assert_equals(uniq(['a','a','a','b','b','b','c','c','c']), ['a','b','c'])
test.assert_equals(uniq([]), [])
test.assert_equals(uniq(['foo']), ['foo'])
test.assert_equals(uniq(['bar']), ['bar'])
test.assert_equals(uniq(['']), [''])
test.assert_equals(uniq([None,'a','a']), [None,'a'])
