from task_tracker.utils import load_tasks, save_task
import os

def delete_task(task_id: int) -> bool :
    """
    Delete a task by ID.

    :param task_id: ID of the task to delete
    :return: True if deleted, False if not found
    """
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            save_task(tasks)
            print('Task successfully removed')
            return True
        
    print(f'Task with id {task_id} not found')
    return False