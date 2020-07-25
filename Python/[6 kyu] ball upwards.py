# see https://www.codewars.com/kata/566be96bb3174e155300001b/solutions/python

from TestFunction import Test

def max_ball(v0):
  g = 9.81
  v0 = v0 * 1 / 3.6
  t, h, max_height, max_index = 0, [], 0, 0
  while v0*t-0.5*g*t*t >= 0:
    h.append(v0*t-0.5*g*t*t)
    t += 1/10
    if h[-1] > max_height: 
      max_height = h[-1]
      max_index = len(h) - 1
  return max_index
     

Test = Test(None)
Test.assert_equals(max_ball(37), 10)
Test.assert_equals(max_ball(45), 13)
Test.assert_equals(max_ball(99), 28)
Test.assert_equals(max_ball(85), 24)
Test.assert_equals(max_ball(15), 4)
