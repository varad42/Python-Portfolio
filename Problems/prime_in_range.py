
def is_prime(n):
    factors = []
    for i in range(1, n+1):
        if n%i == 0:
            factors.append(i)

    if len(factors) == 2:
        return True
    else:
        return False
def primes_in_range(start, end):

    result = []
    for num in range(start, end + 1):  # end inclusive
        if is_prime(num):
            result.append(num)
    return result

print(primes_in_range(10, 30))
print(primes_in_range(24, 28))
print(primes_in_range(1, 10))