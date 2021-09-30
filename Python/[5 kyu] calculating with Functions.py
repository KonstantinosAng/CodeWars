# see https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
import types
def zero(*args, **kwargs):
  self_value = 0
  if not args: return self_value
  if isinstance(args, types.FunctionType):
    return
def one(*args, **kwargs):
  self_value = 1
def two(*args, **kwargs):
  self_value = 2
def three(*args, **kwargs):
  self_value = 3
def four(*args, **kwargs):
  self_value = 4
def five(*args, **kwargs):
  self_value = 5
def six(*args, **kwargs):
  self_value = 6
def seven(*args, **kwargs):
  self_value = 7
def eight(*args, **kwargs):
  self_value = 8
def nine(*args, **kwargs):
  self_value = 9
def plus(*args, **kwargs):
def minus(*args, **kwargs): #your code here
def times(*args, **kwargs): #your code here
def divided_by(*args, **kwargs): #your code here


from TestFunction import Test
test = Test(None)   
test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)
