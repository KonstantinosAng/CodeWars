# see https://www.codewars.com/kata/59c3e819d751df54e9000098/train/python

from TestFunction import Test

def get_consective_items(items, key): 
  positions, max_count, count = [], 0, 0
  for i, item in enumerate(str(items)):
    if item == str(key):
      positions.append(i)
  for i in range(len(positions)-1):
    if positions[i+1] - positions[i] == 1:
      count += 1
    else:
      count = 0
    if count > max_count:
      max_count = count
  if len(positions) == 0: return 0
  return max_count + 1


test = Test(None)
test.assert_equals(get_consective_items(90000, 0), 4)
test.assert_equals(get_consective_items('ascasdaiiiasdacasdiiiiicasdasdiiiiiiiiiiisdasdasdiii', 'i'), 11)
