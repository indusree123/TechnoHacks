def add_task(todo_list):
    task = input("Enter the task to add: ")
    priority = input("Enter the priority of the task (High, Medium, Low): ")
    todo_list[task] = priority
    print(f"Task '{task}' added successfully.")

def remove_task(todo_list):
    task = input("Enter the task to remove: ")
    if task in todo_list:
        del todo_list[task]
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks(todo_list):
    if todo_list:
        print("Tasks:")
        for task, priority in todo_list.items():
            print(f"- {task} (Priority: {priority})")
    else:
        print("No tasks found.")

def main():
    todo_list = {}

    while True:
        print("To-Do List")
        print("----------")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = int(input("Enter your choice (1, 2, 3, or 4): "))

        if choice == 1:
            add_task(todo_list)
        elif choice == 2:
            remove_task(todo_list)
        elif choice == 3:
            view_tasks(todo_list)
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


main()

               
