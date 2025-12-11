from task_tracker.update_task import update_task

def handle_update(parts: list[str]) -> bool:
    if len(parts) < 2:
        print('Usage: update <id> <new description>')
        return False

    try:
        id_part, description = parts[1].split(' ', 1)
        task_id = int(id_part)
        update_task(task_id, description)
        return True
    except ValueError:
        print('Please provide a valid task id.')
        return False