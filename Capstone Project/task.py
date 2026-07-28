
from datetime import date
class Task:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done



    def complete(self):
        self.done = True

    def display(self):
        if self.done:
            return "[X] " + self.name
        return "[ ] " + self.name

    def rename(self, new_name):
        self.name = new_name

    def dict(self, name):
        self.name = name
        tasks = {
            "task": name,
            "done": False
        }
        return tasks

    def to_dict(self):
        return {"task": self.name, "done": self.done}

class UrgentTask(Task):
    def __init__(self, name, deadline):
        super().__init__(name)
        self.deadline = date.fromisoformat(deadline)  # gate translates, ALWAYS

    def display(self):
        today = date.today()
        if self.deadline < today:
            return "🔥 " + self.name + " ⚠️ OVERDUE"
        else:
            return "🔥 " + self.name + " (" + str((self.deadline - today).days) + " days left)"

    def to_dict(self):
        d = super().to_dict()
        d["deadline"] = str(self.deadline)
        d["type"] = "urgent"
        return d

class LazyTask(Task):
    pass

