# see https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

from time import time


def increment_string(s):
  if s == "" or not s[-1].isdigit(): return s + '1'
  start = len(s) - 1
  while s[start:].isdigit():
    digits = s[start:]
    start -= 1
  word = s[:len(s)-len(digits)]
  increment = str(int(digits)+1)
  diff = len(digits)-len(increment)
  newIncrement= "".join([digits[:diff]if diff>=0 else"", increment])
  return "".join([word, newIncrement])


# def increment_string(strng):
  
#   # strip the decimals from the right
#   stripped = strng.rstrip('1234567890')
  
#   # get the part of strng that was stripped
#   ints = strng[len(stripped):]
  
#   if len(ints) == 0:
#       return strng + '1'
#   else:
#       # find the length of ints
#       length = len(ints)
  
#       # add 1 to ints
#       new_ints = 1 + int(ints)
  
#       # pad new_ints with zeroes on the left
#       new_ints = str(new_ints).zfill(length)
  
#       return stripped + new_ints


from TestFunction import Test
test = Test(None)   
test.assert_equals(increment_string("foo"), "foo1")
test.assert_equals(increment_string("foobar001"), "foobar002")
test.assert_equals(increment_string("foobar1"), "foobar2")
test.assert_equals(increment_string("foobar00"), "foobar01")
test.assert_equals(increment_string("foobar99"), "foobar100")
test.assert_equals(increment_string("foobar099"), "foobar100")
test.assert_equals(increment_string(""), "1")
start_time = time()
test.assert_equals(increment_string(">*12=4180288e]d%173035337\\]@jB5L~41V7`V28343r)z{I)*V@4130993Z59D%16TP957231007"), ">*12=4180288e]d%173035337\\]@jB5L~41V7`V28343r)z{I)*V@4130993Z59D%16TP957231008")
print(time() - start_time)
start_time = time()
test.assert_equals(increment_string("c]|v885710I51737587}El~E/eX29290419+SB2188090tbM<X9*014410445PV[8P~33a1650504KL{{247430xx85000000003516"), "c]|v885710I51737587}El~E/eX29290419+SB2188090tbM<X9*014410445PV[8P~33a1650504KL{{247430xx85000000003517")
print(time() - start_time)
start_time = time()
test.assert_equals(increment_string('5w47054727^*/SZi$bM86819qm"(/Yf>&RLZ^)3399352z4cuA|WUq051234SK~KUJ-n~1s~kEXEb4000000000048599'), '5w47054727^*/SZi$bM86819qm"(/Yf>&RLZ^)3399352z4cuA|WUq051234SK~KUJ-n~1s~kEXEb4000000000048600')
print(time() - start_time)
