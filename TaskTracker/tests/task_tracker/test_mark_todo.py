from unittest.mock import patch
from task_tracker.mark_task_todo import mark_task_todo

def test_mark_task_todo_success():
    """
    GIVEN a task with status 'in_progress'
    WHEN mark_task_todo is called
    THEN task status is updated to 'todo'
    AND save_task is called
    AND True is returned
    """

    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "in_progress"
        }
    ]

    with patch("task_tracker.mark_task_todo.load_tasks", return_value=fake_tasks) as mock_load, \
         patch("task_tracker.mark_task_todo.save_task", return_value=True) as mock_save:

        result = mark_task_todo(1)

        mock_load.assert_called_once()
        mock_save.assert_called_once_with(fake_tasks)
        assert result is True
        assert fake_tasks[0]["status"] == "todo"

def test_mark_task_todo_already_todo():
    """
    GIVEN a task already marked as todo
    WHEN mark_task_todo is called
    THEN it should return False
    AND save_task should not be called
    """

    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "todo"
        }
    ]

    with patch("task_tracker.mark_task_todo.load_tasks", return_value=fake_tasks), \
         patch("task_tracker.mark_task_todo.save_task") as mock_save:

        result = mark_task_todo(1)

        mock_save.assert_not_called()
        assert result is False

def test_mark_task_todo_from_done():
    fake_tasks = [
        {
            "id": 1,
            "description": "Test task",
            "status": "done"
        }
    ]

    with patch("task_tracker.mark_task_todo.load_tasks", return_value=fake_tasks), \
         patch("task_tracker.mark_task_todo.save_task") as mock_save:

        result = mark_task_todo(1)

        mock_save.assert_not_called()
        assert result is False

def test_mark_task_todo_task_not_found():
    with patch("task_tracker.mark_task_todo.load_tasks", return_value=[]), \
         patch("task_tracker.mark_task_todo.save_task") as mock_save:

        result = mark_task_todo(99)

        mock_save.assert_not_called()
        assert result is False
