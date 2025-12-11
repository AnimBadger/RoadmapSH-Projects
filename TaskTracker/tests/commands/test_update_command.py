from unittest.mock import patch
from commands.update_command import handle_update


def test_handle_update_success():
    parts = ["update", "1 New task description"]

    with patch("commands.update_command.update_task") as mock_update:
        result = handle_update(parts)

        mock_update.assert_called_once_with(1, "New task description")
        assert result is True


def test_handle_update_missing_arguments():
    parts = ["update"]

    with patch("commands.update_command.update_task") as mock_update:
        result = handle_update(parts)

        mock_update.assert_not_called()
        assert result is False


def test_handle_update_invalid_task_id():
    parts = ["update", "abc New description"]

    with patch("commands.update_command.update_task") as mock_update:
        result = handle_update(parts)

        mock_update.assert_not_called()
        assert result is False
