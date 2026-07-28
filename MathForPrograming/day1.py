# def is_odd(n):
#     return (n&1) == 1
#
# print(is_odd(5))

# Q.find a unique number from a list where other number appear twice
# list = [2,3,3,4,2,6,4]
# def unique_no():
#     unique = 0
#     for i in list:
#         unique ^= i
#     return unique
# print(unique_no())

# Q.find a unique number from a list where other number appear thrice
# list = [2,3,2,4,2,4,4,5,5,5]
#
# def unique_no():
#     for i in list:
#         i += i
#     return i%3
# print(unique_no())


def magic_number():
    n = 3
    ans = 0
    base = 5
    while(n>0):
        last = n & 1
        n = n >> 1
        ans += last * base
        base = base * 5
    print(ans)
magic_number()

