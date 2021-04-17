# see https://www.codewars.com/kata/5f631ed489e0e101a70c70a0/train/python

def tourney(inp):
  ret = []
  ret.append(inp)
  inp = inp.copy()
  lastDigit = None
  pointer = 0
  while len(inp) > 1:
    
    if len(inp) % 2 != 0:
      lastDigit = inp.pop(-1)

    while pointer < len(inp) - 1:
      if inp[pointer] > inp[pointer+1]:
        inp.pop(pointer+1)
      else:
        inp.pop(pointer)
      pointer += 1
  
    if lastDigit is not None:
      inp = [lastDigit] + inp
      lastDigit = None   
    
    ret.append([x for x in inp])
    pointer = 0
  return ret
  

from TestFunction import Test
test = Test(None)
input1 = [9, 5, 4, 7, 6, 3, 8, 2]
output1 = [
  [9, 5, 4, 7, 6, 3, 8, 2], 
  [9, 7, 6, 8],
  [9, 8],
  [9]
]
test.assert_equals(tourney(input1), output1)
test.it("testing odd list length")
input2 = [9, 5, 4, 7, 6, 3, 8]
output2 = [
  [9, 5, 4, 7, 6, 3, 8], 
  [8, 9, 7, 6], 
  [9, 7],
  [9]
]
test.assert_equals(tourney(input2), output2)
