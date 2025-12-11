import os
import json
from pathlib import Path
from dotenv import load_dotenv
import random

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
TASK_FILE = Path(os.getenv("TASK_FILE", BASE_DIR / "task.json"))

def get_task_id_limit() -> int:
    try:
        return int(os.getenv("TASK_ID_LIMIT", 9999))
    except ValueError:
        return 9999

TASK_ID_LIMIT = get_task_id_limit()


def load_tasks() -> list:
    """
    Load tasks from the JSON file.
    Creates an empty list if the file doesn't exist.
    """
    if not TASK_FILE.exists():
        TASK_FILE.parent.mkdir(parents=True, exist_ok=True)
        TASK_FILE.write_text("[]")  # safer than open+json.dump
        return []

    try:
        return json.loads(TASK_FILE.read_text())
    except json.JSONDecodeError:
        print("Warning: task file corrupted. Resetting to empty list.")
        return []


def save_task(tasks: list[dict]) -> bool:
    """
    Save the list of tasks to the JSON file safely.
    """
    if not isinstance(tasks, list):
        print("Error: tasks must be a list. Aborting save.")
        return False

    try:
        TASK_FILE.parent.mkdir(parents=True, exist_ok=True)
        TASK_FILE.write_text(json.dumps(tasks, indent=2))
        return True
    except Exception as e:
        print(f"Failed to save tasks: {e}")
        return False

def generate_task_id(tasks: list[dict]) -> int:
    existing_ids = {task["id"] for task in tasks}

    while True:
        task_id = random.randint(1, TASK_ID_LIMIT)
        if task_id not in existing_ids:
            return task_id