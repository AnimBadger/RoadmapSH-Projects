from commands import *
from task_tracker.mark_task_in_progress import mark_task_in_progress

def show_help():
    print("""
    Task Tracker CLI
    ================
    A simple command-line tool to manage your tasks.

    Available Commands
    ------------------
    add <description>
    Add a new task
    Example: add Buy groceries

    update <id> <new description>   
    Update an existing task
    Example: update 1 Buy groceries and cook

    delete <id>
    Delete a task
    Example: delete 1

    list
    List all tasks

    mark <id> <todo|in-progress|done>
    Mark a task's status
    Example: mark 1 done

    help
    Show this help menu

    exit
    Exit the application
""")

def main():
    """
    Entry point of the application
    """
    show_help()
    running = True

    COMMAND_HANDLERS = {
        "add": handle_add,
        "update": handle_update,
        "delete": handle_delete,
        "list": handle_list,
        "mark_in_progress": mark_task_in_progress
    }

    while running:
        user_input = input("\n> ").strip()

        if not user_input:
            continue

        parts = user_input.split(" ", 1)
        command = parts[0].lower()

        # handle exit
        running = handle_command(command)
        if not running:
            print("Goodbye 👋")
            break

        # execute command handler
        handler = COMMAND_HANDLERS.get(command)
        if handler:
            handler(parts)
        else:
            print(f"Unknown command: {command}")
    
def handle_command(command: str) -> bool:
    return command != "exit"
    
if __name__ == '__main__':
    main()
