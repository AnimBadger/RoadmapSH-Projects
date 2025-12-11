from task_tracker.utils import load_tasks, save_task

def mark_task_todo(task_id: int) -> bool:
    tasks = load_tasks()

    for task in tasks:
        if task['id'] == task_id:
            # not already todo or not done
            if task['status'] == 'todo' or task['status'] == 'done':
                print(f'Task with id {task_id} should be in progress')
                return False
            task['status'] = 'todo'
            save_task(tasks)
            print(f'Task with id {task_id} marked successful')
            return True
    print('No tasks found')
    return False
