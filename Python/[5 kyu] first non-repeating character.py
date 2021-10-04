# see https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/python

def first_non_repeating_letter(string):
  stringCopy = "".join([x.lower() for x in string])
  for s in stringCopy:
    if stringCopy.count(s) == 1:
      if s.isalpha():
        if s in string: return s
        if s.upper() in string: return s.upper()
      else:
        return s
  return ""


from TestFunction import Test
test = Test(None)   

test.describe('Basic Tests')
# test.it('should handle simple tests')
test.assert_equals(first_non_repeating_letter('a'), 'a')
test.assert_equals(first_non_repeating_letter('stress'), 't')
test.assert_equals(first_non_repeating_letter('moonmen'), 'e')

# test.it('should handle empty strings')
test.assert_equals(first_non_repeating_letter(''), '')

# test.it('should handle all repeating strings') 
test.assert_equals(first_non_repeating_letter('abba'), '')
test.assert_equals(first_non_repeating_letter('aa'), '')

# test.it('should handle odd characters')
test.assert_equals(first_non_repeating_letter('~><#~><'), '#')
test.assert_equals(first_non_repeating_letter('hello world, eh?'), 'w')

test.it('should handle letter cases')
test.assert_equals(first_non_repeating_letter('sTreSS'), 'T')
test.assert_equals(first_non_repeating_letter('Go hang a salami, I\'m a lasagna hog!'), ',')
