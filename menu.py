import getpass
def mainmenu():
    user_input = int(input("Welcome to Ajoeks-Pass\nEnter:\n1--> To create a new password! \n2--> To view all passwords!"))
    if user_input == 1:
        print("You have chosen to create a new password!")
        name_of_site = input("Enter the name of the website! ")
        email = input("Enter the email associcated with the account! ")
        passwd = getpass.getpass("Enter the password! ") 
        conf_passwd = getpass.getpass("Enter your password again! ")
        while passwd != conf_passwd:
            print("The password you entered is incorret!\nPlease enter it again!")
            passwd = getpass.getpass("Enter the password! ") 
            conf_passwd = getpass.getpass("Enter your password again! ")
        print("Your infos are; Site name: ",name_of_site," Email associated: ",email)
        conf = input("If all the credentials match press Y; If not press N!")
        confirmation = conf.upper()
        if confirmation == "Y":
            print("Your information has now been saved to database!")
        while confirmation == "N":
            name_of_site = input("Enter the name of the website! ")
            email = input("Enter the email associcated with the account! ")
            passwd = getpass.getpass("Enter the password! ") 
            conf_passwd = getpass.getpass("Enter your password again! ")
            while passwd != conf_passwd:
                print("The password you entered is incorret!\nPlease enter it again!")
                passwd = getpass.getpass("Enter the password! ") 
                conf_passwd = getpass.getpass("Enter your password again! ")
            print("Your infos are; Site name: ",name_of_site," Email associated: ",email)
            conf = input("If all the credentials match press Y; If not press N!")
            confirmation = conf.upper()
            if confirmation == "Y":
                print("Your information has now been saved to database!")
                exit()
mainmenu()