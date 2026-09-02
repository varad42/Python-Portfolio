def two_sum(nums, num):
    seen = {}

    for i, value in enumerate(nums):
        num2 = num - value

        if num2 in seen:
            return seen[num2], i

        seen[value] = i

print(two_sum([2, 7, 11, 15], 9))  # (0, 1)   because nums[0]+nums[1] = 2+7 = 9
print(two_sum([3, 2, 4], 6))  # (1, 2)   because 2+4 = 6  ← NOT (0,0)! read on
print(two_sum([3, 3], 6))  # (0, 1)
print(two_sum([1, 2, 3], 100))  # None     ← no pair works