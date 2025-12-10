from task_tracker.add_task import add_task

def handle_add(parts: list):
    if len(parts) < 2:
        print('Usage: add <description>')
        return

    description = parts[1]
    add_task(description)