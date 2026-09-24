
def longestConsecutive(nums):

    if len(nums) == 0:
        return 0

    nums = sorted(nums)
    current = 1
    best = 1

    for i in range(len(nums) - 1):
        if nums[i] + 1 == nums[i+1]:
            current = current + 1

            if current > best:
                best = current

        elif nums[i] == nums[i+1]:
            continue
        else:
            current = 1

    return best

print(longestConsecutive([100, 4, 200, 1, 3, 2]))       # 4
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
print(longestConsecutive([]))                            # 0
print(longestConsecutive([1, 2, 2, 3]))                  # 3