# see https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

from TestFunction import Test

def solution(number):
  return sum([x for x in range(1,number) if not x%3 or not x%5])

test = Test(None)
test.describe("Sample tests")
test.it("Should return 3 for n=4")
test.assert_equals(solution(4), 3)     
test.it("Should return 8 for n=6")
test.assert_equals(solution(6), 8)
test.it("Should return 60 for n=16")
test.assert_equals(solution(16), 60)
test.it("Should return 0 for n=3")
test.assert_equals(solution(3), 0)
test.it("Should return 3 for n=5")
test.assert_equals(solution(5), 3)
test.it("Should return 45 for n=15")
test.assert_equals(solution(15), 45)
test.it("Should return 0 for n=0")
test.assert_equals(solution(0), 0)
test.it("Should return 0 for n=-1")
test.assert_equals(solution(-1), 0)
test.it("Should return 23 for n=10")
test.assert_equals(solution(10), 23)
test.it("Should return 78 for n=20")
test.assert_equals(solution(20), 78)
test.it("Should return 9168 for n=200")
test.assert_equals(solution(200), 9168)

