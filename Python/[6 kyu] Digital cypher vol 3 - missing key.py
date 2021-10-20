# see https://www.codewars.com/kata/5930d8a4b8c2d9e11500002a/train/python

import math
def find_the_key(message, code):
  digits = [ord(x) - 96 for x in message]
  diff = [a - b for a, b in zip(code, digits)]
  strDiff = "".join(str(x) for x in diff)
  # print(digits, diff, strDiff)
  pointer = 1
  if strDiff.count(strDiff[0]) == len(strDiff): return int(strDiff[0])
  while pointer < math.floor(len(strDiff) / 2) + 1:
    subString = strDiff[:pointer]
    # print(subString, strDiff[pointer:pointer+len(subString)])
    if subString == strDiff[pointer:pointer+len(subString)] and pointer > 1: return int(subString)
    pointer += 1
  pointer = 1
  while pointer < len(strDiff):
    count = strDiff.count(strDiff[0:pointer]) 
    # print(count)
    if count == 1:
      retString = strDiff[pointer:].index(strDiff[0])
      # print(pointer, pointer + retString)
      return int(strDiff[:pointer + retString])
    pointer += 1
    
    
  

from TestFunction import Test
test = Test(None)

test.assert_equals(find_the_key("scout", [20, 12, 18, 30, 21]), 1939)
test.assert_equals(find_the_key("scoutc", [20, 12, 18, 30, 21, 12]), 1939)
test.assert_equals(find_the_key("scoutco", [20, 12, 18, 30, 21, 12, 18]), 1939)
test.assert_equals(find_the_key("masterpiece", [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8]), 1939)
test.assert_equals(find_the_key("nomoretears", [15, 17, 14, 17, 19, 7, 21, 7, 2, 20, 20]), 12)
test.assert_equals(find_the_key("tenthousand", [21, 5, 14, 20, 8, 16, 21, 19, 1, 14, 5]), 10000)
test.assert_equals(find_the_key("wouldgiveonedifferentown", [32, 24, 29, 13, 13, 16, 17, 23, 14, 24, 22, 6, 13, 18, 14, 7, 14, 27, 13, 15, 29, 24, 31, 15]), 9981)
test.assert_equals(find_the_key("firstchildfeellarge", [13, 16, 21, 25, 27, 10, 11, 15, 19, 11, 9, 11, 12, 19, 15, 7, 25, 14, 8]), 7736)