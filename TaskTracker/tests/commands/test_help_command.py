from unittest.mock import patch
from commands.help_command import HELP_MESSAGE, handle_help

def test_handle_help_print_help_message():
    parts = ['help']

    with patch('builtins.print') as mock_prints:
        handle_help(parts)

        # Ensure print was called at least once
        mock_prints.assert_called()

        # Ensure the first call printed the expected message
        printed_text = mock_prints.call_args[0][0]
        assert "Task Tracker CLI" in printed_text
        assert "Available Commands" in printed_text


def test_handle_help_with_extra_args():
    # Passing extra arguments should print usage
    parts = ["help", "extra"]

    with patch("builtins.print") as mock_print:
        handle_help(parts)
        mock_print.assert_called_once_with("Usage: help")