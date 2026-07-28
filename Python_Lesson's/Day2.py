# Lesson 9: Lists — boxes with labels

# animals = ["wolf","dinosaur","spider"]
# print(animals[0])
# print(animals)
# animals.remove("spider")
# print(len(animals))
# for animal in animals:
#     print("I love " + animal + "s!")



favorite_food = ["Chicken","Frankie","Shawarma","Biryani"]
# print(favorite_food)
# print(favorite_food[0])
# print(favorite_food[3])
# for food in favorite_food:
#     print("Yum, " + food + "!")
# print("My list has " + str(len(favorite_food)) + " foods")
#
# favorite_food.append("Vadapav")
# favorite_food.remove("Frankie")
# print(favorite_food)


# Lesson 10: Dictionaries — boxes with labels

# person = {
#     "name": "Varad",
#     "age": 21,
#     "favorite_color": "green"
# }
# print(person["name"])
# print(person["favorite_color"])
#
# person["age"] = 22        # happy birthday
# person["pet"] = "wolf"
# del person["favorite_color"]
# print(person)

# Me = {"name": "Varad","age": 1,"city": "newyork","hobby": "singing"}
# print(Me["name"])
# print(Me["hobby"])
# Me["age"] = 2
# Me["favorite_food"] = ["Chicken","Frankie","Shawarma","Biryani"]
# print(Me)
# del Me["city"]
# print(Me["city"])



# Lesson 11: Functions — BUILD YOUR OWN MACHINE


# def greet():
#     print("Hello there!")
#     print("Welcome to my program!")
#
# greet()

# def greet(name):
#     print("Hello, " + name + "!")
#
# greet("Varad")
# greet("Wolf")
# greet("Rahul")
#
# # def double(number):
# #     return number * 2
# #
# # result = double(5)
# # print(result)        # 10
#
# def square(number):
#     return number*number
#
# answer = square(4)
# print(answer)
# answer = square(9)
# print(answer)
#
# Me = {"name": "Varad","age": 1,"city": "newyork","hobby": "singing"}
#
# def describe(person):
#     print(person["name"] + " is " + str(person["age"]) + " years old")
#
# describe(Me)


# Lesson 12 preview: Loops + Dictionaries, the dream team
# marks = {"math": 95, "science": 88, "english": 76}
#
# for subject in marks:
#     print(subject + ": " + str(marks[subject]))
#
# print(marks.keys())     # all the labels
# print(marks.values())   # all the contents
#
# for subject, score in marks.items():
#     print(subject + ": " + str(score))


# marks = {"math": 75,"sci": 50,"geo": 90,"his": 100}
#
# for subject, score in marks.items():
#     print(subject + ": " + str(score))
#
# print(marks.keys())
# print(marks.values())
#
# for subject, score in marks.items():
#     if score >= 90:
#         print(subject + ": A")
#     elif score >= 75:
#         print(subject + ": B")
#     else:
#         print(subject + ": C")
#
# def total(dic):
#     total = 0
#     for subject, score in dic.items():
#         total += score
#     return total
#
#
# total_marks = total(marks)
# print(total({"art": 50}))
# print(total_marks)

# Lesson 13: String powers

# name = "Varad"
#
# print(name.upper())    # VARAD
# print(name.lower())    # varad
# print(len(name))       # 5 — old friend len works on text too!
#
# word = "dinosaur"
#
# print(word[0])      # d      (position 0, of course!)
# print(word[0:4])    # dino   (from 0 up to but NOT including 4 — range rules again!)
# print(word[4:])     # saur   (from 4 to the end)
# print(word[-1])     # r      (minus = count from the END! -1 is the last letter)
#
# print("dino" in word)     # True
# print("cat" in word)      # False
#
# messy = "   hello   "
# print(messy.strip())      # hello

# name = "Varad"
# print(name.upper())
# print(name.lower())
# print(len(name))
#
# word = "programing"
# print(word[0])
# print(word[-1])
# print(word[0:7])
#
# word = input("Type a word ")
# if "a" in word:
#     print("Their is letter a inside the word")
# else:
#     print("No a found out")
#
# username = input("Enter your name ")
# print(username.strip().lower())

# Lesson 14: True/False — Booleans, the tiny truth machines ⚖️
#
# print(5 > 3)
# print(5 == 6)
# print("a" in "cat")
#
# is_hungry = True
# is_sleepy = False
#
# if is_hungry:
#     print("Go eat something!")
#
# age = 21
# has_ticket = True
#
# # and → BOTH must be true
# if age >= 18 and has_ticket:
#     print("Enter the concert!")
#
# # or → at LEAST ONE must be true
# if age < 3 or age > 90:
#     print("Free entry!")
#
# # not → flips the truth
# if not has_ticket:
#     print("Go buy a ticket first!")

# print(10 > 5 and 3 > 1)
# print(10 > 5 and 3 > 100)
# print(10 > 5 or 3 > 100)
# print(not 10 > 5)
# print(5 == 5 and not 2 > 3)
#
# age = int(input("What is your age "))
# have_a_ticket = input("Do you have a ticket")
# if age >= 12 and have_a_ticket == "yes":
#     print("yes")
# else:
#     print("No")

# for i in range(1, 21):
#     if i % 3 == 0 or i % 5 == 0:
#         print("i")
#     else:
#         print("Not special")

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

# Lesson 16: The TODO App — your first real software

todos = []

while True:
    print("---My TODO APP---")
    print("1.Add the task")
    print("2.Show tasks")
    print("3.Quit")
    print("4.Remove task")
    choice = input("Choose (1/2/3/4): ")

    if choice == "1":
        task = input("New task:")
        todos.append(task)
        print("Added!")
    elif choice == "2":
        if not todos:
            print("No tasks yet!")
        for task in todos:
            print("- " + task)
    elif choice == "3":
        print("Goodbye!")
        break
    elif choice == "4":
        task = input("Which task to remove ")
        if not todos:
            print("No tasks to remove")
        elif task not in todos:
            print("Non-existent task")

        elif task in todos:
            todos.remove(task)
            print("Removed task")

    else:
        print("Pick 1,2,3 or 4!")