# see https://www.codewars.com/kata/582c01ad3fd1cc5736000348/train/python

import math
def make_matrix(m: int, n: int) -> str:
  halfTopArray = []
  halfBottomArray = []
  middleArray = []
  stringM = str(m)
  middle = math.floor(n/2)
  for i in range(middle):
    tempString = " ".join(x for x in stringM[3]*i + stringM[0] + stringM[1]*(n-2*(i+1)) + stringM[0] + stringM[4]*i)
    halfTopArray.append(tempString)
  for i in range(middle):
    tempString = " ".join(x for x in stringM[3]*i + stringM[0] + stringM[2]*(n-2*(i+1)) + stringM[0] + stringM[4]*i)
    halfBottomArray.append(tempString)
  halfBottomArray = [x for x in reversed(halfBottomArray)]
  middleArray = [" ".join(x for x in stringM[3]*middle + stringM[0] + stringM[4]*middle)]
  array = "\n".join(x for x in halfTopArray + middleArray + halfBottomArray)
  return array

    


from TestFunction import Test
test = Test(None)

test.describe("Sample tests")

test.it('Size 3')
result = "6 7 6\n" + \
        "9 6 0\n" + \
        "6 8 6"
case = (67890, 3)
test.assert_equals(
    make_matrix(*case),
    result,
    "Fail with code: {} and size: {}\n".format(*case))

test.it('Size 5')
result = "1 2 2 2 1\n" + \
        "4 1 2 1 5\n" + \
        "4 4 1 5 5\n" + \
        "4 1 3 1 5\n" + \
        "1 3 3 3 1"
case = (12345, 5)
test.assert_equals(
    make_matrix(*case),
    result,
    "Fail with code: {} and size: {}\n".format(*case)
)


test.it('Size 7')
result = "1 3 3 3 3 3 1\n" + \
        "7 1 3 3 3 1 9\n" + \
        "7 7 1 3 1 9 9\n" + \
        "7 7 7 1 9 9 9\n" + \
        "7 7 1 5 1 9 9\n" + \
        "7 1 5 5 5 1 9\n" + \
        "1 5 5 5 5 5 1"
case = (13579, 7)
test.assert_equals(
    make_matrix(*case),
    result,
    "Fail with code: {} and size: {}\n".format(*case)
)
