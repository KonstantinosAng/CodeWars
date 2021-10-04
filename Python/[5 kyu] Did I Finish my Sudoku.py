# see https://www.codewars.com/kata/53db96041f1a7d32dc0004d2/train/python

from math import floor
def validateRows(board):
  for row in board:
    for i in range(1, 10):
      if row.count(i) != 1: return False
  return True

def validateCols(board):
  cols = [[] for _ in range(9)]
  for row in board:
    for i in range(9):
      cols[i].append(row[i])
  return validateRows(cols)

def validateIslands(board):
  islands = [[] for _ in range(9)]
  for i, row in enumerate(board):
    islands[0 + floor(i/3) * 3].append(row[:3])
    islands[1 + floor(i/3) * 3].append(row[3:6])
    islands[2 + floor(i/3) * 3].append(row[6:])
  flattenIslands = []
  for island in islands:
    flattenIslands.append(island[0] + island[1] + island[2])
  return validateRows(flattenIslands)

def done_or_not(board):
  return 'Finished!' if validateRows(board) and validateCols(board) and validateIslands(board) else 'Try again!'
  

from TestFunction import Test
test = Test(None)
test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]), 'Finished!');
                        
test.assert_equals(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                              ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                              ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                              ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                              ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                              ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                              ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                              ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                              ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]), 'Try again!');