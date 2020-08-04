# see https://www.codewars.com/kata/554ca54ffa7d91b236000023/solutions/python

from TestFunction import Test


def delete_nth(order,max_e):
  counts = {}
  rv = []
  for i in order:
    if str(i) not in counts:
      counts[str(i)] = 1  
    else:
      counts[str(i)] += 1
    if counts[str(i)] <= max_e:
      rv.append(i)
  return rv 


Test = Test(None)
Test.assert_equals(delete_nth([20,37,20,21], 1), [20,37,21])
Test.assert_equals(delete_nth([1,1,3,3,7,2,2,2,2], 3), [1, 1, 3, 3, 7, 2, 2, 2])
