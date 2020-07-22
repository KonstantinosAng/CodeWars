# see https://www.codewars.com/kata/58a5aeb893b79949eb0000f1/solutions/python

from TestFunction import Test

def shared_bits(a, b):
  a, b, count = bin(a).replace("0b", ""), bin(b).replace("0b", ""), 0
  if len(a) < len(b):
    while len(a) < len(b):
     a = "0" + a
  elif len(a) > len(b):
    while len(b) < len(a): 
      b = "0" + b
  else:
    pass
  print(a, b)
  for digit1, digit2 in zip(a, b):
    if digit1 == digit2 and digit1 == "1": 
      count += 1
    if count >= 2: return True
  return False


Test(False).assert_result(shared_bits(1, 2))
Test(False).assert_result(shared_bits(16, 8))
Test(False).assert_result(shared_bits(1, 1))
Test(False).assert_result(shared_bits(2, 3))
Test(False).assert_result(shared_bits(7, 10))
Test(True).assert_result(shared_bits(43, 77))
Test(True).assert_result(shared_bits(7, 15))
Test(True).assert_result(shared_bits(23, 7))