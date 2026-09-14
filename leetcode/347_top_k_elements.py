def topkelements(nums, k):
    freq = {}
    result = []

    for i in nums:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1

    while k != 0:
        large_num = 0
        large_key = None

        for key in freq:
            if freq[key] > large_num:
                large_num = freq[key]
                large_key = key

        result.append(large_key)
        del freq[large_key]
        k -= 1

    return result


print(topkelements([1, 2, 2, 3, 3, 3], 2))

def topkelements(nums, k):
    freq = {}

    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    result = sorted(freq, key=freq.get, reverse=True)[:k]

    return result

# https://neetcode.io/problems/top-k-elements-in-list/history?list=neetcode150&submissionIndex=0
# Time: O(n²) | Space: O(n)

# approach count how many times each int appears and store it in a dictionary
# repeatedly find the int with the largest frequency
# add that int to result and remove it from the dictionary
# repeat until we have k elements