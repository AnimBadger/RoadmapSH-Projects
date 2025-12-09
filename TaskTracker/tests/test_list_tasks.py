from unittest.mock import patch, mock_open
import io
from task_tracker.list_tasks import list_tasks

def test_list_tasks_behavior_and_output():
    # Sample tasks to simulate what load_tasks() would return
    sample_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo",
            "createdAt": "2025-12-09T17:17:23",
            "updatedAt": "2025-12-09T17:17:23"
        },
        {
            "id": 2,
            "description": "Another task",
            "status": "in-progress",
            "createdAt": "2025-12-09T17:20:00",
            "updatedAt": "2025-12-09T17:20:00"
        }
    ]

    # Patch os.path.exists and load_tasks, capture stdout
    with patch("task_tracker.list_tasks.os.path.exists", return_value=True), \
         patch("task_tracker.list_tasks.load_tasks", return_value=sample_tasks), \
         patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:

        result = list_tasks()  # no arguments needed
        output = mock_stdout.getvalue()

    # 1️⃣ Behavior: returns the tasks
    assert result == sample_tasks

    # 2️⃣ Printed output: check key info is present
    assert "ID       : 1" in output
    assert "Description: Test task" in output
    assert "Status     : todo" in output
    assert "ID       : 2" in output
    assert "Description: Another task" in output
    assert "Status     : in-progress" in output

def test_list_tasks_file_missing_returns_empty():
    # File does not exist
    with patch("task_tracker.list_tasks.os.path.exists", return_value=False):
        result = list_tasks()

    assert result == []