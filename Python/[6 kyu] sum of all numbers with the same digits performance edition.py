# see https://www.codewars.com/kata/5eb9a92898f59000184c8e34/solutions

from TestFunction import Test

from itertools import permutations


def sum_arrangements(num):
  rv = []
  for x in permutations([int(x) for x in str(num)]):
    rv.append(int(''.join([str(y) for y in x])))
  return sum(rv)


test = Test(None)
test.assert_equals(sum_arrangements(123), 1332)
test.assert_equals(sum_arrangements(1185), 99990)
test.assert_equals(sum_arrangements(9617658098), 23788799997621120)
test.assert_equals(sum_arrangements(3045748679), 21369599997863040)
test.assert_equals(sum_arrangements(7448087599), 24595199997540480)
test.assert_equals(sum_arrangements(3404642039), 14111999998588800)
test.assert_equals(sum_arrangements(7945984136), 22579199997742080)
