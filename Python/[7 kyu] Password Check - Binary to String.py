# see https://www.codewars.com/kata/5a731b36e19d14400f000c19/train/python

def decode_pass(pass_list, bits):
  stringPassword = "".join(chr(int(x, 2)) for x in bits.split(" "))
  if stringPassword in pass_list: return stringPassword
  return False

from TestFunction import Test
test = Test(None)   
test.describe("Fixed Tests")
test.it("Tests")
test.assert_equals(decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'), 'password123');
test.assert_equals(decode_pass(['password321', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'), False);
test.assert_equals(decode_pass(['password456', 'pass1', 'test12'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'), False);