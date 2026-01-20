def main():

    # greet user, and ask which option in the menu they would like to choose
    username = "lee wong".strip().capitalize() # must come back to this one
    print(f"Hello {username}! Hope you're doing well \n")
    menu = ["1", "2", "3", "4", "5", "6"]
    
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
                print("1") # we'll later add code that goes into selected menu option for case 1 - 6
            case "2":
                print("2")
            case "3":
                print("3")
            case "4":
                print("4")
            case "5":
                print("5")
            case "6":
                print("Session Terminated. Goodbye!")
                exit()

main()

"""
- Function to add task
- Function to view pending tasks
- Function to mark tasks done
- Function to view completed tasks
- Function to delete completed tasks
"""