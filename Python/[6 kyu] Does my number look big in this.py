# More details on this kata
# https://www.codewars.com/kata/5287e858c6b5a9678200083c

def narcissistic(value):
    return sum([n**(len([int(d) for d in str(value)])) for n in [int(d) for d in str(value)]]) == value

