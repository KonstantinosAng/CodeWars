# see https://www.codewars.com/kata/55ab4f980f2d576c070000f4/train/python

def game(n):
  if n == 0: return [0]
  if n == 1: return [1, 2]
  if n == 2: return [3, 2]
  if n == 3: return [9, 2]
  s, step = 4.5, 3.5
  for _ in range(n-3):
    s = s + step
    step += 1.0
  if int(s) == s: return [s]
  else: return [int(str(2*int(s)+1)), 2]
    


from TestFunction import Test
test = Test(None)

test.assert_equals(game(0), [0])
test.assert_equals(game(1), [1, 2])
test.assert_equals(game(2), [3, 2])
test.assert_equals(game(3), [9, 2])
test.assert_equals(game(4), [8])
test.assert_equals(game(5), [25, 2])
test.assert_equals(game(6), [18])
test.assert_equals(game(7), [49, 2])
test.assert_equals(game(8), [32])

# 0.5, 1.5, 4.5, 8, 12.5, 18, 24.5, 32
# 1, 3, 3.5, 4.5, 5.5, 6.5, 7.5 