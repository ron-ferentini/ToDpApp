tasks = []
runApp = True

def addTask():
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

def viewTasks():
    global tasks
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

def removeTask():
    global tasks
    if len(tasks) == 0:
        print("No tasks to remove.")
        print()
        return
    viewTasks()
    
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
        
while runApp:
    
    try:
        print("To-Do Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Quit")
        menuSelection = input("What do you want to do? ")

        if menuSelection == "1":
            addTask()
        elif menuSelection == "2":
            viewTasks()
        elif menuSelection == "3":
            removeTask()
        elif menuSelection == "4":
            runApp = False
            print("Quitting...")
    except TypeError:
        print("Error: Invalid input type.")
    except Exception as e:
        print(f"Error: {e}")