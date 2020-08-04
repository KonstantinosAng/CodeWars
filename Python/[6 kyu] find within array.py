# see https://www.codewars.com/kata/51f082ba7297b8f07f000001/solutions/python

from TestFunction import Test

def find_in_array(seq, predicate): 
  rv = [i for i, x in enumerate(seq) if predicate(x, i)]
  if rv == []: return -1
  return rv[0]

test = Test(None)
true_if_even = lambda v, i: v % 2 == 0
never_true = lambda v, i: False
true_if_value_equals_index = lambda v, i: v == i
true_if_length_equals_index = lambda v, i: len(v) == i

test.assert_equals(find_in_array([], true_if_even) , -1)
test.assert_equals(find_in_array([1,3,5,6,7], true_if_even) , 3)
test.assert_equals(find_in_array([2,4,6,8], true_if_even) , 0)
test.assert_equals(find_in_array([2,4,6,8], never_true) , -1)
test.assert_equals(find_in_array([13,5,3,1,4,5], true_if_value_equals_index) , 4)
test.assert_equals(find_in_array(["one","two","three","four","five","six"], true_if_length_equals_index) , 4)
test.assert_equals(find_in_array(["bc","af","d","e"], true_if_length_equals_index) , -1)
