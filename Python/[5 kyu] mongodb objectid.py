# see https://www.codewars.com/kata/52fefe6cb0091856db00030e/solutions/python

from TestFunction import Test

from datetime import datetime
import re

class Mongo(object):

  @classmethod
  def is_valid(cls, s):
    if type(s) == str:
      if len(s) != 24: return False
      if re.compile("^[0-9a-f]+$").match(s): return True
    return False
  
  @classmethod
  def get_timestamp(cls, s):
    if type(s) == str:
      if len(s) != 24: return False
      if re.compile("^[0-9a-f]+$").match(s):
        d = int(s[:8], 16)
        return datetime.fromtimestamp(d) 
    return False

test = Test(None)
from datetime import datetime

test.assert_equals(Mongo.is_valid(False), False)
test.assert_equals(Mongo.is_valid([]), False)
test.assert_equals(Mongo.is_valid(1234), False)
test.assert_equals(Mongo.is_valid('123476sd'), False)
test.assert_equals(Mongo.is_valid('507f1f77bcf86cd79943901'), False)
test.assert_equals(Mongo.is_valid('507f1f77bcf86cd799439016'), True)
test.assert_equals(Mongo.is_valid('d07f1f77bcf86c!799439016'), False)
test.assert_equals(Mongo.is_valid('507f1f77bcF86cd799439011'), False)

test.assert_equals(Mongo.get_timestamp(False), False)
test.assert_equals(Mongo.get_timestamp([]), False)
test.assert_equals(Mongo.get_timestamp(1234), False)
test.assert_equals(Mongo.get_timestamp('123476sd'), False)
test.assert_equals(Mongo.get_timestamp('507f1f77bcf86cd79943901'), False)
test.assert_equals(Mongo.get_timestamp('d07f1f77bcf86FF799439016'), False)
