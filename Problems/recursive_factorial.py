
def recursive_factorial(n, result = 1):
    # if n == 0:
    #     return result
    result = n * result
    return recursive_factorial(n-1, result)

print(recursive_factorial(0))
print(recursive_factorial(5))
print(recursive_factorial(3))
print(recursive_factorial(1))