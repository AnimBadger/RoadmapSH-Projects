from task_tracker.task import Task
import os
import random
import json

TASK_FILE = 'tasks.json'

def add_task(description: str) -> Task :
    tasks = load_tasks()

    task_id = generate_task_id(tasks)
    task = Task(task_id, description)

    tasks.append(task.to_dict())

    save_task(tasks)
    return task


def load_tasks() -> list:
    # If file doesn't exist, create it with an empty list
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file, indent=2)
        return []

    # If file exists, load the tasks
    with open(TASK_FILE, 'r') as file:
        return json.load(file)
    

def generate_task_id(tasks: list[dict]) -> int:
    existing_ids = {task["id"] for task in tasks}

    while True:
        task_id = random.randint(1, 9999)
        if task_id not in existing_ids:
            return task_id
        
def save_task(task: list[dict]):
    with open(TASK_FILE, 'w') as file:
        json.dump(task, file, indent=2)
        print('Successfully added task.')