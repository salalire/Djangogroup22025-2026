class ToDoTask:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def mark_completed(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def to_dictionary(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

    @staticmethod
    def from_dictionary(data):
        return ToDoTask(
            task_id=data["id"],
            title=data["title"],
            completed=data["completed"]
        )
