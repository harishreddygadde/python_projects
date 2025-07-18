# to-do-listapp.py 'using Python'

tasks = []

def show_menu():
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            print("Your tasks:")
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for idx, task in enumerate(tasks, 1):
                print(f"{idx}. {task}")
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")