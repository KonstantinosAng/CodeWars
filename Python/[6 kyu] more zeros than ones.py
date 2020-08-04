# see 

from TestFunction import Test

def more_zeros(s):
  count = {}
  rv = []
  for letter in s:
    if letter not in count:
      count[letter] = 1
      print(letter, letter.encode('ascii', 'replace'))
      binary = str(letter.encode('ascii', 'replace'), 2).replace('0b', '')
      if binary.count('0') >= binary.count('1'):
        rv.append(letter)
  return rv


test = Test(None)
test.assert_equals(more_zeros('abcde'), ['a', 'b', 'd'])
test.assert_equals(more_zeros('thequickbrownfoxjumpsoverthelazydog'), ['h', 'b', 'p', 'a', 'd'])
test.assert_equals(more_zeros('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG'), ['T', 'H', 'E', 'Q', 'I', 'C', 'B', 'R', 'F', 'X', 'J', 'P', 'L', 'A', 'D'])
test.assert_equals(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'), ['a', 'b', 'd', 'h', 'p', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'I', 'J', 'L', 'P', 'Q', 'R', 'T', 'X', '0'])
test.assert_equals(more_zeros('DIGEST'), ['D', 'I', 'E', 'T'])
