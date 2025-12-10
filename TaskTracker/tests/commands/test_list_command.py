from commands.list_command import handle_list
from unittest.mock import patch

def test_list_command_calls_list_tasks():
    parts = ["list"]

    with patch("commands.list_command.list_tasks") as mock_list:
        handle_list(parts)
        mock_list.assert_called_once()

        