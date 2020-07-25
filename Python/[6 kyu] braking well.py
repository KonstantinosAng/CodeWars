# see https://www.codewars.com/kata/565c0fa6e3a7d39dee000125/solutions/python

from TestFunction import Test

from math import sqrt
g = 9.81
def dist(v, mu):     
  v = v*1000/3600
  d1 = v*v / (2*mu*g)
  d2 = v * 1
  return d1 + d2

def speed(d, mu):
  a = 1/(2*mu*g)
  b = 1
  c = -d
  d = b*b - 4*a*c
  if d >= 0:
    r1, r2 = ((-b+sqrt(d))/(2*a))*3.6, ((-b-sqrt(d))/(2*a))*3.6
    return r1 if r1 >= 0 else r2
  else:
    return None

Test = Test(None)
Test.assert_equals(dist(144, 0.3), 311.83146449201496)
Test.assert_equals(dist(92, 0.5), 92.12909477605366)
Test.assert_equals(dist(142, 0.2), 435.94398509960854)
Test.assert_equals(dist(96, 0.2), 207.8876429946766)
Test.assert_equals(speed(159, 0.8), 153.79671564846308)
Test.assert_equals(speed(164, 0.7), 147.91115701756493)
Test.assert_equals(speed(153, 0.7), 142.14404997566152)
Test.assert_equals(speed(88, 0.9), 113.64202099481099)  
