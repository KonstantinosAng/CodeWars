# see 

from TestFunction import Test

"""def parts_sums(ls):
  if ls == []: return [0]
  s = []
  i = 0
  while i != len(ls):
    s.append(sum(ls[i:]))
    i += 1
  return s + [0]
"""

def parts_sums(ls):
  if ls == []: return [0]
  return [sum(ls[i:]) for i in range(len(ls)+1)]


Test = Test(None)

def dotest(ls, expected):
  actual = parts_sums(ls)
  Test.assert_equals(actual, expected)
    
def basic_tests():
  dotest([], [0])
  dotest([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0])
  dotest([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0])
  dotest([14231, 137542, 173347, 19792, 63830, 87040, 15621, 56268, 65441, 193264, 153828, 97321, 179116, 182144],
         [1438785, 1424554, 1287012, 1113665, 1093873, 1030043, 943003, 927382, 871114, 805673, 612409, 458581, 361260, 182144, 0])
  dotest([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358], 
      [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0])

basic_tests()      


