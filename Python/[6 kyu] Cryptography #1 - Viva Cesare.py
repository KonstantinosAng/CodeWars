# see https://www.codewars.com/kata/56efab15740d301ab40002ee/train/python

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_crypto_encode(text, shift):
  ret = ""
  if not text: return ret
  if text.strip() == "": return ret
  for letter in text:
    if letter.isalpha():
      value = letters.find(letter) + shift
      while value >= len(letters): value -= len(letters)
      while value < 0: value += len(letters)
      ret += letters[value]
    else:  ret += letter
  return ret
  
from TestFunction import Test
test = Test(None)

      
test.describe("Basic tests")
test.it("Very basic tests")
test.assert_equals(caesar_crypto_encode("Et tu, Brute?", 3), "Hw wx, Euxwh?");
test.assert_equals(caesar_crypto_encode("Hw wx, Euxwh?", -3), "Et tu, Brute?");
test.it("Extended tests")
test.assert_equals(caesar_crypto_encode("123,.)(!?", 10), "123,.)(!?")
test.assert_equals(caesar_crypto_encode("", 10), "", "Problem: empty string")
test.assert_equals(caesar_crypto_encode(None, 10), "", "Problem: null")
test.assert_equals(caesar_crypto_encode("   ", 10), "", "Problem: whitespaces")
test.assert_equals(caesar_crypto_encode("Hello world!", 127), "eBIIL TLOIA!")
test.assert_equals(caesar_crypto_encode("eBIIL TLOIA!", -127), "Hello world!")
test.assert_equals(caesar_crypto_encode("ksdjai8983hdk?}{", 15), "zHsypx8983wsz?}{")
test.assert_equals(caesar_crypto_encode("Hello world!", 0), "Hello world!")
test.assert_equals(caesar_crypto_encode("-UrSmx/vjn5ynS4;BMDXfP:f0SdRVcI*", -47), "-ZwXrC/Aos5DsX4;GRIckU:k0XiWahN*")
test.assert_equals(caesar_crypto_encode("NqKxSc1;MRjFB25uy+v:AX9;4wdve gG-UW76HG,t..I", 4), "RuOBWg1;QVnJF25yC+z:Eb9;4Ahzi kK-Ya76LK,x..M")
