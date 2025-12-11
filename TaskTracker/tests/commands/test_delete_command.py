from unittest.mock import patch
from commands.delete_command import handle_delete

def test_handle_delete_success():
    parts = ["delete", "1"]

    with patch("commands.delete_command.delete_task") as mock_delete:
        result = handle_delete(parts)

        mock_delete.assert_called_once_with(1)
        assert result is True

def test_handle_delete_missing_id():
    parts = ["delete"]

    with patch("commands.delete_command.delete_task") as mock_delete:
        result = handle_delete(parts)

        mock_delete.assert_not_called()
        assert result is False


def test_handle_delete_invalid_id():
    parts = ["delete", "abc"]

    with patch("commands.delete_command.delete_task") as mock_delete:
        result = handle_delete(parts)

        mock_delete.assert_not_called()
        assert result is False
