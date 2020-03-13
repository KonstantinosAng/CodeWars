# More details about this kata
# https://www.codewars.com/kata/the-millionth-fibonacci-kata

def multiply(m1, m2):
    x = m1[0][0]*m2[0][0] + m1[0][1] * m2[1][0]
    y = m1[0][0]*m2[0][1] + m1[0][1] * m2[1][1]
    z = m1[1][0]*m2[0][0] + m1[1][1] * m2[1][0]
    w = m1[1][0]*m2[0][1] + m1[1][1] * m2[1][1]
    return [[x, y], [z, w]]

def fib(n):
    r = [[1, 0], [0, 1]]
    t = [[0, 1], [1, 1]]
    if n < 0:
        n, t = -n, [[-1, 1], [1, 0]]
    while n > 0:
        if n & 1 > 0:
            r = multiply(t, r)
        t = multiply(t, t)
        n >>= 1
    return r[0][1]
