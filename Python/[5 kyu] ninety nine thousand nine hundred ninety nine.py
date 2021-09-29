# see https://www.codewars.com/kata/57f7b8271e3d9283300000b4/train/python

from TestFunction import Test

one = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
specials = {"10": "ten", '11': "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen", "19": "nineteen"}
twos = {"2": "twenty", "3": "thirty", "4": "forty", "5": "fifty", "6": "sixty", "7": "seventy", "8": "eighty", "9": "ninety"}
threes = "hundred"
fours = "thousand"

def parse_two_digits(n):
  if n[0] == '0':
    if n[1] == '0':
      return ''
    else:
      return one[n[1]]
  if n[0] == '1':
    return specials[n]
  else:
    if n[1] == '0':
      return twos[n[0]]
    else:
      return " ".join([twos[n[0]], one[n[1]]]).strip()

def parse_three_digits(n):
  if n[0] == '0': return parse_two_digits(n[1:])
  return " ".join([one[n[0]], threes, parse_two_digits(n[1:])]).strip()

def parse_four_digits(n):
  return " ".join([one[n[0]], fours, parse_three_digits(n[1:])]).strip()

def parse_five_digits(n):
  return " ".join([parse_two_digits(n[:2]), fours, parse_three_digits(n[2:])]).strip()

def number_to_english(n):
  if n > 99999: return ''
  if n < 0: return ''
  if type(n) == float: return ''
  n = str(n)
  if len(n) == 1: 
    return one[n]
  elif len(n) == 2: 
    return parse_two_digits(n)
  elif len(n) == 3:
    return parse_three_digits(n)
  elif len(n) == 4:
    return parse_four_digits(n)
  else: 
    return parse_five_digits(n)



test = Test(None)
test.describe("Basic Tests")
test.it("should handle numbers between 0-99999")
test.assert_equals( number_to_english(0), 'zero')
test.assert_equals( number_to_english(7), 'seven')
test.assert_equals( number_to_english(11), 'eleven')
test.assert_equals( number_to_english(20), 'twenty')
test.assert_equals( number_to_english(47), 'forty seven')
test.assert_equals( number_to_english(100), 'one hundred')
test.assert_equals( number_to_english(111), 'one hundred eleven')
test.assert_equals( number_to_english(305), 'three hundred five')
test.assert_equals( number_to_english(4002), 'four thousand two')
test.assert_equals( number_to_english(3892), 'three thousand eight hundred ninety two')
test.assert_equals( number_to_english(6800), 'six thousand eight hundred')
test.assert_equals( number_to_english(14111), 'fourteen thousand one hundred eleven')
test.assert_equals( number_to_english(20500), 'twenty thousand five hundred')
test.assert_equals( number_to_english(99999), 'ninety nine thousand nine hundred ninety nine')
test.it("should return empty string when given number out of range")
test.assert_equals( number_to_english(95.99), '')
test.assert_equals( number_to_english(-4), '')