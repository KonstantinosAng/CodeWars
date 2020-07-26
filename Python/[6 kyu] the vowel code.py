# see https://www.codewars.com/kata/53697be005f803751e0015aa/solutions/python

from TestFunction import Test

encodings = {'a': '1', 'e': '2', 'i': '3', 'o': '4', 'u': '5'}
decodings = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}

def encode(st):
  ret = ''
  for letter in st:
    if letter in encodings:
      ret += encodings[letter]
    else:
      ret += letter
  return ''.join(c for c in ret)
        
def decode(st):
  ret = ''
  for letter in st:
    if letter in decodings:
      ret += decodings[letter]
    else:
      ret += letter
  return ''.join(c for c in ret)

Test = Test(None)
Test.assert_equals(encode('hello'), 'h2ll4')
Test.assert_equals(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
Test.assert_equals(encode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
Test.assert_equals(decode('h2ll4'), 'hello')
