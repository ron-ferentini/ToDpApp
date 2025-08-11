def add_task():
    global tasks
    try:
        print()
        newTask = input("Enter a new task: ")

        if not newTask.strip():
            raise ValueError()
        tasks.append(newTask)
        print("Task added successfully.")
        print()
    except ValueError:
        print("Invalid input. Task not added.")