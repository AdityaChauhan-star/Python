#                                    TASK 1

#                                  TO-DO LIST

#  A To-Do List application is a useful project that helps users manage and organize
#  their tasks efficiently. This project aims to create a command-line or GUI-based
#  application using Python, allowing users to create, update, and track their
#  to-do lists


tasks = []

def display_menu():
    print("===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save To-Do List")
    print("6. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found. Add tasks to the list.")
    else:
        print("===== To-Do List =====")
        for index, task in enumerate(tasks, 1):
            status = "✔" if task["completed"] else " "
            print(f"{index}. [{status}] {task['task']}")

def mark_task_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    except IndexError:
        print("Invalid task number. Please try again.")

def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task['task']}' deleted successfully!")
    except IndexError:
        print("Invalid task number. Please try again.")

def save_to_file():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['completed']}\n")
    print("To-Do List saved to 'tasks.txt'!")

def load_from_file():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task, completed = line.strip().split("|")
                tasks.append({"task": task, "completed": completed == "True"})
        print("To-Do List loaded from 'tasks.txt'!")
    except FileNotFoundError:
        print("No saved To-Do List found. Start adding tasks!")

def main():
    load_from_file()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
