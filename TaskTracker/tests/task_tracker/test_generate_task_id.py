from task_tracker.add_task import generate_task_id
from task_tracker.utils import TASK_ID_LIMIT

def test_task_id_returns_id_int():
    tasks = []

    task_id = generate_task_id(tasks)
    
    assert isinstance(task_id, int)
    assert 1 <= task_id <= TASK_ID_LIMIT