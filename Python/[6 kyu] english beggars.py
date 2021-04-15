# see https://www.codewars.com/kata/59590976838112bfea0000fa/train/python

def beggars(values, n):
  if n == 0: return []
  start, ret, temp, counter = 0, [], [], 0
  while start < len(values):
    while counter < len(values):
      temp.append(values[counter])
      counter += n
    ret.append(sum(temp))
    temp = []
    start += 1
    counter = start
  while n > len(ret):
    ret.append(0)
  return ret[:n]
  

from TestFunction import Test
test = Test(None)
test.describe("Basic tests")
test.assert_equals(beggars([1,2,3,4,5],1),[15])
test.assert_equals(beggars([1,2,3,4,5],2),[9,6])
test.assert_equals(beggars([1,2,3,4,5],3),[5,7,3])
test.assert_equals(beggars([1,2,3,4,5],6),[1,2,3,4,5,0])
test.assert_equals(beggars([1,2,3,4,5],0),[])