
"""import database as db
import settings as stg
from text import Text
import time
import os
import sys
settings = stg.Settings()
settings.read_settings()
text = Text()
if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
    clear = 'clear'
elif sys.platform.startswith('win'):
    clear = 'cls'
else:
    print("The birds say you are using an unsupported operating system. This program can only run on computers with linux, macOS and windows installed. If you think there is something wrong, please contact the manufacturer!")
    time.sleep(10)
    exit()


def intro():
    print("#"*37)
    print("#      WELCOME TO GRAPHIQUEZ!       #")
    print("#"*37)
    if settings.evervisited() == False:
        print(text.get_kvkk())
        process = input()
        if process == "1":
            os.system(clear)
            print("Thank you!")
            settings.change_setting("evervisited","1")
        else:
            print("Thank you for your honesty. The application is closing... ")
            time.sleep(5)
            exit()
intro()

while True:
    
    flag = 0
    
    try:
        database = db.Database()
        database.connect()
        flag = 1 
    except Exception as f:
        flag = 0
        print(f)
    if flag == 1:
        break
    time.sleep(5)

def start_screen():
    while True:
        while True:
            print("For log-in please type 0, for sign-up please type 1. \n To exit you can type q.")
            process = input()
            if process == "0" or process == "1":
                os.system(clear)
                return process
            elif process =="q":
                print("The application is closing...")
                time.sleep(2)
                exit()

            else:
                print("You can only type 0 or 1 please try again!")
def log_in_screen():
    while True:
        rememberMe,user_name = database.rememberMe(settings.remember_key())
        if rememberMe == "NoProblem":
            willRememberWork = input(f"We remembered you {user_name}! Would you like to use this account(hit just enter) or login with different account?(type 0)")
            if willRememberWork == "0":
                settings.delete_generated_key()
            else:
                return "NoProblem",user_name
        user_name = input(text.get_login("username"))
        password = input(text.get_login("password"))
        t_f , message = database.isPasswordCorrect(user_name,password)
        if message == "NoProblem":
            rememberMe = input(text.get_login("activateremember"))
            if not rememberMe or rememberMe[0] != "0":
                rememberMe = "1"
                settings.delete_generated_key()
            if rememberMe[0] == "0":
                settings.write_generated_key(database,user_name)
            return message,user_name
        elif message == "noAccount":
            process = input(f"There is not any account with username: {user_name}. To try again please type something. To go back please type 1 ")
            if process == "1":
                return "BackScreen",None
                
            else:
                continue
        elif message == "wrongPass":
            process = input(text.get_login("wrongpassword"))
            if process == "1":
                return "BackScreen",None
            else:
                continue

            
def signed_processes(username):
    os.system(clear)
    print(f"You are in! Welcome {username}!")
    mode = settings.get_setting("mode")
    print(f"You are in {mode} mode. If you want to change it go to section settings.")
    print(text.get_signed_main())
    
"""


import screens as sc
import time
import database as db


def databaseConnectScreen():
    while True:
            
        flag = 0
            
        try:
            database = db.Database()
            database.connect()
            flag = 1 
            return database
        except Exception as f:
            flag = 0
            print(f)
        if flag == 1:
            break
        time.sleep(5)
    


database = databaseConnectScreen()
screens = sc.Screens(database)

screens.intro()
while True:                    #main thing goes on here.
    is_log_succesful = False
    process = screens.start_screen()
    if process == "1":
        database.newAcc()
        continue
    else:
        message,username = screens.log_in_screen()
        if message == "BackScreen":
            continue
        if message == "NoProblem":
            is_log_succesful = True
    
    if is_log_succesful == True:
        screens.signed_processes(username)
        






        
    

            
            

