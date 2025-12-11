from task_tracker.mark_task_todo import mark_task_todo

def handle_mark_todo(parts: list[str]) -> bool:
    if len(parts) < 2:
        print('Usage: marke_todo <id>')
        return False
    else:
        try:
            task_id = int(parts[1])
            mark_task_todo(task_id)
            return True
        except ValueError:
            print('Please provide a valid task id')
            return False

        
