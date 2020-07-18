# see https://www.codewars.com/kata/588a3c3ef0fbc9c8e1000095/solutions/python

def max_diff(lst):
    return sorted(lst)[-1] - sorted(lst)[0] if len(lst) > 1 and lst != [] else 0


print(max_diff([0, 1, 2, 3, 4, 5, 6]) ==  6);
print(max_diff([-0, 1, 2, -3, 4, 5, -6]) == 11);
print(max_diff([0, 1, 2, 3, 4, 5, 16]) == 16);
print(max_diff([16]) == 0);
print(max_diff([]) == 0);
