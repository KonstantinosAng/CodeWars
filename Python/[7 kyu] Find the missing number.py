# see https://www.codewars.com/kata/57f5e7bd60d0a0cfd900032d/solutions/python

def missing_no(nums):
    if 0 not in nums: return 0
    if 100 not in nums: return 100
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:
            return nums[i] + 1
    else:
        return None

nums = list(range(0,101))
nums.remove(5)
print(missing_no(nums) == 5)
nums = list(reversed(range(0,101)))
nums.remove(10)
print(missing_no(nums) == 10)