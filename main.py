def main():

    #greet user, and ask which option in the menu they would like to choose
    username = "name" #must come back to this one
    print(f"Hello {username}! Hope you're doing well \n")
    menu = [1, 2, 3, 4, 5]
    
    try:
        while True:
            #prompt on desired menu choice
            print("what would you like to do today? \n" \
            "1) Enter New Task \n" \
            "2) View Existing Tasks \n" \
            "3) Mark Tasks Done \n" \
            "4) View Completed Tasks \n" \
            "5) Delete completed files")
            break
    except ValueError:
        print("error")

main()

"""
- Function to add task
- Function to view pending tasks
- Function to mark tasks done
- Function to view completed tasks
- Function to delete completed tasks
"""