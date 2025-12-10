import os
from unittest.mock import patch
import json
from copy import deepcopy
from task_tracker.add_task import add_task
from task_tracker.utils import TASK_FILE

def setup_function():
    if os.path.exists(TASK_FILE):
        os.remove(TASK_FILE)


def test_add_task_creates_task():
    task = add_task('Learn unit testing')

    assert task.description == 'Learn unit testing'
    assert task.status == 'todo'

def test_add_task_saves_to_json():
    add_task('write tests')

    with open(TASK_FILE, 'r') as file:
        tasks = json.load(file)

    assert len(tasks) == 1
    assert tasks[0]['description'] == 'write tests'

def test_add_task_increases_length():
    # Original tasks
    existing_tasks = [
        {"id": 1, "description": "Existing task", "status": "todo", "createdAt": "2025-12-09T17:00:00", "updatedAt": "2025-12-09T17:00:00"}
    ]

    new_description = "New Task"

    # Make a copy so we don’t mutate original
    original_tasks = deepcopy(existing_tasks)

    with patch("task_tracker.add_task.load_tasks", return_value=existing_tasks), \
         patch("task_tracker.add_task.save_task") as mock_save:

        new_task = add_task(new_description)

    # The new task should have the correct description
    assert new_task.description == new_description

    # The length should now be original + 1
    assert len(existing_tasks) == len(original_tasks) + 1

    # The last task should be the new one
    assert existing_tasks[-1].get("description") == new_description

    # save_task should have been called once
    mock_save.assert_called_once()