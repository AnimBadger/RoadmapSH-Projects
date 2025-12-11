from task_tracker.utils import load_tasks, TASK_FILE
import os

def list_tasks() -> list:
    tasks = load_tasks()
    print("\nYour Tasks:\n" + "-"*50)
    for task in tasks:
        print(f"ID       : {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status     : {task['status']}")
        print(f"Created At : {task['createdAt']}")
        print(f"Updated At : {task['updatedAt']}")
        print("-"*50)
    return tasks