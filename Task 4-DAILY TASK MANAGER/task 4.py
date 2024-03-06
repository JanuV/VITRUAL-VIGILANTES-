import os
import json

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return {}

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(date, tasks):
    print(f"Tasks for {date}:\n")
    if date in tasks:
        for index, task in enumerate(tasks[date], start=1):
            print(f"{index}. {task['task']} {'(Completed)' if task['completed'] else ''}")
    else:
        print("No tasks for today.")

def add_task(date, tasks):
    task_description = input("Enter task description: ")
    tasks.setdefault(date, []).append({"task": task_description, "completed": False})
    print("Task added successfully.")

def mark_task_completed(date, tasks):
    display_tasks(date, tasks)
    try:
        task_index = int(input("Enter the task number to mark as completed (0 to cancel): "))
        if task_index == 0:
            return
        task_index -= 1  # Adjust to 0-based index
        tasks[date][task_index]["completed"] = True
        print("Task marked as completed.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def main():
    print("Simple Daily Task Manager\n")

    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        tasks = load_tasks()

        while True:
            print("\nOptions:")
            print("1. View tasks")
            print("2. Add task")
            print("3. Mark task as completed")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                display_tasks(date, tasks)
            elif choice == "2":
                add_task(date, tasks)
            elif choice == "3":
                mark_task_completed(date, tasks)
            elif choice == "4":
                save_tasks(tasks)
                print("Tasks saved. Exiting.")
                return
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
