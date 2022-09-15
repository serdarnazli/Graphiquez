import database as db
import settings as stg
from text import Text
import time
import os
import sys
import graphiquez as grph


class Screens():
    def __init__(self,database):
        self.database = database
        self.settings = stg.Settings()
        self.settings.read_settings()
        self.text = Text()
        self.graph = grph.Graphiquez(self.database)
        if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
            self.clear = 'clear'
        elif sys.platform.startswith('win'):
            self.clear = 'cls'
        else:
            print("The birds say you are using an unsupported operating system. This program can only run on computers with Linux, MacOS and Windows installed. If you think there is something wrong, please contact with the manufacturer!")
            time.sleep(10)
            exit()


    def intro(self):
        print("#"*37)
        print("#      WELCOME TO GRAPHIQUEZ!       #")
        print("#"*37)
        if self.settings.evervisited() == False:
            print(self.text.get_kvkk())
            process = input()
            if process == "1":
                os.system(self.clear)
                print("Thank you!")
                self.settings.change_setting("evervisited","1")
            else:
                print("Thank you for your honesty. The application is closing... ")
                time.sleep(5)
                exit()
    

    def start_screen(self):
        while True:
            while True:
                print("For log-in please type 0, for sign-up please type 1. \n To exit you can type q.")
                process = input()
                if process == "0" or process == "1":
                    os.system(self.clear)
                    return process
                elif process =="q":
                    print("The application is closing...")
                    time.sleep(2)
                    exit()

                else:
                    print("You can only type 0 or 1 please try again!")
    def log_in_screen(self):
        while True:
            rememberMe,user_name = self.database.rememberMe(self.settings.remember_key())
            if rememberMe == "NoProblem":
                willRememberWork = input(f"We remembered you {user_name}! Would you like to use this account(hit just enter) or login with different account?(type 0)")
                if willRememberWork == "0":
                    self.settings.delete_generated_key()
                else:
                    return "NoProblem",user_name
            user_name = input(self.text.get_login("username"))
            password = input(self.text.get_login("password"))
            t_f , message = self.database.isPasswordCorrect(user_name,password)
            if message == "NoProblem":
                rememberMe = input(self.text.get_login("activateremember"))
                if not rememberMe or rememberMe[0] != "0":
                    rememberMe = "1"
                    self.settings.delete_generated_key()
                if rememberMe[0] == "0":
                    self.settings.write_generated_key(self.database,user_name)
                return message,user_name
            elif message == "noAccount":
                process = input(f"There is not any account with username: {user_name}. To try again please type something. To go back please type 1 ")
                if process == "1":
                    return "BackScreen",None
                    
                else:
                    continue
            elif message == "wrongPass":
                process = input(self.text.get_login("wrongpassword"))
                if process == "1":
                    return "BackScreen",None
                else:
                    continue

                
    def signed_processes(self,username):
        while True:
            os.system(self.clear)
            print(f"You are in! Welcome {username}!")
            self.mode = self.settings.get_setting("mode")
            print(f"You are in {self.mode} mode. If you want to change it go to section settings.")
            print(self.text.get_signed_main())
            process = input()
            if process.strip() == "q":
                return "Exit"
            elif process.strip() == "1":
                whatreturned = self.settingsScreen()
                
            elif process.strip() == "2":
                whatreturned = self.graphiquezDataScreen(username)
                
            elif process.strip() == "3":
                whatreturned = self.graphiquezMathScreen(username)
            elif process.strip() == "4":
                whatreturned = self.accountScreen(username)
            else:
                print("Unknown section number.")
                time.sleep(1)
                continue



    def settingsScreen(self):
        while True:
            settingsStr1 = str(self.settings)
            print(settingsStr1)
            print("Type 'default' to reset settings.")
            process = input("Please type the setting number that you want to change 'q' -> exit: ")
            if not process:
                continue
            if process == "q":
                return "Exit"
            elif process == "default":
                self.settings.set_default_settings()
                print("All settings are set to default.")
                time.sleep(1.5)
                continue
            else:
                try:
                    int(process)
                    pass
                except:
                    continue
            if int(process) not in range(14):
                print("Unknown setting number. Please try again.")
                continue
            else:
                settingsStr = settingsStr1.split("\n")
                settingList = []
                for i in range(len(settingsStr)):
                    row = settingsStr[i].split("->")
                    index = row[0].index("-")
                    row[0] = row[0][index+1:].strip()
                    row[1] = row[1].strip()
                    settingList.append(row)
                if settingList[int(process)][0] == "mode":
                    print("0->pro mode \n1->amateur mode")
                    tochange = input("Number: ")
                    if tochange == "0":
                        self.settings.change_setting("mode","pro")
                        continue
                    elif tochange == "1":
                        self.settings.change_setting("mode","amateur")
                        continue
                    else:
                        continue
                tochange = input(f"Please type the value for new '{settingList[int(process)][0]}' setting \n")
                print(f"Setting is changing. '{settingList[int(process)][0]}' setting value from '{settingList[int(process)][1]} to '{tochange}'")
                self.settings.change_setting(settingList[int(process)][0],tochange)
                print("Change is succesful.")
                time.sleep(1.5)
                continue


    def graphiquezDataScreen(self,username):
        if self.mode == "pro":
            self.graph.pro_main()
        elif self.mode == "amateur":
            self.graph.amateur_main()
        else:
            print("There is something wrong with your settings. Please check the settings section!")
    def graphiquezMathScreen(self,username):
        self.graph.mathFunctions_main()

    def accountScreen(self,username):
        os.system(self.clear)
        draft_number = self.database.draft_number(username)
        print(f"Hello {username}\nYou have {draft_number} draft rights.")
        while True:
            process = input("If you want to:\n'q'->exit\n'0'->Change password")
            if process == "q":
                return "Exit"
            elif process =="0":
                newpass = input("Please type your new password:\n")
                self.database.password_changer(username,newpass)
                continue

            else:
                continue