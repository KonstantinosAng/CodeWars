# see https://www.codewars.com/kata/55e6f5e58f7817808e00002e/solutions/python

from TestFunction import Tester, Test

#@Tester((35, 1), 371)
#@Tester((7, 2), 1603)
#@Tester((42, 1), 483)
#@Tester((10, 2), 1021)
def seven(m):
  steps = 0
  while len(str(m)) > 2:
    m = int(str(m)[:-1]) - 2*int(str(m)[-1])
    steps += 1
    if m%7 == 0 and len(str(m)) <= 2:
      break
  return (m, steps)


Test((7, 2)).assert_result(seven(1603))
Test((35, 1)).assert_result(seven(371))
Test((42, 1)).assert_result(seven(483))
Test((10, 2)).assert_result(seven(1021))
