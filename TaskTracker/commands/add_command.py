from task_tracker.add_task import add_task

def handle_add(parts: list[str]) -> bool:
    if len(parts) < 2:
        print('Usage: add <description>')
        return False

    description = parts[1]
    add_task(description)
    return True