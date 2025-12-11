from unittest.mock import patch
from task_tracker.mark_task_in_progress import mark_task_in_progress


def test_mark_task_in_progress_success():
    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo"
        }
    ]

    with patch("task_tracker.mark_task_in_progress.load_tasks", return_value=fake_tasks) as mock_load, \
         patch("task_tracker.mark_task_in_progress.save_task", return_value=True) as mock_save:

        result = mark_task_in_progress(1)

        mock_load.assert_called_once()
        mock_save.assert_called_once_with(fake_tasks)
        assert result is True
        assert fake_tasks[0]["status"] == "in-progress"


def test_mark_task_in_progress_already_in_progress():
    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "in-progress"
        }
    ]

    with patch("task_tracker.mark_task_in_progress.load_tasks", return_value=fake_tasks), \
         patch("task_tracker.mark_task_in_progress.save_task") as mock_save:

        result = mark_task_in_progress(1)

        mock_save.assert_not_called()
        assert result is False


def test_mark_task_in_progress_task_not_found():
    with patch("task_tracker.mark_task_in_progress.load_tasks", return_value=[]), \
         patch("task_tracker.mark_task_in_progress.save_task") as mock_save:

        result = mark_task_in_progress(99)

        mock_save.assert_not_called()
        assert result is False
