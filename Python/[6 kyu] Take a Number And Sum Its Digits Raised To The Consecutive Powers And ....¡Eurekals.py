# More details on this kata
# https://www.codewars.com/kata/5626b561280a42ecc50000d1

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    ret, sum = [], 0
    for i in range(a, b + 1):
        num = [int(d) for d in str(i)]
        for j, digit in enumerate(num):
            sum += digit**(j+1)
        if sum == i:
            ret.append(i)
        sum = 0
    if len(ret) > 0:
        return ret
    return []
