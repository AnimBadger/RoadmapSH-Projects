import json 
from unittest.mock import patch
from task_tracker.update_task import update_task

def test_update_task_success():
    """
    GIVEN tasks.json exists and task ID is present
    WHEN update_task is called
    THEN description and updatedAt are updated
    AND updated task returned
    """
    # Fake task data
    fake_tasks = [
        {
            "id": 1,
            "description": "old task",
            "status": "todo",
            "createdAt": "2024-01-01T10:00:00",
            "updatedAt": None
        }
    ]

    with patch("task_tracker.update_task.load_tasks", return_value=fake_tasks) as mock_load, \
         patch("task_tracker.update_task.save_task", return_value=True) as mock_save:

        # Call the function we are testing
        updated_task = update_task(1, "Updated Task")

        mock_load.assert_called_once()


    # Check that the task was updated
    assert updated_task is not None
    assert updated_task["description"] == "Updated Task"
    assert updated_task["updatedAt"] is not None

   
