# see https://www.codewars.com/kata/551dd1f424b7a4cdae0001f0/solutions

from TestFunction import Test

def who_is_next(names, r):
    while r > 5:
        r = (r - 4) // 2
    return names[r-1]

test = Test(None)
names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

test.assert_equals(who_is_next(names, 1), "Sheldon")
test.assert_equals(who_is_next(names, 52), "Penny")
test.assert_equals(who_is_next(names, 7230702951), "Leonard")