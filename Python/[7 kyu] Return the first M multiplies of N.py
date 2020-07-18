# see https://www.codewars.com/kata/593c9175933500f33400003e/solutions/python

def multiples(m, n):
    return [n*i for i in range(1, m+1)]


print(multiples(3, 5) == [5, 10, 15])