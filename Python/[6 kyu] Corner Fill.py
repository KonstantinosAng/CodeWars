# see https://www.codewars.com/kata/60b7d7c82358010006c0cda5/train/python

def corner_fill(square):
  if len(square) <=0 : return []
  rows = len(square)
  cols = len(square[0])
  endCols = 0
  retArray = []
  goDown = True
  for i in range(rows):
    # print('row',i)
    if goDown:
      # print('Go down')
      for j in range(cols - endCols):
        # print(i, j)
        retArray.append(square[i][j])
      for k in range(i, rows):
        if k == i: continue
        # print(k, j)
        retArray.append(square[k][j])
      goDown = False
    else:
      # print('Go up')
      for k in range(rows-1, i-1, -1):
        if k == i: continue
        # print(k, j-1)
        retArray.append(square[k][j-1])
      # print('row',i)
      for j in range(cols - endCols-1, -1, -1):
        # print(i, j)
        retArray.append(square[i][j])
      goDown = True
    endCols += 1
  return retArray

from TestFunction import Test
test = Test(None)

test_cases = [
  ('1x1 square', [[1]], [1]),
  ('2x2 square', [[1,2], [4,5]], [1, 2, 5, 4]),
  ('3x3 square', [[1,2,3], [4,5,6], [7,8,9]], [1, 2, 3, 6, 9, 8, 5, 4, 7]),
]

test.describe('Sample tests')
for name, square, expected in test_cases:
  test.it(name)
  test.assert_equals(corner_fill(square), expected)