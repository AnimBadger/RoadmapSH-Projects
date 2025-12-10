from task_tracker.delete_task import delete_task

def handle_delete(parts: list):
    if len(parts) < 2:
        print('Usage: delete <id>')
        return

    try:
        task_id = int(parts[1])
    except ValueError:
        print('Please provide a valid task id.')
        return

    delete_task(task_id)