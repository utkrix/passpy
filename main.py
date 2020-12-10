import getpass
master_pass = "Root"
def login():
    count = 0
    while count < 3:
        user_input = getpass.getpass("Enter the master password! ")
        if user_input == master_pass:
            user_input = int(input('''Welcome to PassPy\nEnter:\n1--> To create a new password! 
            \n2--> To view all passwords!\n---> '''))
            if user_input == 1:
                from newpass import mainmenu
        else:
            print("Wrong password! Please enter again! ")
            count = count + 1
    else:
        print("You have exceeded the number of tries. PassPy does not like scammers or hackers! ")
        exit
    
        
login()
        

