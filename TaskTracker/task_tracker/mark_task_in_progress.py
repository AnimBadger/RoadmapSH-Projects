from task_tracker.utils import TASK_FILE, save_task
import os
import json

def mark_task_in_progress(task_id: int) -> bool:
    if not os.path.exists(TASK_FILE):
        print('No tasks found')
        return False
    
    with open(TASK_FILE, 'r') as file:
        tasks = json.load(file)

    for task in tasks:
        if task['id'] == task_id:
            if task['status'] == 'in-progress':
                print(f'Task with id {task_id} is already in progress')
            task['status'] = 'in-progress'
            save_task(tasks)
            return True
    print(f'Task with id {task_id} not found')
    return False