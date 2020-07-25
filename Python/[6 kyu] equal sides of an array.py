# see https://www.codewars.com/kata/5679aa472b8f57fb8c000047/solutions/python

from TestFunction import Test

def find_even_index(arr):
  for i in range(len(arr)):
    if sum(arr[i+1:]) == sum(arr[:i]): return i
  return -1

Test = Test(None)
Test.assert_equals(find_even_index([1,2,3,4,3,2,1]),3)
Test.assert_equals(find_even_index([1,100,50,-51,1,1]),1)
Test.assert_equals(find_even_index([1,2,3,4,5,6]),-1)
Test.assert_equals(find_even_index([20,10,30,10,10,15,35]),3)
Test.assert_equals(find_even_index([20,10,-80,10,10,15,35]),0)
Test.assert_equals(find_even_index([10,-80,10,10,15,35,20]),6)
Test.assert_equals(find_even_index(list(range(1,100))),-1)
Test.assert_equals(find_even_index([0,0,0,0,0]),0)
Test.assert_equals(find_even_index([-1,-2,-3,-4,-3,-2,-1]),3)
Test.assert_equals(find_even_index(list(range(-100,-1))),-1)
