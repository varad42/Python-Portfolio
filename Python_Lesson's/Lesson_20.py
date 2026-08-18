


# Lesson 20: Modules — code across multiple files

# Code X
# import storage
# todos = storage.load_todos()
#
# # ========== THE LOOP: only the LIST is touched, never the file ==========
# while True:
#     print("\n---My TODO APP---")
#     print("1.Add the task")
#     print("2.Show tasks")
#     print("3.Quit")
#     print("4.Remove task")
#     print("5.Perform task")
#     choice = input("Choose (1/2/3/4/5): ")
#
#     if choice == "1":
#         task = input("New task: ")
#         new_task = {
#             "task": task,
#             "done": False
#         }
#         todos.append(new_task)
#         print("Added!")
#
#     elif choice == "2":
#         if not todos:
#             print("No tasks yet!")
#         else:
#             for item in todos:
#                 if item["done"]:
#                     print("[X] " + item["task"])
#
#                 else:
#                     print("[ ] " + item["task"])
#
#     elif choice == "3":
#         # ========== QUIT: SAVE (runs ONCE, on the way out) ==========
#         storage.save_todos(todos)
#         print("Goodbye!")
#         break
#
#     elif choice == "4":
#         name = input("Which task to remove? ")
#         found = False
#         for item in todos:
#             if item["task"] == name:
#                 todos.remove(item)
#                 found = True
#                 print("Removed task")
#                 break
#         if not found:  # AFTER the loop — hunt over, verdict time
#             print("Non-existent task")
#     elif choice == "5":
#         if not todos:
#             print("No tasks to perform")
#         else:
#             name = input("Which task to complete: ")
#             for items in todos:
#                 if items["task"] == name:
#                     items["done"] = True
#     else:
#         print("Pick 1,2,3,4 or 5!")

class Task:
    def __init__(self, name):
        self.name = name
        self.done = False

    def complete(self):
        self.done = True

    def display(self):
        if self.done:
            return "[X] " + self.name
        return "[ ] " + self.name

    def rename(self, new_name):
        self.name = new_name

# import json
#
# t = Task("study")
# print(json.dumps(t))
#
#
# t1 = Task("study")
# t2 = Task("sleep")
# t3 = Task("eat")
# t1.complete()
# print(t2.display())
# t2.rename("run")
# print(t1.display())
# print(t2.display())
# print(t3.display())

# t1 = Task("run")
# t2 = Task("run")
# print(t1 == t2)

print(Task("run") == Task("run"))     # predict, then run
print("run" == "run")                  # predict, then run