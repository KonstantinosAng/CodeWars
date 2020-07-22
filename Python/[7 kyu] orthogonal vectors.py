# see 

from TestFunction import Test

def is_orthogonal(u, v): 
    dot = sum([a*b for a, b in zip(u, v)])
    return dot == 0


Test(False).assert_result(is_orthogonal([1,2], [2,1]))
Test(True).assert_result(is_orthogonal([1,-2], [2,1]))
Test(False).assert_result(is_orthogonal([7,8], [7,-6]))
Test(True).assert_result(is_orthogonal([-13,-26], [-8,4]))
Test(True).assert_result(is_orthogonal([1,2,3], [0,-3,2]))
Test(False).assert_result(is_orthogonal([3,4,5], [6,7,-8]))
Test(True).assert_result(is_orthogonal([3,-4,-5], [-4,-3,0]))
Test(True).assert_result(is_orthogonal([1,-2,3,-4], [-4,3,2,-1]))
Test(True).assert_result(is_orthogonal([2,4,5,6,7], [-14,-12,0,8,4]))
Test(False).assert_result(is_orthogonal([5,10,1,20,2], [-2,-20,-1,10,5]))