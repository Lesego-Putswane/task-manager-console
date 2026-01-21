from tasks import *

def main():

    # greet user, and ask which option in the menu they would like to choose
    username = "lee wong".strip().capitalize() # must come back to this one
    print(f"Hello {username}! Hope you're doing well \n")
    tasks = []
    
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
                new_task()
                #tasks.append(new_task)
            case "2":
                view_task()
            case "3":
                mark_done()
            case "4":
                view_completed_tasks()
            case "5":
                delete_tasks()
            case "6":
                print("Session Terminated. Goodbye!")
                exit()

main()

