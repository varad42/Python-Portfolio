def maxArea(heights):
    left = 0
    right = len(heights) - 1
    best = 0
    while left <= right:
        if heights[left] < heights[right]:
            result = heights[left]*(right-left)
        else:
            result = heights[right] * (right - left)

        if result > best:
            best = result
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best

print(maxArea([1,8,6,2,5,4,8,3,7]))   # 49
print(maxArea([1,1]))                 # 1

# Time: O(n) | Space: O(1)
# approach start with two walkers at the left and right ends
# calculate the area using the shorter of the two heights
# update best if the current area is larger
# move the walker with the shorter height inward
# keep the taller height because moving the shorter height is the only way to potentially find a larger area
# continue until the two walkers meet

# Time: O(n) — the two pointers move inward, and each position is visited at most once.
# Space: O(1) — only left, right, best, and result are used; no extra structure grows with n.