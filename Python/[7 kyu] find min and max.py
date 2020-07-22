# see https://www.codewars.com/kata/57a1ae8c7cb1f31e4e000130/solutions/python

from TestFunction import Test

def get_min_max(seq):
  seq = sorted(seq)
  return (seq[0], seq[-1])


Test((1, 1)).assert_result(get_min_max([1]))
Test((1, 2)).assert_result(get_min_max([1,2]))
Test((1, 2)).assert_result(get_min_max([2,1]))
