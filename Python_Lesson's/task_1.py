# import storage
# class Task:
#     def __init__(self, name):
#         self.name = name
#         self.done = False
#
#     def complete(self):
#         self.done = True
#
#     def display(self):
#         if self.done:
#             return "[X] " + self.name
#         return "[ ] " + self.name
#
#     def rename(self, new_name):
#         self.name = new_name
#
#     def to_dict(self):
#         return {"task": self.name, "done": self.done}
#
#
#
# t1 = Task("study")
# t2 = Task("eat")
# t3 = Task("run")
#
#
# todos = storage.load_tasks()
# import storage
# class Task:
#     def __init__(self, name):
#         self.name = name
#         self.done = False
#
#     def complete(self):
#         self.done = True
#
#     def display(self):
#         if self.done:
#             return "[X] " + self.name
#         return "[ ] " + self.name
#
#     def rename(self, new_name):
#         self.name = new_name
#
#     def to_dict(self):
#         return {"task": self.name, "done": self.done}
#
#
#
# t1 = Task("study")
# t2 = Task("eat")
# t3 = Task("run")
# t1.to_dict()
# t2.to_dict()
# t3.complete()
# t3.to_dict()
#
#
# todos = storage.save_tasks()


def run():
    import storage
    from task import Task, UrgentTask
    from datetime import date

    todos = storage.load_tasks()          # objects come back, ready to use

    while True:
        print("\n---My TODO APP---")
        print("1.Add the task")
        print("2.Show tasks")
        print("3.Quit")
        print("4.Remove task")
        print("5.Mark done")
        choice = input("Choose (1/2/3/4/5): ")

        if choice == "1":
            name = input("New task: ")
            # todos.append(Task(name))      # birth! __init__ handles the rest
            # print("Added!")
            urgent = input("Urgent? (yes/no): ")
            if urgent == "yes":
                deadline = input("ENTER A DEADLINE IN YYYY-MM-DD: ")
                todos.append(UrgentTask(name, deadline))
            else:
                todos.append(Task(name))

        elif choice == "2":
            if not todos:
                print("No tasks yet!")
            else:
                for item in todos:
                    print(item.display())   # the class does the checkbox work

        elif choice == "3":
            storage.save_tasks(todos)     # border crossing handled inside
            print("Goodbye!")
            break

        elif choice == "4":
            name = input("Which task to remove? ")
            found = False
            for item in todos:
                if item.name == name:     # .name instead of ["task"]
                    todos.remove(item)
                    found = True
                    print("Removed task")
                    break
            if not found:
                print("Non-existent task")

        elif choice == "5":
            if not todos:
                print("No tasks to complete")
            else:
                name = input("Which task to complete: ")
                found = False
                for item in todos:
                    if item.name == name:
                        item.complete()   # the object flips itself
                        found = True
                        print("Marked done!")
                        break
                if not found:
                    print("Non-existent task")

        else:
            print("Pick 1,2,3,4 or 5!")