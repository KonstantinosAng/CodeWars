# see https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

def max_sequence(arr):
  if arr == []: return 0
  currentMax = arr[0]
  globalMax = arr[0]
  for i in range(1, len(arr)): # 8
      currentMax = max(arr[i], arr[i] + currentMax)
      if (currentMax > globalMax): globalMax = currentMax    
  return globalMax if globalMax > 0 else 0
  



from TestFunction import Test
test = Test(None)   
test.describe("Tests")
test.it('should work on an empty array')  
test.assert_equals(max_sequence([]), 0)
test.it('should work on the example')
test.assert_equals(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
test.assert_equals(max_sequence([-16, -3, -15, 27, 28, 24, -10, 21, 10, 6, -14, 30, -15, 18, 20, -3, 9, -29, -7, -14, -21, -25, 23, 10, 12, 27, -6, 21, -30, 30, -21, -19, 8, 27, 11, 16, 28, 26, -5, -20, -29, -7, -6, 22, 12, -8, -9, -25, 19, 4]), 218)
