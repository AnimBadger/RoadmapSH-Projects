from task_tracker.utils import load_tasks, save_task

def mark_task_done(task_id: int) -> bool:
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == task_id:
            if task['status'] == 'done':
                print(f'Task with id {task_id} is already completed.')
                return False
            elif task['status'] == 'todo':
                print(f'Task with id {task_id} must be in progress.')
                return False
            else:
                task['staus'] = 'done'
                save_task(task)
                print(f'Task with id {task_id} completed.')
                return True
    print(f'Task with id {task_id} not found')
    return False
