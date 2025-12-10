from task_tracker.list_tasks import list_tasks

def handle_list(parts: list):
    if len(parts) > 2:
        print('Usage: list')
        
    list_tasks()
