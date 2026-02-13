import json
import os
from todotasck import ToDoTask


class TodoManager:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
        
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(item) for item in data]
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    
   

    def add_task(self, title):
        task_id = self.generate_id()
        new_task = ToDoTask(task_id, title)
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for task in self.tasks:
            status = "✅ Completed" if task.completed else "❌ Not Completed"
            print(f"[{task.id}] {task.title} - {status}")

    def update_task(self, task_id, new_title=None, completed=None):
        for task in self.tasks:
            if task.id == task_id:
                if new_title:
                    task.title = new_title
                if completed is not None:
                    task.completed = completed
                self.save_tasks()
                print("Task updated successfully!")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()
        print("Task deleted successfully!")

    def generate_id(self):
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1
