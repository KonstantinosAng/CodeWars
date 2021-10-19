# see https://www.codewars.com/kata/59098c39d8d24d12b6000020/train/python

def dot(n,m):
  retArray = []
  for i in range(2*m+1):
    if i%2: retArray.append("| o "*n + "|")
    else: retArray.append("+---"*n + "+")
  return "\n".join(x for x in retArray)


from TestFunction import Test
test = Test(None)

test.describe("Basic tests")
# test.assert_equals(dot(1,1), "+---+\n| o |\n+---+")
test.assert_equals(dot(3,2), "+---+---+---+\n| o | o | o |\n+---+---+---+\n| o | o | o |\n+---+---+---+")