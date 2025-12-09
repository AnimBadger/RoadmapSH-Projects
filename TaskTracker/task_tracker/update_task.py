from task_tracker.utils import TASK_FILE
import os
import json
from datetime import datetime
def update_task(task_id: int, new_description: str):
    if not os.path.exists(TASK_FILE):
        print('No tasks found')
        return None
    
    with open(TASK_FILE, 'r') as file:
        tasks = json.load(file)

    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()

            with open(TASK_FILE, 'w') as file:
                json.dump(tasks, file, indent=2)
                print(f'Task id {task_id} updated successfully')
            return task
        
    print(f'Task with id {task_id} not found.')
    return None
        
