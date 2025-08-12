def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks available.")
        print()
    else:
        try:
            print("Current Tasks:")
            for i, task in enumerate(tasks, 0):
                print(f"{i + 1} - {task}")
            print()
        except TypeError:
            print("Error: Invalid task list.")
        except Exception as e:
            print(f"Error: {e}")