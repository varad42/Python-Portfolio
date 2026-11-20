# binary search on the answer (speed 1..max pile); works → best = mid, go left”, Time O(n log m), Space O(1)
def minEatingSpeed(piles, hrs):
    low = 1
    best = max(piles)
    high = max(piles)

    while low <= high:
        mid = (low + high) // 2
        total_hours = 0

        for pile in piles:
            required_hour = (pile + mid - 1) // mid
            total_hours += required_hour

        if total_hours > hrs:
            low = mid + 1
        else:
            best = mid          # ← the speed that worked, not its hours
            high = mid - 1

    return best


print(minEatingSpeed([3, 6, 7, 11], 8))          # 4
print(minEatingSpeed([30, 11, 23, 4, 20], 5))    # 30
print(minEatingSpeed([30, 11, 23, 4, 20], 6))    # 23