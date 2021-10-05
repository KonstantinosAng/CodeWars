def solve(m):
  return (2*m + 1 - (4*m + 1)**0.5)/(2 * m)
  # s = 0
  # x = 0.6
  # found = False
  # while not found:
  #   s = sum([n*x**n for n in range(1, 50)])
  #   if 0 <= m - s <= 1e-12: found = True
  #   if s > m: x -= 0.00000001
  #   else: x += 0.0000001
  #   print(x)
  # return x
  
print(solve(2))
print(solve(4))