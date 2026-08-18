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

# def fibonacci(provided_num):
#     result = []
#     a = 0
#     b = 1
#     while len(result) < provided_num:
#         result.append(a)
#         a, b = b, a + b
#     return result
#
# print(fibonacci(7))   # [0, 1, 1, 2, 3, 5, 8]
# print(fibonacci(1))   # [0]
# print(fibonacci(0))   # []
