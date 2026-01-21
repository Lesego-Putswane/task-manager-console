from tasks import *

def main():
    # greet user, and ask which option in the menu they would like to choose
    username = "lee wong".strip().capitalize() # must come back to this one
    print(f"Hello {username}! Hope you're doing well \n")
    open_tasks = []
    done_tasks = []
    
    while True:
        # prompt on desired menu choice
        print("what would you like to do today? \n" \
        "1) Enter New Task \n" \
        "2) View Existing Tasks \n" \
        "3) Mark Tasks Done \n" \
        "4) View Completed Tasks \n" \
        "5) Delete completed files \n" \
        "6) Exit")
        
        # get users choice and check which condition it fits
        user_choice = input("Enter your Menu Choice: \n")
        match user_choice:
            case "1":
                added_task = new_task()
                print(f"{added_task}, has been added as a task \n")
                open_tasks.append(added_task)
            case "2":
                if open_tasks == []:
                    print("You have no open open_tasks \n")
                else:
                    for task in open_tasks:
                        print(task)
            case "3":
                task_choice = input("Which task would you like to mark done: \n")
                if task_choice.lower() in open_tasks:
                    open_tasks.remove(task_choice) 
                    done_tasks.append(task_choice)
                    print(f"{task_choice} has been removed. \nThese are your new tasks \n {open_tasks}")
                else:
                    print("Task does not exist")
            case "4":
                print("These are your done tasks:\n")
                for done_task in done_tasks:
                        print(done_task)
            case "5":
                delete_tasks()
                delete = input("Would you like to delete done tasks? \n")
                if delete == "yes" or delete == "y":
                    done_tasks.clear()
                elif delete == "no" or delete == "n":
                    print("Done tasks not deleted")
                else:
                    print("invalid input!")
            case "6":
                print("Session Terminated. Goodbye!")
                exit()
                
main()