import sys
import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Task status constants
NOT_DONE = "not done"
IN_PROGRESS = "in progress"
DONE = "done"

# Ensure the task file exists
def initialize_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)

# Load tasks from the JSON file
def load_tasks():
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

# Save tasks to the JSON file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(title):
    tasks = load_tasks()
    tasks.append({"title": title, "status": NOT_DONE})
    save_tasks(tasks)
    print(f"Task '{title}' added.")

# Update a task's title or status
def update_task(index, new_title=None, new_status=None):
    tasks = load_tasks()
    try:
        task = tasks[int(index)]
        if new_title:
            task["title"] = new_title
        if new_status:
            task["status"] = new_status
        save_tasks(tasks)
        print(f"Task '{task['title']}' updated.")
    except (IndexError, ValueError):
        print("Invalid task index.")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    try:
        removed = tasks.pop(int(index))
        save_tasks(tasks)
        print(f"Task '{removed['title']}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task index.")

# List tasks with optional filtering by status
def list_tasks(status_filter=None):
    tasks = load_tasks()
    filtered_tasks = [t for t in tasks if status_filter is None or t["status"] == status_filter]
    if not filtered_tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(filtered_tasks):
            print(f"{i}. {task['title']} - {task['status']}")

# Command-line interface for task management
def main():
    initialize_file()

    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [options]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "update" and len(sys.argv) >= 4:
        update_task(sys.argv[2], new_title=" ".join(sys.argv[3:]))
    elif command == "status" and len(sys.argv) >= 4:
        update_task(sys.argv[2], new_status=sys.argv[3])
    elif command == "delete" and len(sys.argv) >= 3:
        delete_task(sys.argv[2])
    elif command == "list":
        list_tasks()
    elif command == "list-done":
        list_tasks(DONE)
    elif command == "list-not-done":
        list_tasks(NOT_DONE)
    elif command == "list-in-progress":
        list_tasks(IN_PROGRESS)
    else:
        print("Invalid command or missing arguments.")

if __name__ == "__main__":
    main()
