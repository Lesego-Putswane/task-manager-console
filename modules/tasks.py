def new_task():
        while True:
            new_task = input("Enter your new task: \n")
            if new_task != "":
                return new_task
            else:
                print(
                    "Task Cannot be empty! Try again")

def delete_tasks():
    pass

