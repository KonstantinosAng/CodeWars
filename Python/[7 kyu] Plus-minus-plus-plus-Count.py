# see https://www.codewars.com/kata/5bbb8887484fcd36fb0020ca/solutions/python

def catch_sign_change(lst):
    if lst == []: return 0
    plus = False if lst[0] < 0 else True
    minus = False if lst[0] >= 0 else True
    count = 0
    for number in lst:
        if number >= 0 and minus is True:
            count += 1
            minus, plus = False, True
        if number < 0 and plus is True:
            count += 1
            plus, minus = False, True
    return count

print(catch_sign_change([1, 3, 4, 5]) == 0)
print(catch_sign_change([1, -3, -4, 0, 5]) == 2)
print(catch_sign_change([]) == 0)
print(catch_sign_change([-47,84,-30,-11,-5,74,77]) == 3)