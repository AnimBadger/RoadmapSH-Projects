from unittest.mock import patch
from task_tracker.mark_task_done import mark_task_done


def test_mark_task_done_success():
    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "in_progress"
        }
    ]

    with patch("task_tracker.mark_task_done.load_tasks", return_value=fake_tasks) as mock_load, \
         patch("task_tracker.mark_task_done.save_task", return_value=True) as mock_save:

        result = mark_task_done(1)

        mock_load.assert_called_once()
        mock_save.assert_called_once()
        assert result is True
        assert fake_tasks[0].get("staus") == "done"


def test_mark_task_done_already_done():
    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "done"
        }
    ]

    with patch("task_tracker.mark_task_done.load_tasks", return_value=fake_tasks), \
         patch("task_tracker.mark_task_done.save_task") as mock_save:

        result = mark_task_done(1)

        mock_save.assert_not_called()
        assert result is False


def test_mark_task_done_from_todo():
    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo"
        }
    ]

    with patch("task_tracker.mark_task_done.load_tasks", return_value=fake_tasks), \
         patch("task_tracker.mark_task_done.save_task") as mock_save:

        result = mark_task_done(1)

        mock_save.assert_not_called()
        assert result is False


def test_mark_task_done_task_not_found():
    with patch("task_tracker.mark_task_done.load_tasks", return_value=[]), \
         patch("task_tracker.mark_task_done.save_task") as mock_save:

        result = mark_task_done(99)

        mock_save.assert_not_called()
        assert result is False
