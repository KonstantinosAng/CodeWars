# see https://www.codewars.com/kata/5f77d62851f6bc0033616bd8/train/python

from TestFunction import Test


def valid_spacing(s):
  return s.count(' ') == len([s for s in s.split(" ") if s != ''])-1 if s != "" else True


test = Test(None)
test.describe('Sample Tests')
test.assert_equals(valid_spacing('Hello world'), True)
test.assert_equals(valid_spacing(' Hello world'), False)
test.assert_equals(valid_spacing('Hello  world '), False)
test.assert_equals(valid_spacing('Hello'), True)
test.assert_equals(valid_spacing('Helloworld'), True)
