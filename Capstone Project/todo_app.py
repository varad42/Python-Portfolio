import storage_1
from task import Task, UrgentTask
import random


quotes = [
    "Small steps every day lead to big results.",
    "The secret of getting ahead is getting started.",
    "Don't watch the clock; do what it does. Keep going.",
    "Success is the sum of small efforts repeated daily.",
    "Today's progress is tomorrow's achievement."
]

def show_quote():
    print(random.choice(quotes))
def run():


    todos = storage_1.load_tasks()  # objects come back, ready to use

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
                    print(item.display())  # the class does the checkbox work

        elif choice == "3":
            storage_1.save_tasks(todos)  # border crossing handled inside
            print("Goodbye!")
            break

        elif choice == "4":
            name = input("Which task to remove? ")
            found = False
            for item in todos:
                if item.name == name:  # .name instead of ["task"]
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
                        item.complete()  # the object flips itself
                        found = True
                        print("Marked done!")
                        break
                if not found:
                    print("Non-existent task")

        else:
            print("Pick 1,2,3,4 or 5!")

def show_tasks():
    todos = storage_1.load_tasks()
    for item in todos:
        print(item.display())