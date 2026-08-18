# def power(base, exponent):
#     answer = base
#     if exponent == 0:
#         return 1
#     else:
#         while exponent != 1:
#             answer = answer * base
#             exponent = exponent - 1
#     return answer


def power(base, exponent):
    answer = 1                      # empty accumulator
    while exponent != 0:
        answer = answer * base
        exponent = exponent - 1
    return answer

print(power(2, 5))
print(power(3, 3))
print(power(10, 0))

