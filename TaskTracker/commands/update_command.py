from task_tracker.update_task import update_task

def handle_update(parts):
    if len(parts) < 2:
        print('Usage: update <id> <new description>')
        return

    try:
        id_part, description = parts[1].split(' ', 1)
        task_id = int(id_part)
    except ValueError:
        print('Please provide a valid task id.')
        return

    update_task(task_id, description)