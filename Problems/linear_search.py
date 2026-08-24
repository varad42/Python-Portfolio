def find(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            position = i
            return position
    return -1

print(find([4, 8, 15, 16], 15))    # 2   ← position, not the value!
print(find([4, 8, 15, 16], 4))     # 0   ← first position is 0
print(find([4, 8, 15, 16], 99))    # -1  ← not found
print(find([7, 7, 7], 7))          # 0   ← FIRST occurrence