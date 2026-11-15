def productExceptSelf(nums):
    result = [1] * len(nums)
    product = 1

    for i in range(len(nums)):
        result[i] = product
        product = product * nums[i]

    product = 1

    for i in range(len(nums) -1 ,-1, -1):
        result[i] =  result[i] * product
        product = product * nums[i]

    return result

print(productExceptSelf([1, 2, 3, 4]))       # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]