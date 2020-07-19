# see https://www.codewars.com/kata/556196a6091a7e7f58000018/solutions/python

def largest_pair_sum(numbers): 
    return sorted(numbers)[-1] + sorted(numbers)[-2]


print(largest_pair_sum([10,14,2,23,19]) == 42)
print(largest_pair_sum([-100,-29,-24,-19,19]) == 0)
print(largest_pair_sum([1,2,3,4,6,-1,2]) == 10)
print(largest_pair_sum([-10, -8, -16, -18, -19]) == -18)