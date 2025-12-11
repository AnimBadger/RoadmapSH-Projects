from task_tracker.utils import load_tasks, save_task


def mark_task_in_progress(task_id: int) -> bool:
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if task['status'] == 'in-progress':
                print(f'Task with id {task_id} is already in progress')
                return False
            task['status'] = 'in-progress'
            save_task(tasks)
            print(f'Task with id {task_id} is in progress')
            return True
    print(f'Task with id {task_id} not found')
    return False