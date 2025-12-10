from commands import *
from commands.help_command import handle_help


def main():
    """
    Entry point of the application
    """ 
    running = True
    handle_help(['help'])
    COMMAND_HANDLERS = {
        "add": handle_add,
        "update": handle_update,
        "delete": handle_delete,
        "list": handle_list,
        "mark_in_progress": handle_mark_in_progress,
        "help": handle_help
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
