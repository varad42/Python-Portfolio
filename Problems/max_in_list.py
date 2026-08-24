def find_max(numbers):
    large_num = numbers[0]
    for i in numbers:
        if large_num < i:
            large_num = i
    return large_num


print(find_max([10, 5, 8, 20, 3]))  # 20
print(find_max([7]))  # 7
print(find_max([-5, -2, -9]))  # -2  ← the trap!