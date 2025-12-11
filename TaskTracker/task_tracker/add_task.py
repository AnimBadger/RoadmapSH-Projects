from task_tracker.task import Task
from task_tracker.utils import load_tasks, save_task, generate_task_id


def add_task(description: str) -> Task :
    tasks = load_tasks()

    task_id = generate_task_id(tasks)
    task = Task(task_id, description)

    tasks.append(task.to_dict())

    task_saved = save_task(tasks)
    if task_saved:
        print(f'Task with id {task_id} successfully saved.')
    return task    
