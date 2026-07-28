# Lesson 22, first of the intermediate arc: List Comprehensions ⚡

# numbers = [1,2,3,4,5]
#
# tripled = []
# for t in numbers:
#     tripled.append(t*3)
# print(tripled)
#
# tripled_short = [n*3 for n in numbers]
# print(tripled_short)
#
# letters = ["a","b","c"]
#
# capital_letters = [(n + "!").upper() for n in letters]
# print(capital_letters)
#
# # Long version — the if lives INSIDE the loop:
# evens = [1,2,3]
# for n in numbers:
#     if n % 2 == 0:
#         evens.append(n)
# print(evens)
#
# # Short version — the if moves to the END of the line:
# evens = [n for n in numbers if n % 2 == 0]
# print(evens)


squares = [n * n for n in range(1, 11)]
print(squares)

words = ["hi","claude","how","are","you"]

print([n.upper() for n in words])

print([i for i in range(1, 51) if i%3 == 0 or i%5 == 0])
