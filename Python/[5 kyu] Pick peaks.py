# see https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/train/python

# def pick_peaks(arr):
#   retDictionary = {"pos": [], "peaks": []}
#   counter = 1
#   while counter < len(arr) - 1:
#     possiblePeak = arr[counter]
#     if possiblePeak >= arr[counter - 1] and possiblePeak >= arr[counter + 1] and arr[counter - 1] != arr[counter + 1]: 
#       tempCounter = 1
#       end=False
#       print(counter)
#       if possiblePeak == arr[counter + 1] or possiblePeak == arr[counter - 1]:
#         while possiblePeak == arr[counter + tempCounter]:
#           if counter + tempCounter == len(arr) - 1: 
#             end=True
#             break
#           tempCounter += 1
#         print(end, possiblePeak, arr[counter + tempCounter], arr[counter - 1])
#         if not end and possiblePeak > arr[counter + tempCounter] and possiblePeak > arr[counter - 1]:
#           retDictionary['pos'].append(counter)
#           retDictionary['peaks'].append(possiblePeak)  
#           counter += tempCounter
#       else:
#         retDictionary['pos'].append(counter)
#         retDictionary['peaks'].append(possiblePeak)
#     counter += 1
#   return retDictionary

def pick_peaks(arr):
  retDictionary = {"pos": [], "peaks": []}
  counter = 1
  storeRemoved = []
  while counter < len(arr) - 1:
    possiblePeak = arr[counter]
    if possiblePeak == arr[counter + 1]:
      while possiblePeak == arr[counter + 1]:
        arr.pop(counter + 1)
        storeRemoved.append(counter + 1)
        if counter >= len(arr) - 1: break
    else:
      if possiblePeak > arr[counter - 1] and possiblePeak > arr[counter + 1]:
        tempCounter = 0
        for pos in storeRemoved:
          if counter >= pos:
            tempCounter += 1
        retDictionary['pos'].append(counter + tempCounter)
        retDictionary['peaks'].append(possiblePeak)
      counter += 1
  return retDictionary

from TestFunction import Test
test = Test(None)   

test.assert_equals(pick_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos":[3,7], "peaks":[6,3]})
test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos":[3,7], "peaks":[6,3]})
test.assert_equals(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos":[3,7,10], "peaks":[6,3,2]})
test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2,1]), {"pos":[2,4], "peaks":[3,2]})
test.assert_equals(pick_peaks([2,1,3,1,2,2,2,2]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([2,1,3,2,2,2,2,5,6]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([2,1,3,2,2,2,2,1]), {"pos":[2], "peaks":[3]})
test.assert_equals(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos":[2,7,14,20], "peaks":[5,6,5,5]})
test.assert_equals(pick_peaks([]),{"pos":[],"peaks":[]})
test.assert_equals(pick_peaks([1,1,1,1]),{"pos":[],"peaks":[]})
test.assert_equals(pick_peaks([15, 14, 2, 1, 7, 3, 4, 5, 2, -4, -4, 15, -5, 17, 18, 19, 3, 10, 15, 5, 13, 13, 20, 13, 17, 8, 1, 5]),{'pos': [4, 7, 11, 15, 18, 22, 24], 'peaks': [7, 5, 15, 19, 15, 20, 17]})
