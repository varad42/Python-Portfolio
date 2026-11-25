def minEatingSpeed(bananas, hrs):
    low = 1
    min_eating_speed = max(bananas)
    high = max(bananas)

    while low <= high:
        mid = (low + high) // 2
        total_hours = 0

        for pile in bananas:
            required_hour = (pile + mid - 1) // mid
            total_hours += required_hour

        if total_hours > hrs:
            low = mid + 1
        else:
            min_eating_speed = mid
            high = mid - 1

    return min_eating_speed


print(minEatingSpeed([3, 6, 7, 11], 8))          # 4
print(minEatingSpeed([30, 11, 23, 4, 20], 5))    # 30
print(minEatingSpeed([30, 11, 23, 4, 20], 6))    # 23
print(minEatingSpeed([1], 1))                    # 1