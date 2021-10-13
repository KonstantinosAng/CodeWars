# see https://www.codewars.com/kata/59fc9e7ec374cbbb8a0000a7/train/python

def largest_cross_sum(matrix):
  maxRow1 = 0
  maxRowIndex1 = 0
  for i, row in enumerate(matrix):
    if sum(row) > maxRow1:
      maxRow1 = sum(row)
      maxRowIndex1 = i
  maxCol1 = 0
  for i in range(len(matrix[0])):
    col = []
    for j, row in enumerate(matrix):
      if j != maxRowIndex1:
        col.append(row[i])
    if sum(col) > maxCol1:
      maxCol1 = sum(col)
  maxCol2 = 0
  maxColIndex2 = 0
  for i in range(len(matrix[0])):
    col = []
    for j, row in enumerate(matrix):
      col.append(row[i])
    if sum(col) > maxCol2:
      maxCol2 = sum(col)
      maxColIndex2 = i
  maxRow2 = 0
  for i, row in enumerate(matrix):
    if sum(row[:maxColIndex2] + row[maxColIndex2+1:]) > maxRow2:
      maxRow2 = sum(row[:maxColIndex2] + row[maxColIndex2+1:])
  # print(maxRow1 + maxCol1, maxRow2 + maxCol2)
  return max(maxRow1 + maxCol1, maxRow2 + maxCol2)

from TestFunction import Test
test = Test(None)

test.describe('Sample Test Cases')
test.it('Example Test Case')
# matrix1 = [[1, 2, 3],
#             [4, 5, 6],
#             [7, 8, 9]]
        
# test.assert_equals(largest_cross_sum(matrix1), 33)

# matrix2 = [[1, 2, 1],
#             [2, 2, 2],
#             [1, 2, 1]]
        
# test.assert_equals(largest_cross_sum(matrix2), 10)

# matrix3 = [[1, 2, 1, 1],
#             [2, 2, 2, 2],
#             [1, 2, 1, 1],
#             [1, 2, 1, 1]]
        
# test.assert_equals(largest_cross_sum(matrix3), 14)

# matrix4 = [[1, 1, 1, 4, 1, 1, 1],
#             [3, 3, 3, 3, 3, 3, 3],
#             [1, 1, 1, 4, 1, 1, 1]]
        
# test.assert_equals(largest_cross_sum(matrix4), 29)

# matrix5 = [[1, 0, 3, 2, 3, 4, 2, 3, 0, 0], 
#             [3, 4, 1, 2, 2, 0, 1, 1, 3, 0], 
#             [3, 2, 3, 1, 1, 3, 4, 4, 0, 4], 
#             [4, 1, 0, 3, 4, 0, 0, 4, 3, 4], 
#             [0, 2, 0, 3, 1, 0, 4, 3, 0, 1], 
#             [4, 2, 4, 3, 4, 4, 3, 2, 0, 3], 
#             [4, 4, 0, 1, 1, 1, 4, 4, 2, 4], 
#             [4, 1, 3, 2, 4, 3, 4, 1, 4, 4], 
#             [2, 2, 4, 4, 0, 3, 2, 2, 1, 1]]

# test.assert_equals(largest_cross_sum(matrix5), 53)

# matrix6 = [[4, 4, 0, 1, 1, 1, 4, 1, 2, 1], [4, 4, 1, 1, 1, 0, 3, 3, 0, 3], [1, 4, 0, 1, 4, 0, 0, 1, 4, 3], [2, 2, 4, 0, 4, 2, 0, 1, 1, 0], [4, 4, 2, 0, 2, 3, 1, 1, 1, 4], [2, 1, 1, 2, 3, 0, 4, 2, 4, 2]]

# test.assert_equals(largest_cross_sum(matrix6), 39)

matrix7 = [[1, 0, 0, 0, 1, 3], 
            [1, 2, 2, 2, 3, 1], 
            [3, 3, 0, 2, 1, 4]]

test.assert_equals(largest_cross_sum(matrix7), 18)