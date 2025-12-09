from unittest.mock import patch, mock_open
from task_tracker.delete_task import delete_task

@patch('task_tracker.utils.open', new_callable=mock_open,
       read_data='[{"id": 1, "description": "delete task"}]')
@patch('task_tracker.delete_task.os.path.exists', return_value=True)
@patch('task_tracker.delete_task.save_task')
def test_delete_task_success(mock_save, mock_exists, mock_file):
    """
    GIVEN a tasks.json file containing a task
    WHEN delete_task is called with a valid task_id
    THEN the task is removed, saved, and True is returned
    """
    result = delete_task(1)

    assert result is True
    mock_save.assert_called_once()

@patch('task_tracker.delete_task.load_tasks')
@patch('task_tracker.delete_task.save_task')
def test_delete_task_not_found(mock_save, mock_load_tasks):
    """
    GIVEN a tasks.json file that does NOT contain the requested task ID
    WHEN delete_task is called with a non-existing task_id
    THEN the function prints 'Task not found', returns False,
    AND save_task is NOT called
    """
    # Simulate tasks in file
    mock_load_tasks.return_value = [
        {"id": 2, "description": "another task"},
        {"id": 3, "description": "some task"}
    ]

    # Call delete_task with an ID that does not exist
    result = delete_task(1)

    # Assert the function returns False
    assert result is False

    # Assert save_task was not called because no deletion occurred
    mock_save.assert_not_called()
