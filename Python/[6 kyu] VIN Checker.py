# see https://www.codewars.com/kata/60a54750138eac0031eb98e1/train/python

from TestFunction import Test

def check_vin(number):
  if 'I' in number or 'O' in number or 'Q' in number: return False
  if len(number) != 17: return False
  letterMap = {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'G': '7', 'H': '8', 'J': '1', 'K': '2', 'L': '3', 'M': '4', 'N': '5', 'P': '7', 'R': '9', 'S': '2', 'T': '3', 'U': '4', 'V': '5', 'W': '6', 'X': '7', 'Y': '8', 'Z': '9'}
  weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2] 
  ret = ""
  for digit in number:
    digit = digit.upper()
    if digit.isalpha():
      ret += letterMap[digit]
    else:
      ret += digit
  sums = []
  for digit, weight in zip(ret, weights):
    sums.append(int(digit)*weight)
  sums = sum(sums)
  mod = 'X' if str(sums % 11) == '10' else str(sums % 11)
  return True if mod == number[8] else False

    

test = Test(None)
test.describe("Tests") 
test.it("Fixed Tests")
test.assert_equals(check_vin("5YJ3E1EA7HF000337"), True)
test.assert_equals(check_vin("5YJ3E1EAXHF000347"), True)
test.assert_equals(check_vin("5VGYMVUX7JV764512"), True)
test.assert_equals(check_vin("7WDMMTDV9TG739741"), False)
test.assert_equals(check_vin("7JTRH08L5EJ234829"), False)
