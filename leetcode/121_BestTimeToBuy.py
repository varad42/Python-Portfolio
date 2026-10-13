def maxProfit(prices):
    day = 0
    lowest_so_far = prices[0]
    best_so_far = 0
    while day < len(prices):
        profit = prices[day] - lowest_so_far
        if lowest_so_far > prices[day]:
            lowest_so_far = prices[day]

        if profit > best_so_far:
            best_so_far = profit
        day += 1
    return best_so_far


print(maxProfit([7, 1, 5, 3, 6, 4]))   # 5
print(maxProfit([7, 6, 4, 3, 1]))      # 0

# with the header Time O(n), Space O(1), plus the note “profit before updating lowest = never sell before you buy.