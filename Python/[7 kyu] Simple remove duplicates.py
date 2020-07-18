# see https://www.codewars.com/kata/5ba38ba180824a86850000f7/solutions/python

def solve(arr):
  i = 0
  while i < len(arr):
    if arr.count(arr[i]) > 1:
      arr.pop(i)
    else:
      i+= 1
  return arr

print(solve([3,4,4,3,6,3]) == [4,6,3])
print(solve([1,2,1,2,1,2,3]) == [1,2,3])
print(solve([1,2,3,4]) == [1,2,3,4])
print(solve([1,1,4,5,1,2,1]) == [4,5,2,1])
