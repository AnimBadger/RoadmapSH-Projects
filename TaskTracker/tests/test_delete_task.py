from unittest.mock import patch, mock_open
from task_tracker.delete_task import delete_task

@patch('task_tracker.utils.open', new_callable=mock_open,
       read_data='[{"id": 1, "description": "delete task"}]')
@patch('task_tracker.delete_task.os.path.exists', return_value=True)
@patch('task_tracker.delete_task.save_task')
def test_delete_task_success(mock_save, mock_exists, mock_file):
    result = delete_task(1)

    assert result is True
    mock_save.assert_called_once()
