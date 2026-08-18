import json
from task import Task, UrgentTask

def load_profile():
    try:
        with open("profile.json", "r") as file:
            profile = json.load(file)
            return profile
    except FileNotFoundError:
        return None
def save_profile(profile):
    with open("profile.json", "w") as file:
        json.dump(profile, file, indent=4)
    print("Profile save successfully")



def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            dicts = json.load(file)
    except FileNotFoundError:
        return []
    tasks = []
    for d in dicts:
        if d.get("type") == "urgent":
            t = UrgentTask(d["task"], d["deadline"])
        else:
            t = Task(d["task"], d["done"])
        t.done = d["done"]
        tasks.append(t)
    return tasks

def save_tasks(tasks):
    # dicts = []
    # for t in tasks:
    #     dicts.append(t.to_dict())
    dicts = [t.to_dict() for t in tasks]
    with open("tasks.json", "w") as file:
        json.dump(dicts, file)