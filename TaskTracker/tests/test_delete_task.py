import json
from unittest.mock import patch
from task_tracker.delete_task import delete_task

def test_delete_task_success():
    """
    GIVEN a tasks.json file containing a task
    WHEN delete_task is called with a valid task_id
    THEN the task is removed, saved, and True is returned
    """
    fake_tasks = [{"id": 1, "description": "delete task"}]

    with patch("task_tracker.delete_task.load_tasks", return_value=fake_tasks), \
         patch("task_tracker.delete_task.save_task") as mock_save, \
         patch("task_tracker.delete_task.os.path.exists", return_value=True):

        result = delete_task(1)

    assert result is True
    mock_save.assert_called_once()

def test_delete_task_not_found():
    """
    GIVEN tasks.json exists but task ID does not exist
    WHEN delete_task is called
    THEN False is returned and save_task is NOT called
    """
    fake_tasks = [
        {"id": 2, "description": "another task"},
        {"id": 3, "description": "some task"},
    ]

    with patch("task_tracker.delete_task.load_tasks", return_value=fake_tasks), \
         patch("task_tracker.delete_task.save_task") as mock_save, \
         patch("task_tracker.delete_task.os.path.exists", return_value=True):

        result = delete_task(1)

    assert result is False
    mock_save.assert_not_called()