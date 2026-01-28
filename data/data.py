import json
import os

DATA_FILE = "data/tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)