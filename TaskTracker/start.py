from task_tracker.add_task import add_task
from task_tracker.update_task import update_task 
from task_tracker.delete_task import delete_task
from task_tracker.list_tasks import list_tasks

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
    Docstring for main
    Entry point of application
    """
    show_help()
    running = True
    while running:
        user_input = input('\n> ').strip()

        if not user_input:
            continue

        parts = user_input.split(' ', 1) # split only once
        command = parts[0].lower() # add
        #parts[1] - id description description

        running = handle_command(command)
        if not running:
            print("Goodbye 👋")
              
        try:
            if command == 'add':
                if len(parts) < 2:
                    print('Usage: add <description>')
                    continue

                description = parts[1] # everything after add because of the split
                add_task(description)

            elif command == 'update':
                if len(parts) < 2:
                    print('Usage: update <id> <new description>')
                    continue
                try:
                    id_part, description = parts[1].split(' ', 1)
                    task_id = int(id_part)
                except ValueError:
                    print('Please provide a valid task id.')
                    continue

                update_task(task_id, description)
            
            elif command == 'delete':
                if len(parts) < 2:
                    print(f'Usage: delete <id>')
                    continue
                try:
                    task_id = int(parts[1])
                except ValueError:
                    print('Please provide a valid task id')
                    continue

                delete_task(task_id)

            elif command == 'list':
                list_tasks()
                    


        except (IndentationError, ValueError):
            print("Invalid command format. Type 'help for usage.'")
    
    
def handle_command(command: str) -> bool:
    return command.strip().lower() != 'exit'

    
if __name__ == '__main__':
    main()
