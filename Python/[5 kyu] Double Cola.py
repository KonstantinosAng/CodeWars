# see https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/train/python

def who_is_next(names, r):
  nNames = len(names)
  while r > nNames:
    r = (r - nNames) // 2 + ((r - nNames) % 2) # equivalent of ceil((r-5)/2)
  return names[r-1]



from TestFunction import Test
test = Test(None)   

names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

test.assert_equals(who_is_next(names, 1), "Sheldon")
test.assert_equals(who_is_next(names, 2), "Leonard")
test.assert_equals(who_is_next(names, 3), "Penny")
# test.assert_equals(who_is_next(names, 35), "Leonard")
test.assert_equals(who_is_next(names, 52), "Penny")
test.assert_equals(who_is_next(names, 7230702951), "Leonard")
