from unittest.mock import patch
from commands.mark_todo_command import handle_mark_todo


def test_handle_mark_todo_success():
    parts = ["mark_todo", "1"]

    with patch("commands.mark_todo_command.mark_task_todo") as mock_mark:
        result = handle_mark_todo(parts)

        mock_mark.assert_called_once_with(1)
        assert result is True


def test_handle_mark_todo_missing_id():
    parts = ["mark_todo"]

    with patch("commands.mark_todo_command.mark_task_todo") as mock_mark:
        result = handle_mark_todo(parts)

        mock_mark.assert_not_called()
        assert result is False


def test_handle_mark_todo_invalid_id():
    parts = ["mark_todo", "abc"]

    with patch("commands.mark_todo_command.mark_task_todo") as mock_mark:
        result = handle_mark_todo(parts)

        mock_mark.assert_not_called()
        assert result is False
