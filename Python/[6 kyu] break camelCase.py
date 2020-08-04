# see 

from TestFunction import Test


def solution(s):
  uppercase = [i for i, x in enumerate(s) if x.isupper()] 
  return ' '.join([s[:i] for i in uppercase])
    

Test = Test(None)
Test.assert_equals(solution("helloWorld"), "hello World")
Test.assert_equals(solution("camelCase"), "camel Case")
Test.assert_equals(solution("breakCamelCase"), "break Camel Case")
