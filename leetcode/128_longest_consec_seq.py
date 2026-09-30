
# def longestConsecutive(nums):
#
#     if len(nums) == 0:
#         return 0
#
#     nums = sorted(nums)
#     current = 1
#     best = 1
#
#     for i in range(len(nums) - 1):
#         if nums[i] + 1 == nums[i+1]:
#             current = current + 1
#
#             if current > best:
#                 best = current
#
#         elif nums[i] == nums[i+1]:
#             continue
#         else:
#             current = 1
#
#     return best

# Time: O(n log n) | Space: O(n)
# approach sort the array so consecutive numbers are next to each other
# loop through the sorted array and compare neighbouring numbers
# if the next number is exactly +1, increase the current sequence length
# if duplicate numbers are found, skip them
# if the sequence breaks, reset the current length to 1
# keep track of the longest sequence using best

def longestConsecutive(nums):

    if len(nums) == 0:
        return 0

    num_set = set(nums)
    best = 0

    for x in num_set:

        if (x - 1) in num_set:
            continue

        length = 1

        while (x + length) in num_set:
            length += 1

        if length > best:
            best = length

    return best

# Time: O(n) average | Space: O(n)
# approach store all numbers in a set for fast membership checking
# loop through each number and only start counting if x-1 is not in the set
# this means x is the start of a consecutive sequence
# count forward using x+length while the next number exists in the set
# keep track of the longest sequence using best

print(longestConsecutive([100, 4, 200, 1, 3, 2]))       # 4
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])) # 9
print(longestConsecutive([]))                            # 0
print(longestConsecutive([1, 2, 2, 3]))                  # 3