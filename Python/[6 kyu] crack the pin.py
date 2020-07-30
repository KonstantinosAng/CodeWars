# see https://www.codewars.com/kata/5efae11e2d12df00331f91a6/solutions/python

from TestFunction import Test
import hashlib


def crack(hash):
  for i in range(0, 99999):
    pin = '0'*(5-len(str(i))) + str(i)
    guess = hashlib.md5(pin.encode()).hexdigest()
    if guess == hash:
      break
  return pin

test = Test(None)
test.assert_equals(crack("827ccb0eea8a706c4c34a16891f84e7b"), "12345")
test.assert_equals(crack("86aa400b65433b608a9db30070ec60cd"), "00078")
