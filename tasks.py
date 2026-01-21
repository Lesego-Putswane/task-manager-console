def new_task():
        while True:
            new_task = input("Enter your new task: \n")
            if new_task != "":
                return new_task
            else:
                print(
                    "Task Cannot be empty! Try again")

def view_task():
    pass

def mark_done():
    pass

def view_completed_tasks():
    pass

def delete_tasks():
    pass

new_task()