# Keep applying digit sum until only a single digit remains, and return it.

def digit_sum(num):
    result = 0
    while num != 0:
        last_digit = num % 10
        num = num // 10
        result = result + last_digit
    return result

def digit_sum_repeated(num):
    while num >= 10:
        num = digit_sum(num)
    return num

print(digit_sum_repeated(9875))
print(digit_sum_repeated(999))
print(digit_sum_repeated(5))

