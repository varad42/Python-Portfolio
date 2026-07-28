# Lesson 15: The Guessing Game — while True + break 🎲

# import random
#
# secret = random.randint(1, 50)
# print("I'm thinking of a number between 1 and 50...")
#
# tries = 0
# while True:
#     tries += 1
#     guess = int(input("Your guess: "))
#
#     if guess == secret:
#         print("Great you took " + str(tries) + " tries to guess")
#         break
#     elif guess < secret:
#         print("try a higherrr one")
#     else:
#         print("try a lowerrr one")
