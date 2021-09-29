# see https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

from TestFunction import Test

def get_word_score(word):
  count = 0
  for c in word:
    count += ord(c) - 96
  return count

def high(x):
  arr = x.split(" ")
  max_score = {'score': 0, 'word': ''}
  for word in arr:
    score = get_word_score(word)
    if score > max_score['score']:
      max_score['score'] = score
      max_score['word'] = word
  return max_score['word']

test = Test(None)
test.describe("Fixed Tests")
test.it('Basic Test Cases')
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
test.assert_equals(high('aa b'), 'aa')
test.assert_equals(high('b aa'), 'b')
test.assert_equals(high('bb d'), 'bb')
test.assert_equals(high('d bb'), 'd')
test.assert_equals(high("aaa b"), "aaa")
