from unittest.mock import patch
from commands.add_command import handle_add


def test_handle_add_calls_add_task():
    parts = ["add", "Buy milk"]

    # patch the symbol USED in add_command
    with patch("commands.add_command.add_task") as mock_add_task:
        handle_add(parts)
        mock_add_task.assert_called_once_with("Buy milk")


def test_handle_add_no_description():
    parts = ["add"]

    with patch("commands.add_command.add_task") as mock_add_task:
        handle_add(parts)
        mock_add_task.assert_not_called()

