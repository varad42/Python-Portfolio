# Lesson 22 archive — List Comprehensions ⚡:

numbers = [1, 2, 3]

doubles = []                    # 1. start with an empty list
for n in numbers:               # 2. visit each item
    doubles.append(n * 2)       # 3. transform it, append it

print(doubles)                  # [2, 4, 6]

doubles = [n * 2 for n in numbers]

# Pair 1
squares = [n * n for n in numbers]

# Pair 2 — with tasks
names = [t.name for t in tasks]

# Pair 3 — plain copy
copy = [n for n in numbers]


numbers = [1, 2, 3, 4, 5]

tripled = []
for n in numbers:
    tripled.append(n * 3)
print(tripled)                             # [3, 6, 9, 12, 15]

tripled_short = [n * 3 for n in numbers]
print(tripled_short)                       # [3, 6, 9, 12, 15] — identical



# Long version — if inside the loop:
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)

# Short version — if moves to the END:
evens = [n for n in numbers if n % 2 == 0]      # [2, 4]

big_shouts = [word.upper() for word in words if len(word) > 3]


letters = ["a", "b", "c"]
capital_letters = [(n + "!").upper() for n in letters]
print(capital_letters)                     # ['A!', 'B!', 'C!']

squares = [n * n for n in range(1, 11)]
print(squares)          # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

words = ["hi", "claude", "how", "are", "you"]
print([n.upper() for n in words])          # ['HI', 'CLAUDE', 'HOW', 'ARE', 'YOU']

print([i for i in range(1, 51) if i % 3 == 0 or i % 5 == 0])
# [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48, 50]



