from task_tracker.mark_task_in_progress import mark_task_in_progress

def handle_mark_in_progress(parts: list[str]):
    if len(parts) < 2:
        print('Usage: mark-in-progress <id>')
        try:
            print(parts[1])
            task_id = int(parts[1])
            mark_task_in_progress(task_id)
        except ValueError:
            print('Please provide a valid task id')
        
