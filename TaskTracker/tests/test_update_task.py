import json 
from unittest.mock import patch, mock_open
from task_tracker.update_task import update_task


@patch('task_tracker.update_task.os.path.exists', return_value=True)
@patch('task_tracker.update_task.open', new_callable=mock_open)
def test_update_task_success(mock_file, _mock_exists):
    '''
    GIVEN tasks.json exists and task ID is present
    WHEN update_task is called
    THEN description and updatedAt are updated
    AND updated task returned
    '''

    fake_tasks = [
        {
            'id': 1,
            'description': 'old task',
            'createdAt': '2024-01-01T10:00:00',
            'updatedAt': None
        }
    ]

    mock_file().read.return_value = json.dumps(fake_tasks)

    result = update_task(1, 'Updated Task')

    assert result is not None
    assert result['description'] == 'Updated Task'
    assert result['updatedAt'] is not None