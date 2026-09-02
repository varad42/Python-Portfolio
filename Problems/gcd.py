def gcd_brute(a, b):
    divisor = 0
    count = 0
    for i in range(1, min(a, b) + 1):
        count += 1
        if a % i == 0 and b % i == 0:
            divisor = i
    return divisor, count

def gcd_euclid(a, b):
    count = 0
    while b != 0:
        count += 1
        a, b = b, a % b
    return a, count

print(gcd_brute(1071, 462))
print(gcd_euclid(1071, 462))


# print(gcd(12, 18))  # 6
# print(gcd(1071, 462))  # 21
# print(gcd(7, 13))  # 1
# print(gcd(5, 15))  # 5