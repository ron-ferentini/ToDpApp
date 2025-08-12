from add_task import add_task
from view_tasks import view_tasks
from remove_task import remove_task

def main():
    tasks = []
    runApp = True
    while runApp:
    
        try:
            print("To-Do Application")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Remove Task")
            print("4. Quit")
            menuSelection = input("What do you want to do? ")

            if menuSelection == "1":
                tasksadd_task(tasks)
            elif menuSelection == "2":
                view_tasks(tasks)
            elif menuSelection == "3":
                tasks = remove_task(tasks)
            elif menuSelection == "4":
                runApp = False
                print("Quitting...")
        except TypeError:
            print("Error: Invalid input type.")
        except Exception as e:
            print(f"Error: {e}")
            
if __name__ == "__main__":
    main()