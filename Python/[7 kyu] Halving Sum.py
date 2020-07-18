# see https://www.codewars.com/kata/5a58d46cfd56cb4e8600009d/solutions/python

def halving_sum(n): 
    sum, i = 0, 1
    while n//i >= 1:
        sum += n//i
        i *= 2
    return sum


print(halving_sum(25) == 47)
print(halving_sum(127) == 247)