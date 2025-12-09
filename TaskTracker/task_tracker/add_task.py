from task_tracker.task import Task
from task_tracker.utils import load_tasks, save_task
import random
from task_tracker.utils import TASK_ID_LIMIT


def add_task(description: str) -> Task :
    tasks = load_tasks()

    task_id = generate_task_id(tasks)
    task = Task(task_id, description)

    tasks.append(task.to_dict())

    task_saved = save_task(tasks)
    if task_saved:
        print(f'Task with id {task_id} successfully saved.')
    return task    

def generate_task_id(tasks: list[dict]) -> int:
    existing_ids = {task["id"] for task in tasks}

    while True:
        task_id = random.randint(1, TASK_ID_LIMIT)
        if task_id not in existing_ids:
            return task_id
        
