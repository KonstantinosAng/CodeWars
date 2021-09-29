# see https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

from TestFunction import Test

def race(v1, v2, g):
  if v1 >= v2: return None
  v1 = v1/3600
  v2 = v2/3600
  seconds = g/(v2 - v1)
  print(seconds)
  minutes = int(seconds / 60)
  hours = int(minutes / 60)
  minutes = minutes - 60*hours
  seconds = seconds - 60*minutes - 3600*hours
  return [hours, minutes, round(seconds)]

test = Test(None)
test.describe("race")
test.it("basic tests")
test.assert_equals(race(720, 850, 70), [0, 32, 18])
test.assert_equals(race(80, 91, 37), [3, 21, 49])
test.assert_equals(race(820, 81, 550), None)
test.assert_equals(race(386, 434, 105), [2, 11, 15])
