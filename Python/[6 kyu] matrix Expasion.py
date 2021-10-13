# see https://www.codewars.com/kata/614adaedbfd3cf00076d47de/train/python

def expansion(matrix, n):
  for _ in range(n):
    rows = [x + [sum(x)] for x in matrix]
    extraRow = [sum([x[i] for x in rows]) for i in range(len(matrix))] + [sum([matrix[i][i] for i in range(len(matrix))])]
    rows.append(extraRow)
    matrix = rows
  return matrix


from TestFunction import Test
test = Test(None)

m1 = [
    [1,2],
    [5,3]
]

m2 = [
    [4,1],
    [19,-2]
]

m3 = [
    [102,39],
    [-11,-97]
]

m4 = [
    [53, -64, 16, 16], 
    [-98, 0, -14, -87], 
    [75, -74, 39, 36], 
    [32, 90, 42, 12]
]

test.describe("Example Tests")

test.it('Depth 1')
test.assert_equals(expansion(m1, 1), [[1, 2, 3], [5, 3, 8], [6, 5, 4]])
test.assert_equals(expansion(m2, 1), [[4, 1, 5], [19, -2, 17], [23, -1, 2]])
test.assert_equals(expansion(m3, 1), [[102, 39, 141], [-11, -97, -108], [91, -58, 5]])

test.it('Depth 2')
test.assert_equals(expansion(m1, 2), [[1, 2, 3, 6], [5, 3, 8, 16], [6, 5, 4, 15], [12, 10, 15, 8]])
# test.assert_equals(expansion(m2, 2), [[4, 1, 5, 10], [19, -2, 17, 34], [23, -1, 2, 24], [46, -2, 24, 4]])
# test.assert_equals(expansion(m3, 2), [[102, 39, 141, 282], [-11, -97, -108, -216], [91, -58, 5, 38], [182, -116, 38, 10]])
# test.assert_equals(expansion(m4, 2), [[53, -64, 16, 16, 21, 42], [-98, 0, -14, -87, -199, -398], [75, -74, 39, 36, 76, 152], [32, 90, 42, 12, 176, 352], [62, -48, 83, -23, 104, 178], [124, -96, 166, -46, 178, 208]])
