from task_tracker.list_tasks import list_tasks

def handle_list(parts: list[str]) -> bool:
    if len(parts) > 2:
        print('Usage: list')
        return False
        
    list_tasks()
    return True
