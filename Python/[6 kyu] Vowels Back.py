# see https://www.codewars.com/kata/57cfd92c05c1864df2001563/train/python

def vowel_back(st):
  consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
  retArray = []
  for letter in st:
    if letter in consonants:
      if letter == 'c': 
        newLetter = ord(letter) - 1
      elif letter == 'd':
        newLetter = ord(letter) - 3
      else:
        newLetter = ord(letter) + 9
      if newLetter > ord('z'): newLetter -= 26
    else:
      if letter == 'o': 
        newLetter = ord(letter) - 1
      elif letter == 'e':
        newLetter = ord(letter) - 4
      else:
        newLetter = ord(letter) - 5
      if newLetter < ord('a'): newLetter += 26
    if chr(newLetter) in ['c', 'o', 'd', 'e']: newLetter = ord(letter)
    retArray.append(chr(newLetter))
  return "".join(x for x in retArray)
  

from TestFunction import Test
test = Test(None)
test.describe("Fixed Tests")
test.it('Basic Test Cases')
test.assert_equals(vowel_back("testcase"), "tabtbvba")
test.assert_equals(vowel_back("codewars"), "bnaafvab")
test.assert_equals(vowel_back("exampletesthere"), "agvvyuatabtqaaa")
test.assert_equals(vowel_back("returnofthespacecamel"), "aatpawnftqabyvbabvvau")