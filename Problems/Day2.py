# Write reverse_number(n) that reverses the digits of an integer.
# def reverse_num(num):
#     result = 0
#     while num != 0:
#         last_digit = num%10
#         result = result * 10 + last_digit
#         num = num//10
#     return result
#
# print(reverse_num(4156))


# Q.4 Write is_palindrome(n) that returns True if a number reads the same forwards and backwards.

# def ispalindrome(num):
#     result = 0
#     provided_number = num
#     while num != 0:
#         last_digit = num%10
#         result = result * 10 +last_digit
#         num = num // 10
#     return result == provided_number
# print(ispalindrome(123))
# print(ispalindrome(121))

# Q.5 Write digit_sum(n) that returns the sum of a number's digits.

# def digit_sum(num):
#     result = 0
#     while num!=0:
#         last_digit = num%10
#         num = num // 10
#         result = last_digit + result
#     return result
#
# print(digit_sum(0))

# Q.6 Write fibonacci(n) that returns the first n numbers of the Fibonacci sequence as a list (each number is the sum of the previous two).
#
# def fibonacci(provided_num):
#     result = []
#     a = 0
#     b = 1
#     temp = 0
#     while len(result) < provided_num:
#         result.append(a)
#         temp = a
#         a = b
#         b = a + 1
#     return result
#
# print(fibonacci(7))

def fibonacci(provided_num):
    result = []
    a = 0
    b = 1
    while len(result) < provided_num:
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(7))   # [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(1))   # [0]
print(fibonacci(0))   # []

# Q.7 Print numbers 1 to 50, but: for multiples of 3 print "Fizz", multiples of 5 print "Buzz", multiples of both print "FizzBuzz".

# def fizzbuzz(num):
#     for i in range(1, n+1):
#         if i%3 == 0 and i%5 == 0:
#             print("FizzBuzz")
#         elif i%3 == 0:
#             print("Fizz")
#         elif i%5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# fizzbuzz(50)


# Q.8 A number is an Armstrong number if the sum of each digit raised to the power of the digit-count equals the number itself. E.g. 153 has 3 digits: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓

