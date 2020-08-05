# see https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/solutions/python

from TestFunction import Test

def solution(s):
  if len(s) == 1: return [s + '_']
  if len(s) == 2: return [s]
  rv = []
  j = 0
  if len(s)%2 != 0:
    s += '_'
  for i in range(len(s)-2-j):
    rv.append(s[i+j:i+2+j])
    j += 1
  return [x for x in rv if x != '']

test = Test(None)
test.describe("Example Tests")

tests = (
    ("asdfadsf", ['as', 'df', 'ad', 'sf']),
    ("asdfads", ['as', 'df', 'ad', 's_']),
    ("", []),
    ("x", ["x_"]),
)

for inp, exp in tests:
    test.assert_equals(solution(inp), exp)
