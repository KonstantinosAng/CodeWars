# see https://www.codewars.com/kata/539a0e4d85e3425cb0000a88/train/python

class Addition(int):
  def __call__(self, value):
    return Addition(self + value)

def add(n):
  return Addition(n)


from TestFunction import Test
test = Test(None)   

test.assert_equals(add(1), 1)
test.assert_equals(add(1)(2), 3)
test.assert_equals(add(1)(2)(3), 6)
