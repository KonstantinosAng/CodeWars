# see https://www.codewars.com/kata/5906436806d25f846400009b/train/python

# -*- coding: utf-8 -*-
import math
def x(n):
  retArray = []
  iterations = math.floor(n/2)
  for i in range(iterations+1):
    row = ['□' if j != i and j!=n-1-i else "■" for j in range(n)]
    retArray.append("".join(x for x in row))
  return "\n".join(x for x in retArray + [x for x in reversed(retArray[:-1])])


from TestFunction import Test
test = Test(None)

# -*- coding: utf-8 -*-
test.describe("Default test cases")
test.it("Should work for test cases")
test.assert_equals(x(3), "■□■\n□■□\n■□■", "Should look like this: \n■□■\n□■□\n■□■")
test.assert_equals(x(7), "■□□□□□■\n□■□□□■□\n□□■□■□□\n□□□■□□□\n□□■□■□□\n□■□□□■□\n■□□□□□■", "Should look like this: \n■□□□□□■\n□■□□□■□\n□□■□■□□\n□□□■□□□\n□□■□■□□\n□■□□□■□\n■□□□□□■")
