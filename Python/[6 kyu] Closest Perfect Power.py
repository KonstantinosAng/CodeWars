# see https://www.codewars.com/kata/57c7930dfa9fc5f0e30009eb/train/python

closest_power=lambda n:4if n<6 else min((abs(n-p),p)for i in range(2,int(__import__('math').log(n,2))+2)for x in[max(int(n**(1/i)),2)]for p in[x**i,(x+1)**i])[1]


from TestFunction import Test
test = Test(None)

test.describe("Fixed Tests")
test.it("Sample Tests")
test.assert_equals(closest_power(0), 4, "Remember: the lowest perfect power is 4")
test.assert_equals(closest_power(9), 9, "Should get exact powers")
test.assert_equals(closest_power(30), 32, "Should work for powers greater than 2")
test.assert_equals(closest_power(34), 32, "If you got 36, make sure you return the lowest of the two closest powers")
test.assert_equals(closest_power(56.5), 49, "If you got 64, make sure you return the lowest of the two closest powers")
test.assert_equals(closest_power(123321456654), 123321773584, "Make sure it works for bigger numbers too")