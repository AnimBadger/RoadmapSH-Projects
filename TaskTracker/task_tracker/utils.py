import os
import json
from dotenv import load_dotenv

load_dotenv()

TASK_FILE = os.getenv('TASK_FILE', 'task.json')



def load_tasks() -> list:
    """
    Docstring for load_tasks
    
    :return: list of tasks
    :rtype: list
    """
    # If file doesn't exist, create it with an empty list
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file, indent=2)
        return []

    # If file exists, load the tasks
    with open(TASK_FILE, 'r') as file:
        return json.load(file)
    
def save_task(task: list[dict]) -> bool:
   """
   Docstring for save_task
   
   :param task: list of tasks
   :type task: list[dict]
   :return: if the save was a success or not
   :rtype: bool
   """
   try:
    with open(TASK_FILE, 'w') as file:
        json.dump(task, file, indent=2)
        return True
   except Exception as e:
      print(f'Failed to save task: {e}')
      return False