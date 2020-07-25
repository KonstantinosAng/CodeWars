# see https://www.codewars.com/kata/562e274ceca15ca6e70000d3/solutions/python

from TestFunction import Test
import numpy as np
# n : number of intervals
def len_curve(n):
  steps, length = [], 0
  x2 = lambda x: x*x
  steps = np.linspace(0,1,n+1)
  # print(steps)
  for i in range(len(steps) - 1):
    x0 = steps[i]
    y0 = x2(steps[i])
    x1 = steps[i+1]
    y1 = x2(steps[i+1])
    length += np.sqrt((x0 - x1)**2 + (y0 - y1)**2)
  return float("%.9f" % length)

Test = Test(None)
Test.assert_equals(len_curve(1), 1.414213562)
Test.assert_equals(len_curve(10), 1.478197397)
Test.assert_equals(len_curve(40), 1.478896)
Test.assert_equals(len_curve(200), 1.478940)
Test.assert_equals(len_curve(1200), 1.478942)
Test.assert_equals(len_curve(47541), 1.478942)