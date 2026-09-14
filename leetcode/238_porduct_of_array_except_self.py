def productExceptSelf(nums):
    result = [1] * len(nums)
    product = 1

    for i in range(len(nums)):
        result[i] = product
        product = product * nums[i]

    product = 1

    for i in range(len(nums) -1, -1, -1):
        result[i] = result[i] * product
        product = product * nums[i]

    return result


print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))

# https://neetcode.io/problems/products-of-array-discluding-self/history?list=neetcode150&submissionIndex=0
# Time O(n), Space O(1)
# approach create a result array and a running product
# first pass: walk left to right and store the product of everything before the current index
# reset product to 1
# second pass: walk right to left and multiply result[i] by the product of everything after the current index
# update product using nums[i] as we move right to left
# return result