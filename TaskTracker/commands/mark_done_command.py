from task_tracker.mark_task_done import mark_task_done

def handle_mark_done(parts: list[str]):
    if len(parts) < 2:
        print('Usage: mark-in-progress <id>')
        return False
    else:
        try:
            task_id = int(parts[1])
            mark_task_done(task_id)
            return True
        except ValueError:
            print('Please provide a valid task id')
        