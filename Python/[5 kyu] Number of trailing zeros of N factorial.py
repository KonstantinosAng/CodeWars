# More details on this kata
# https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

def zeros(n):
    if n == 0: return 0
    i, _zeroes = 5, 0
    while n/i >= 1:
        _zeroes += int(n/i)
        i *= 5
    return int(_zeroes)

