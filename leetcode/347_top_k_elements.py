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