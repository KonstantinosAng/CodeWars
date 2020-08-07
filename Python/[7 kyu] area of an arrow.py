# see https://www.codewars.com/kata/589478160c0f8a40870000bc/train/python

def arrow_area(a, b):
  return (1/2)*a*(b/2)


from TestFunction import Test
test = Test(None)
test.describe("Example Tests")
test.assert_equals(arrow_area(4,2), 2)
test.assert_equals(arrow_area(7,6), 10.5)
test.assert_equals(arrow_area(25,25), 156.25)