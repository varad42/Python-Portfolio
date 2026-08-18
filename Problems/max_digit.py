def max_digit(num):
    max_so_far = 0
    while num != 0:
        last_digit = num % 10
        num = num // 10
        if last_digit > max_so_far:
            max_so_far = last_digit
    return max_so_far





print(max_digit(3947))
print(max_digit(111))
print(max_digit(520))