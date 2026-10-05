def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left + 1, right + 1]
        elif total > target:      # too big
            right -= 1                # which walker, which way?
        else:                     # too small
            left += 1



print(twoSum([2, 7, 11, 15], 9))   # [1, 2]
print(twoSum([2, 3, 4], 6))        # [1, 3]
print(twoSum([-1, 0], -1))         # [1, 2]