# see https://www.codewars.com/kata/57b1f617b69bfc08cf00042a/solutions

from TestFunction import Test

def sum_of_digits(a, b):
    def f(n):
        d, m, s = 0, 1, 0
        while n:
            n, r = divmod(n, 10)
            s += r * 9 * d * 10 ** d // 2 + r * (r-1) // 2 * 10 ** d + r * m
            m += r * 10 ** d
            d += 1
        return s
    return f(b) - f(max(a-1, 0))

test = Test(None)

testing = [[[6, 18], 75], [[17, 18], 17], [[11, 16], 27], [[6, 7], 13], [[3, 17], 78], [[2, 14], 59], [[5, 13], 45], [[2, 10], 45], [[8, 19], 72], [[7, 12], 30], 
            [[1, 10], 46], [[0, 9], 45], [[9, 999], 13464], [[10, 10000], 179956], [[1, 10000000], 315000001]]

for (a, b), expected in testing:
    test.assert_equals(sum_of_digits(a, b), expected)