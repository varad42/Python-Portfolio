# Lesson 30 — The Debugger 🔬

def longest(*words):
    best = ""
    for w in words:
        if len(w) > len(best):    # 🔴 breakpoint went HERE
            best = w
    return best

print(longest("i", "will", "win", "the", "game"))

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
        tasks.append(t)         # 🔴 breakpoint goes HERE — expand t's ▶ arrow each freeze
    return tasks