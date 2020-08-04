# see https://www.codewars.com/kata/5208f99aee097e6552000148/solutions/python

from TestFunction import Test


def solution(s):
  indexes = [0] + [i for i, x in enumerate(s) if x.isupper()] 
  return ' '.join([s[indexes[i]:indexes[i+1]] for i in range(len(indexes) - 1)]) + ' ' + s[indexes[-1]:]
  

Test = Test(None)
Test.assert_equals(solution("helloWorld"), "hello World")
Test.assert_equals(solution("camelCase"), "camel Case")
Test.assert_equals(solution("breakCamelCase"), "break Camel Case")
