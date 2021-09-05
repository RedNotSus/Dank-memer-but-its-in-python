import time
from replit import db

red = "\033[0;31m"
green = "\033[0;32m"
white = "\033[0;37m"


def login(): # making the login system
     # the  thing
    print("Do you want to log-in, sign-up or play as guest(Money won't be saved if you play as a Guest):")
    account_choice = input("[1] Login\n[2] Sign Up\n[3] Guest\n>>> ")

    if account_choice == "1":
        
        print("Login\n")
        user = input("Username: ")
        passcode = input("Password: ")
        try:
            Password = db[user]

            if Password == passcode:
                
                print(green+"Logged in!"+white)
                time.sleep(2) # waiting 2 seconds
                

            else:
                
                print(red+"Incorrect!"+white)
                time.sleep(2)
                login()

        except:
            
            print(red+"That username is not included!"+white)
            time.sleep(2)
            login()

    elif account_choice == "2":
        
        print("Sign up\n")
        newuser = input("Username: ")
        newpasscode = input("Password: ")

        try:
            db[newuser] = newpasscode
            
            print(green+"Account made!"+white)
            time.sleep(2)
            
            login()
        
        except:
            
            print(red+"Account already made!"+white)
            time.sleep(2)
            
            login()

    elif account_choice == "3":
        
        print(red+"Playing as a Guest"+white)
        time.sleep(2)
        

    else:
        
        print(red+"Invalid Command!"+white)
        time.sleep(2)
        
        login()