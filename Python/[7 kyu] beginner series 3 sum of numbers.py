# see https://www.codewars.com/kata/55f2b110f61eb01779000053/solutions/python

from TestFunction import Tester

@Tester(1)
def get_sum(a, b):
  if a <= b:
    return sum([x for x in range(a, b+1)])
  else:
    return sum([x for x in range(b, a+1)])

get_sum(0, 1)
# get_sum(0, -1)
