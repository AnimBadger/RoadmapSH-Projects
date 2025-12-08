from datetime import datetime

class Task:
    def __init__(self, task_id: int, description: str, status = 'todo'):
        self.id = task_id
        self.description = description
        self.status = status
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """
        Convert Task object to a dictionary for JSON storage.
        """
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at
        }
    
    @staticmethod
    def from_dict(data):
        """
        Create a Task object from a dictionary (loaded from JSON).
        """
        task = Task(
            task_id=data["id"],
            description=data["description"],
            status=data["status"]
        )
        task.created_at = data["createdAt"]
        task.updated_at = data["updatedAt"]
        return task