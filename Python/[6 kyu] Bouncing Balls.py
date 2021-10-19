# see https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

def bouncing_ball(h, bounce, window):
  if h > 0 and bounce > 0 and bounce < 1 and window < h:
    count = 0
    while h > window:
      h = h*bounce
      count += 2
    return count - 1
  return -1

from TestFunction import Test
test = Test(None)

test.describe('Tests')
def testing(h, bounce, window, exp):
  actual = bouncing_ball(h, bounce, window)
  test.assert_equals(actual, exp)
        
test.it('Fixed Tests')
testing(2, 0.5, 1, 1)
testing(3, 0.66, 1.5, 3)
testing(30, 0.66, 1.5, 15)
# testing(30, 0.75, 1.5, 21)
