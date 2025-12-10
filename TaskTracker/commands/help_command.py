HELP_MESSAGE = """
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

mark_<todo|in_progress|done> <id>
    Mark a task's status
    Example: mark_in_progress 1

help
    Show this help menu

exit
    Exit the application
"""


def handle_help(parts: list):
    """
    Handler for the 'help' command.
    Shows the HELP_MESSAGE. No extra arguments are allowed.
    """
    if len(parts) > 1:
        print("Usage: help")
        return

    print(HELP_MESSAGE)
