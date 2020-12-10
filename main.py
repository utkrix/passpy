import getpass
master_pass = "Root"
def login():
    count = 0
    while count < 3:
        user_input = getpass.getpass("Enter the master password! ")
        if user_input == master_pass:
            print("Welcome to Ajoeks-Pass Pass")
            from menu import mainmenu
        else:
            print("Wrong password! Please enter again! ")
            count = count + 1
    else:
        print("You have exceeded the number of tries. Ajoeks-Pass Pass does not like scammers or hackers! ")
        exit
login()
        

