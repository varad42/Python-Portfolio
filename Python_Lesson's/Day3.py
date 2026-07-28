# Lesson 17: Files — programs that REMEMBER 💾
# file = open("notes.txt", "w")
# file.write("Hello, file!")
# file.close()

# file = open("notes.txt", "r")
# content = file.read()
# file.close()
# print(content)
#
# file = open("notes.txt", "a")
# file.write("\nAnother line")     # \n = new line, remember!
# file.close()

# with open("notes.txt", "r") as file:
#     content = file.read()
# print(content)

# with open("ghost.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("foods.txt","w")
# file.write("Vadapav\nShawarma\nCake\nBiryani")
# file.close()
#
# with open("foods.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("oods.txt","r")

# ========== STARTUP: LOAD (runs ONCE, before the loop) ==========
# with open("todos.txt", "r") as file:
#     content = file.read()
#
# if content:                        # file has text → unfold it into a list
#     todos = content.split("\n")
# else:                              # file exists but is empty → start fresh
#     todos = []                     # (without this, split gives [""] — a ghost task!)
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")

# Lesson 18: try / except — the airbags 🪂
# try:
#     with open("todos.txt", "r") as file:
#         content = file.read()
#
#     if content:
#         todos = content.split("\n")
#     else:
#         todos = []
# except FileNotFoundError:
#     todos = []
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")
#

# Lesson 17: Files — programs that REMEMBER 💾
# file = open("notes.txt", "w")
# file.write("Hello, file!")
# file.close()

# file = open("notes.txt", "r")
# content = file.read()
# file.close()
# print(content)
#
# file = open("notes.txt", "a")
# file.write("\nAnother line")     # \n = new line, remember!
# file.close()

# with open("notes.txt", "r") as file:
#     content = file.read()
# print(content)

# with open("ghost.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("foods.txt","w")
# file.write("Vadapav\nShawarma\nCake\nBiryani")
# file.close()
#
# with open("foods.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("oods.txt","r")

# ========== STARTUP: LOAD (runs ONCE, before the loop) ==========
# with open("todos.txt", "r") as file:
#     content = file.read()
#
# if content:                        # file has text → unfold it into a list
#     todos = content.split("\n")
# else:                              # file exists but is empty → start fresh
#     todos = []                     # (without this, split gives [""] — a ghost task!)
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")

# Lesson 18: try / except — the airbags 🪂
# try:
#     with open("todos.txt", "r") as file:
#         content = file.read()
#
#     if content:
#         todos = content.split("\n")
#     else:
#         todos = []
# except FileNotFoundError:
#     todos = []
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")
#

# Lesson 17: Files — programs that REMEMBER 💾
# file = open("notes.txt", "w")
# file.write("Hello, file!")
# file.close()

# file = open("notes.txt", "r")
# content = file.read()
# file.close()
# print(content)
#
# file = open("notes.txt", "a")
# file.write("\nAnother line")     # \n = new line, remember!
# file.close()

# with open("notes.txt", "r") as file:
#     content = file.read()
# print(content)

# with open("ghost.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("foods.txt","w")
# file.write("Vadapav\nShawarma\nCake\nBiryani")
# file.close()
#
# with open("foods.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("oods.txt","r")

# ========== STARTUP: LOAD (runs ONCE, before the loop) ==========
# with open("todos.txt", "r") as file:
#     content = file.read()
#
# if content:                        # file has text → unfold it into a list
#     todos = content.split("\n")
# else:                              # file exists but is empty → start fresh
#     todos = []                     # (without this, split gives [""] — a ghost task!)
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")

# Lesson 18: try / except — the airbags 🪂
# try:
#     with open("todos.txt", "r") as file:
#         content = file.read()
#
#     if content:
#         todos = content.split("\n")
#     else:
#         todos = []
# except FileNotFoundError:
#     todos = []
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")
#

# Lesson 17: Files — programs that REMEMBER 💾
# file = open("notes.txt", "w")
# file.write("Hello, file!")
# file.close()

# file = open("notes.txt", "r")
# content = file.read()
# file.close()
# print(content)
#
# file = open("notes.txt", "a")
# file.write("\nAnother line")     # \n = new line, remember!
# file.close()

# with open("notes.txt", "r") as file:
#     content = file.read()
# print(content)

# with open("ghost.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("foods.txt","w")
# file.write("Vadapav\nShawarma\nCake\nBiryani")
# file.close()
#
# with open("foods.txt", "r") as file:
#     content = file.read()
# print(content)

# file = open("oods.txt","r")

# ========== STARTUP: LOAD (runs ONCE, before the loop) ==========
# with open("todos.txt", "r") as file:
#     content = file.read()
#
# if content:                        # file has text → unfold it into a list
#     todos = content.split("\n")
# else:                              # file exists but is empty → start fresh
#     todos = []                     # (without this, split gives [""] — a ghost task!)
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")

# Lesson 18: try / except — the airbags 🪂
# try:
#     with open("todos.txt", "r") as file:
#         content = file.read()
#
#     if content:
#         todos = content.split("\n")
#     else:
#         todos = []
# except FileNotFoundError:
#     todos = []
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     choice = input("Choose (1/2/3/4): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         todos.append(task)         # add to the LIVE list. That's ALL. No file!
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         for task in todos:
#             print("- " + task)
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         with open("todos.txt", "w") as file:
#             file.write("\n".join(todos))   # fold the list into clean lines
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         if not todos:
#             print("No tasks to remove")
#         else:
#             task = input("Which task to remove? ")
#             if task in todos:
#                 todos.remove(task)     # again: LIST only. File stays asleep.
#                 print("Removed task")
#             else:
#                 print("Non-existent task")
#
#     else:
#         print("Pick 1,2,3 or 4!")
#

import random

secret = random.randint(1, 50)
print("I'm thinking of a number between 1 and 50...")

tries = 0
while True:
    try:  # ← risky zone begins
        guess = int(input("Your guess: "))
    except ValueError:  # ← catch ONLY this beast
        print("Numbers only, please!")
        continue  # ← skip the ifs, back to top

    tries += 1

    if guess == secret:
        print("Great! You took " + str(tries) + " tries to guess")
        break
    elif guess < secret:
        print("try a higherrr one")
    else:
        print("try a lowerrr one")
