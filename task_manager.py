
import json
import os
from settings import TASK_FILE

class TaskManager:
    def __init__(self):
        self.filename = TASK_FILE
        self.check_file()

    def check_file(self):
        # لو الملف مش موجود، بنعمل ملف JSON فيه ليستة فاضية []
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def load_tasks(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_tasks(self, tasks):
        
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)