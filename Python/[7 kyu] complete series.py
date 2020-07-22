# see https://www.codewars.com/kata/580a4001d6df740d61000301/solutions/python

from TestFunction import Test

def complete_series(seq): 
    seq = sorted(seq)
    for number in seq:
      if seq.count(number) > 1:
        return [0]
    return [i for i in range(seq[-1]+1)]


Test([0,1]).assert_result(complete_series([0,1]))
Test([0,1,2,3,4,5,6]).assert_result(complete_series([1,4,6]))
Test([0,1,2,3,4,5]).assert_result(complete_series([3,4,5]))
Test([0,1,2]).assert_result(complete_series([2,1]))
Test([0]).assert_result(complete_series([1,4,4,6]))
