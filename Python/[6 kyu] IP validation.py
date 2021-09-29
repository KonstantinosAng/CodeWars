# see https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python

from TestFunction import Test

import re
def is_valid_IP(strng):
  digitsArray = strng.split(".") 
  if len(digitsArray) != 4: return False
  for number in digitsArray:
    if re.match('^[0-9]+$', number):
      if len(str(int(number))) != len(number): return False
      if 255 < int(number) or int(number) < 0:
        return False
    else:
      return False
  return True


Test = Test(None)
Test.describe("Basic tests")
Test.assert_equals(is_valid_IP('12.255.56.1'),     True)
Test.assert_equals(is_valid_IP(''),                False)
Test.assert_equals(is_valid_IP('abc.def.ghi.jkl'), False)
Test.assert_equals(is_valid_IP('123.456.789.0'),   False)
Test.assert_equals(is_valid_IP('12.34.56'),        False)
Test.assert_equals(is_valid_IP('12.34.56 .1'),     False)
Test.assert_equals(is_valid_IP('12.34.56.-1'),     False)
Test.assert_equals(is_valid_IP('123.045.067.089'), False)
Test.assert_equals(is_valid_IP('127.1.1.0'),        True)
Test.assert_equals(is_valid_IP('0.0.0.0'),          True)
Test.assert_equals(is_valid_IP('0.34.82.53'),       True)
Test.assert_equals(is_valid_IP('192.168.1.300'),   False)