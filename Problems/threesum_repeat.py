def threeSum(nums):
    nums = sorted(nums)
    result = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left = i+1
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] == target:
                result.append([nums[i],nums[left],nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

    return result





print(threeSum([-1, 0, 1, 2, -1, -4]))
print(threeSum([0, 0, 0, 0]))
