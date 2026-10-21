def trap(heights):
    total_water = 0

    def build_left_max(heights):
        n = len(heights)
        left_max = [0] * n
        left_max[0] = heights[0]

        for i in range(1, n):
            left_max[i] = max(left_max[i-1], heights[i])

        return left_max

    def build_right_max(heights):
        n = len(heights)
        right_max = [0] * n
        right_max[n-1] = heights[n-1]

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i+1], heights[i])

        return right_max

    if len(heights) < 3:
        return 0

    left_max = build_left_max(heights)
    right_max = build_right_max(heights)

    for i in range(1, len(heights) - 1):
        water = min(left_max[i],right_max[i]) - heights[i]
        total_water += water

    return total_water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(trap([4,2,0,3,2,5]))               # 9