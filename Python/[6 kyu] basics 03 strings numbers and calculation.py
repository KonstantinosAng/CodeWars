# see https://www.codewars.com/kata/56b5dc75d362eac53d000bc8/solutions/python

from TestFunction import Test

import string
def calculate_string(st):
  operations = '+-/*.'
  punctuation = ''.join([x for x in string.punctuation if x not in operations])
  letters = string.ascii_lowercase + punctuation + '§¿¡'
  st = ''.join([x for x in st if x.lower() not in letters])
  return str(int(round(eval(st))))

test = Test(None)
test.assert_equals(calculate_string(";$%§fsdfsd235??df/sdfgf5gh.000kk0000"), "47")
test.assert_equals(calculate_string("sdfsd23454sdf*2342"), "54929268")
test.assert_equals(calculate_string("fsdfsd235???34.4554s4234df-sdfgf2g3h4j442"), "-210908")
test.assert_equals(calculate_string("fsdfsd234.4554s4234df+sf234442"), "234676")
test.assert_equals(calculate_string("a1a2b3c.c0c/a1a0b.cc00c"), '12')