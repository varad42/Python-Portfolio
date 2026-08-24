def stats(list):
    total = 0
    count = 0
    for i in list:
        total = total + i
        count = count + 1
    avg = total/count
    return total,avg

print(stats([4, 8, 15, 16]))
print(stats([5]))
print(stats([2, 4, 6, 8, 10]))