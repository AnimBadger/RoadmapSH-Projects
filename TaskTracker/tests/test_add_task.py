import os
import json
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