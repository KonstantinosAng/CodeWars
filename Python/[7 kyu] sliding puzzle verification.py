# see https://www.codewars.com/kata/5e28b3ff0acfbb001f348ccc/solutions/python

from TestFunction import Test

def is_solved(board):
  array = []
  for row in board:
    for col in row:
      array.append(col)
  return array == [x for x in range(len(board)*len(board))]
  

Test(True).assert_result(is_solved([[0,1],[2,3]]))
Test(False).assert_result(is_solved([[1,0],[3,2]]))