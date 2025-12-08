from task_tracker.add_task import add_task
from task_tracker.task import Task
def show_help():
    """
    Docstring for show_help
    Show help to teach how to use progran
    """
#     print("""Task Tracker CLICommands:
#     add "task description"
#     update <id> "new description"
#     delete <id>
#     list
#     mark <id> <todo|in-progress|done>

#     Examples:
#     python start.py add "Buy groceries"
#     python start.py update 1 "Buy groceries and cook"
#     python start.py mark 1 done
#     python start.py list
# """)
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
    while True:
        user_input = input('\n> ').strip()

        if not user_input:
            continue

        parts = user_input.split()
        command = parts[0]
        
        try:
            if command.lower() == 'exit':
                print("Goodbye 👋")
                break

            elif command.lower() == 'add':
                description = parts[1]
                add_task(description)

        except (IndentationError, ValueError):
            print("Invalid command format. Type 'help for usage.'")
    
    

    
if __name__ == '__main__':
    main()
