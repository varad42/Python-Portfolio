# Lesson 19: JSON — saving STRUCTURED data 📦
# import json
#
# with open("todos.json", "w") as file:
#     json.dump(todos, file)
#
# with open("todos.json", "r") as file:
#     todos = json.load(file)





# import json
# try:
#     with open("todos.json", "r") as file:
#         todos = json.load(file)
#     # if content:
#     #     todos = content.split("\n")
#     # else:
#     #     todos = []
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
#         with open("todos.json", "w") as file:
#             json.dump(todos, file)   # fold the list into clean lines
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
