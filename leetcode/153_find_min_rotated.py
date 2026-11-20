# compare mid with high: bigger → go right; else keep mid (high = mid). Loop while low < high”, Time O(log n), Space O(1)

def findMin(nums):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    return nums[low]


print(findMin([3, 4, 5, 1, 2]))  # 1
print(findMin([4, 5, 6, 7, 0, 1, 2]))  # 0
print(findMin([11, 13, 15, 17]))  # 11  (rotated n times = not rotated)
print(findMin([2, 1]))  # 1