# see https://www.codewars.com/kata/60fa9511fb42620019966b35/train/python

def recur(index, array, store):
  pointer = index
  while pointer < len(array):
    tempS = store[0] - array[pointer]
    if tempS % 2 == 0:
      store.pop(0)
      store = [array[pointer]] + store
      store.append(tempS)
      store = recur(pointer+1, array, store)
      return store
    else:
      pointer += 1
  return store

def peel_the_onion(s, d):
  ret = []
  for i in range(1, s+1):
    ret.append(i**d)
  if len(ret) == 1: return ret
  if len(ret) == 2: return ret[-1:]
  ret = [x for x in reversed(ret)]
  store = []
  store.append(ret[0])
  store = recur(1, ret, store)
  return [x for x in sorted(store, reverse=True)]
    


from TestFunction import Test
test = Test(None)

sample_test_cases = [
      #  s  d     result    
    (1, [
        (1, 1,    [1]),
        (2, 1,    [2]),
        (3, 1,    [2, 1]),
        (4, 1,    [2, 2]),
        (5, 1,    [2, 2, 1]),
    ]),
    (2, [
        (1, 2,    [1]),
        (2, 2,    [4]),
        (3, 2,    [8, 1]),
        (4, 2,    [12, 4]),
        (5, 2,    [16, 8, 1]),
    ]),
    (3, [
        (1, 3,    [1]),
        (2, 3,    [8]),
        (3, 3,    [26, 1]),
        (4, 3,    [56, 8]),
        (5, 3,    [98, 26, 1]),
    ]),
    (4, [
        (1, 4,    [1]),
        (2, 4,    [16]),
        (3, 4,    [80, 1]),
        (4, 4,    [240, 16]),
        (5, 4,    [544, 80, 1]),
    ]),
]

test.describe('Sample tests')
for d, test_cases in sample_test_cases:
  test.it(f"{d}")
  for s, d, expected in test_cases:
    test.assert_equals(peel_the_onion(s, d), expected, f'peel_the_onion({s}, {d})')
