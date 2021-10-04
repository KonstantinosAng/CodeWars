# see https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
  score = 0
  digit = 1
  while len(dice) > 0 and digit < 7:
    if dice.count(digit) >= 3:
      if digit == 1: score += 1000
      else: score += digit * 100
      for _ in range(3): dice.pop(dice.index(digit))
    if dice.count(digit) > 0 and digit == 5 or digit == 1:
      times = dice.count(digit)
      for _ in range(times):
        if digit == 1: score += 100
        if digit == 5: score += 50
        dice.pop(dice.index(digit))
    digit += 1
  return score
  


from TestFunction import Test
test = Test(None)
test.describe("Example Tests")
test.it("Example Case")
test.assert_equals( score( [2, 3, 4, 6, 2] ), 0)
test.assert_equals( score(  [4, 4, 4, 3, 3] ), 400)
test.assert_equals( score(  [2, 4, 4, 5, 4] ), 450)
