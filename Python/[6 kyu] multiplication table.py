# see https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/solutions/python

from TestFunction import Test

def multiplication_table(size):
  rv = []
  k = 0
  for i in range(size):
    s = 0
    k += 1
    temp = []
    for j in range(size):
      s += k
      temp.append(s)
    rv.append(temp)
  return rv

test = Test(None)
test.describe("Basic Tests")
test.it("Should pass basic tests")
test.assert_equals(multiplication_table(3), [[1,2,3],[2,4,6],[3,6,9]])
