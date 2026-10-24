
def trap(heights):
    total_water = 0

    def left_max_list(heights):
        n = len(heights)
        left_max = [0] * n
        left_max[0] = heights[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], heights[i])

        return left_max

    def right_max_list(heights):
        n = len(heights)
        right_max = [0] * n
        right_max[n - 1] = heights[n - 1]

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], heights[i])

        return right_max

    if len(heights) < 3:
        return 0

    left_max = left_max_list(heights)
    right_max = right_max_list(heights)

    for i in range(1, len(heights) - 1):
        water = min(left_max[i], right_max[i]) - heights[i]
        total_water += water

    return total_water


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
print(trap([4, 2, 0, 3, 2, 5]))                    # 9


# Time: O(n) | Space: O(n)
# approach build a left_max list storing the tallest bar seen from the left at each index
# build a right_max list storing the tallest bar seen from the right at each index
# loop through each interior index and calculate water using the smaller of the two maximums minus the current height
# add the trapped water at each index to the total
# return the total water









