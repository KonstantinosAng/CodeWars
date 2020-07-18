# see https://www.codewars.com/kata/58aed2cafab8faca1d000e20/solutions/python

def modified_sum(a, n):
  return sum([x**n - x for x in a])

print(modified_sum([1, 2, 3], 3) == 30)
print(modified_sum([1, 2], 5) == 30)