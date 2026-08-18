def count_digits(num):
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    return count


print(count_digits(4156))
print(count_digits(7))
print(count_digits(100))