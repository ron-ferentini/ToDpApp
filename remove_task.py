from view_tasks import view_tasks

def remove_task(tasks):
    if len(tasks) == 0:
        print("No tasks to remove.")
        print()
        return
    view_tasks(tasks)

    try:
        print()
        task_number = int(input("Enter task number to remove: "))

        if task_number < 1 or task_number > len(tasks):
            raise ValueError()
        removed = tasks.pop(task_number - 1)
        print(f"Removed task: {removed}")
        print()
        
    except TypeError:
        print("Invalid input. Please enter a number.")
        print
    except ValueError:
        print("Invalid task number no task removed!")
        print()
    finally:
        return tasks