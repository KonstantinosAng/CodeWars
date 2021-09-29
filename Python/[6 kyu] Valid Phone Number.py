# see https://www.codewars.com/kata/525f47c79f2f25a4db000025/train/python

from TestFunction import Test

import re
def valid_phone_number(phone_number):
  return bool(re.match('^[(][0-9]{3}[)][ ][0-9]{3}[-][0-9]{4}$', phone_number))

test = Test(None)
test.describe("Phone number validations")
test.it("Sample Tests")
test.assert_equals(valid_phone_number("(123) 456-7890"),       True)
test.assert_equals(valid_phone_number("(1111)555 2345"),       False)
test.assert_equals(valid_phone_number("(098) 123 4567"),       False)
test.assert_equals(valid_phone_number("(123)456-7890"),        False)
test.assert_equals(valid_phone_number("abc(123)456-7890"),     False)
test.assert_equals(valid_phone_number("(123)456-7890abc"),     False)
test.assert_equals(valid_phone_number("abc(123)456-7890abc"),  False)
test.assert_equals(valid_phone_number("abc(123) 456-7890"),    False)
test.assert_equals(valid_phone_number("(123) 456-7890abc"),    False)
test.assert_equals(valid_phone_number("abc(123) 456-7890abc"), False)
test.assert_equals(valid_phone_number("(333) 185-0594"),       True)