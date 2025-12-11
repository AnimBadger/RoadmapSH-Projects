from task_tracker.delete_task import delete_task

def handle_delete(parts: list[str]) -> bool:
    if len(parts) < 2:
        print('Usage: delete <id>')
        return False

    try:
        task_id = int(parts[1])
        delete_task(task_id)
        return True
    except ValueError:
        print('Please provide a valid task id.')
        return False