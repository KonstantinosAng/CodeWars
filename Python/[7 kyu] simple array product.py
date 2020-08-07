# see https://www.codewars.com/kata/5d0365accfd09600130a00c9/train/python

def solve(arr):
    result = arr[0]
    for number_array in range(1, len(arr)):
        result = [x * y for x in result for y in arr[number_array]]
    return max(result)

from TestFunction import Test
Test = Test(None)
Test.it("Basic tests")
Test.assert_equals(solve([[1, 2],[3, 4]]),8)
Test.assert_equals(solve([[10,-15],[-1,-3]]),45)
Test.assert_equals(solve([[-1,2,-3,4],[1,-2,3,-4]]),12)
Test.assert_equals(solve([[-11,-6],[-20,-20],[18,-4],[-20, 1]]),17600)
Test.assert_equals(solve([[14,2],[0,-16],[-12,-16]]),3584)
Test.assert_equals(solve([[-3,-4],[1,2,-3]]),12)
