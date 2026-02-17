# To-Do List Application using File Handling

FILE_NAME = "tasks.txt"

def add_task():
    task = input("Enter a new task: ").strip()
    if task == "":
        print("Task cannot be empty.\n")
        return

    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")

    print("Task added successfully.\n")


def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.\n")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
            print()

    except FileNotFoundError:
        print("No tasks found.\n")


def delete_task():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks available to delete.\n")
            return

        view_tasks()

        try:
            task_number = int(input("Enter the task number to delete: "))
        except ValueError:
            print("Invalid input. Please enter a number.\n")
            return

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)

            with open(FILE_NAME, "w") as file:
                file.writelines(tasks)

            print(f"Task deleted: {removed_task.strip()}\n")
        else:
            print("Invalid task number.\n")

    except FileNotFoundError:
        print("No tasks found.\n")


def main_menu():
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


main_menu()
