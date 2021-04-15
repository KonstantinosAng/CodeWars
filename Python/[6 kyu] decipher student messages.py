# see https://www.codewars.com/kata/5a1a144f8ba914bbe800003f/train/python

import math

def decipher_message(message):
  counter, ret = 0, ''
  while len(ret) < len(message):
    i = counter
    while i < len(message):
      ret += message[i]
      i += int(math.sqrt(len(message)))
    counter += 1
  return ret

from TestFunction import Test
test = Test(None)
test.it("Basic tests")
test.assert_equals(decipher_message('ArNran u rstm5twob  e ePb'), 'Answer to Number 5 Part b')
test.assert_equals(decipher_message('ArNran u rstm8twob  e ePc'), 'Answer to Number 8 Part c')
test.assert_equals(decipher_message('7660yyyay59y9y85'), '7yy96y5y6y980ay5')
test.assert_equals(decipher_message(' 5y7622a067 8y62'), ' 608526yy2767a 2')
test.assert_equals(decipher_message('9y98a877a95976a758726a89a5659957ya y'), '9777a5y762579aa66y897a5aa5589 89899y')