import json 
from unittest.mock import patch, mock_open
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

    # Patch os.path.exists to simulate file exists
    # Patch open to simulate reading/writing the tasks.json file
    m_open = mock_open(read_data=json.dumps(fake_tasks))
    with patch("task_tracker.update_task.os.path.exists", return_value=True), \
         patch("task_tracker.update_task.open", m_open):

        # Call the function we are testing
        updated_task = update_task(1, "Updated Task")

    # Check that the task was updated
    assert updated_task is not None
    assert updated_task["description"] == "Updated Task"
    assert updated_task["updatedAt"] is not None

    # Ensure the file was opened for writing (saving updates)
    m_open.assert_called_with("tasks.json", "w")
