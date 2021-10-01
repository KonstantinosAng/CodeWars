# see https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

import types
def zero(*args, **kwargs):
  self_value = 0
  if not args: return self_value
  return evaluate(self_value, args[0])

def one(*args, **kwargs):
  self_value = 1
  if not args: return self_value
  return evaluate(self_value, args[0])

def two(*args, **kwargs):
  self_value = 2
  if not args: return self_value
  return evaluate(self_value, args[0])

def three(*args, **kwargs):
  self_value = 3
  if not args: return self_value
  return evaluate(self_value, args[0])

def four(*args, **kwargs):
  self_value = 4
  if not args: return self_value
  return evaluate(self_value, args[0])

def five(*args, **kwargs):
  self_value = 5
  if not args: return self_value
  return evaluate(self_value, args[0])

def six(*args, **kwargs):
  self_value = 6
  if not args: return self_value
  return evaluate(self_value, args[0])

def seven(*args, **kwargs):
  self_value = 7
  if not args: return self_value
  return evaluate(self_value, args[0])

def eight(*args, **kwargs):
  self_value = 8
  if not args: return self_value
  return evaluate(self_value, args[0])

def nine(*args, **kwargs):
  self_value = 9
  if not args: return self_value
  return evaluate(self_value, args[0])

def plus(*args, **kwargs):
  if args and (isinstance(args[0], int) or isinstance(args[0], float)): return '+' + str(args[0])
  
def minus(*args, **kwargs): #your code here
  if args and (isinstance(args[0], int) or isinstance(args[0], float)): return '-' + str(args[0])

def times(*args, **kwargs): #your code here
  if args and (isinstance(args[0], int) or isinstance(args[0], float)):
    return '*' + str(args[0])

def divided_by(*args, **kwargs): #your code here
  if args and (isinstance(args[0], int) or isinstance(args[0], float)): return '/' + str(args[0])

def evaluate(*args, **kwargs):
  if args:
    operator = args[1][0]
    if operator == '*': return float(args[0]) * float(args[1][1:])
    if operator == '/': return int(float(args[0]) / float(args[1][1:]))
    if operator == '+': return float(args[0]) + float(args[1][1:])
    if operator == '-': return float(args[0]) - float(args[1][1:])


from TestFunction import Test
test = Test(None)   
test.describe('Basic Tests')
test.assert_equals(seven(times(five())), 35)
test.assert_equals(four(plus(nine())), 13)
test.assert_equals(eight(minus(three())), 5)
test.assert_equals(six(divided_by(two())), 3)
