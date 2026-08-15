# Q.5 Write digit_sum(n) that returns the sum of a number's digits.

def digit_sum(num):
    result = 0
    while num!=0:
        last_digit = num%10
        num = num // 10
        result = last_digit + result
    return result

print(digit_sum(153))