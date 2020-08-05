# see https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/solutions/python

from TestFunction import Test

def duplicate_encode(word):
  word = word.lower() ; rv = ''
  for x in word:
    if word.count(x) == 1:
      rv += '('
    else:
      rv += ')'
  return rv

Test = Test(None)

Test.assert_equals(duplicate_encode("din"),"(((")
Test.assert_equals(duplicate_encode("recede"),"()()()")
Test.assert_equals(duplicate_encode("Success"),")())())","should ignore case")
Test.assert_equals(duplicate_encode("(( @"),"))((")