def threeSum(nums):
    # sort the array
    nums = sorted(nums)
    result = []


    for i in range(len(nums)):
        # leave the same numbers
        if i > 0 and nums[i] == nums[i-1]:
            continue
        target = -nums[i]
        left = i+1
        right = len(nums) - 1


        while left < right:
            # if we found correct triplet
            if nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip Duplicate Elements
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            # if sum is greater reduce right hand side
            elif nums[left] + nums[right] > target:
                right -= 1
            # else increase left hand side
            else:
                left += 1
    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))   # [[-1, -1, 2], [-1, 0, 1]]
print(threeSum([0, 0, 0, 0]))            # [[0, 0, 0]]
print(threeSum([1, 2, 3]))               # []
print(threeSum([-2, 0, 0, 2, 2]))        # [[-2, 0, 2]]