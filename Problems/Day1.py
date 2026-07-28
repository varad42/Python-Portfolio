# Problem 1:Prime Number Checker

print()

# def is_prime(n):
#     factors = []
#     for i in range(1, n+1):
#         if n%i == 0:
#             factors.append(i)
#
#     if len(factors) == 2:
#         return True
#     else:
#         return False
#
# print(is_prime(2))    # True
# print(is_prime(17))   # True
# print(is_prime(1))    # False
# print(is_prime(100))  # False

# Problem 2: The factorial function

def factorial(n):
    result = n
    if result == 0:
        return 1
    for i in range(1, n):
        result = result * i
    return result

print(factorial(5))
print(factorial(0))

# smarter version
def factorial(n):
    result = 1                  # start at 1, not n
    for i in range(1, n+1):     # loop all the way to n
        result = result * i
    return result

