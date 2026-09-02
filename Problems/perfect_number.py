def is_perfect(num):
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result = result + i
    return result == num

print(is_perfect(6))      # True
print(is_perfect(28))     # True
print(is_perfect(12))     # False
print(is_perfect(1))      # False  ← think: what are 1's divisors-excluding-itself?