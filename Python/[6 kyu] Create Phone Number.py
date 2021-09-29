# see https://www.codewars.com/kata/525f50e3b73515a6db000b83/train/python

from TestFunction import Test

def create_phone_number(n):
  return f'({"".join(str(x) for x in n[:3])}) {"".join(str(x) for x in n[3:6])}-{"".join(str(x) for x in n[6:])}'
    

test = Test(None)
test.describe("Basic tests")
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
test.assert_equals(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
test.assert_equals(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
test.assert_equals(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")