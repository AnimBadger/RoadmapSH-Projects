from task_tracker.utils import load_tasks, save_task
from datetime import datetime

def update_task(task_id: int, new_description: str):
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            if save_task(tasks):
                print(f'Task id {task_id} updated successfully')
            return task
        
    print(f'Task with id {task_id} not found.')
    return None
        
