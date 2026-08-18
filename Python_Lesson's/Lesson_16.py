
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