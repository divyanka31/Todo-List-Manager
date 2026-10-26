
import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Could not read tasks file. Starting empty.")
    return []


def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def view_tasks():
    if not tasks:
        print("\nNo tasks yet!")
        return

    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['title']} [{status}]")


def add_task():
    title = input("Enter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return

    tasks.append({"title": title, "done": False})
    save_tasks()
    print("Task added!")


def complete_task():
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Task number to complete: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            save_tasks()
            print("Task completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")


def delete_task():
    view_tasks()
    if not tasks:
        return

    try:
        number = int(input("Task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            save_tasks()
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")


tasks = load_tasks()

while True:
    print("\n=== To-Do List Manager ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
