from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
  
def login():
    createaccount = input("Y to create account\n")
    if createaccount == 'y':
        username = input("Choose your username \n")
        password = input("Choose your password \n")
    elif createaccount == 'n':
        username = 'Admin'
        password = 'Admin1'

    login_user = input("Enter your username \nLogin: ")
    login_password = input("Enter your password \nPassword: ")

    if login_user == username and login_password == password:
        clear()
        print("Login successful")
    else:
        clear()
        print("\nDenied access!")

username = ''
password = ''
login()