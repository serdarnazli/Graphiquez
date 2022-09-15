password = "9f4fa4e56a989e9c32fa7a"
a = f"mongodb+srv://graphiquez:{password}@graphiquez.1jh7a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

import pymongo
import socket
import time
import hashlib
import os
import sys
import random

class localLogFile:
    def __init__(self,path=os.path.abspath(sys.argv[0]+"/.."+"/.."),name="log.txt"):
        self.path = path + "/logs" + f"/{name}"
        self.name = name

    def writeLog(self,toWrite):
        with open(self.path,"a+") as file:
            toWrite  = toWrite + "\t\t\t" + str(time.gmtime(time.time()))  + "\n"
            file.write(toWrite)



class DatabaseLog():    #This class is for logs. 

    def __init__(self,password="9f4fa4e56a989e9c32fa7a"):
        self.password = password
        self.address = f"mongodb+srv://graphiquez:{self.password}@graphiquez.1jh7a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.collection = None
        self.localLog = localLogFile()


    def connect(self):
        try:
            cluster = pymongo.MongoClient(self.address)
            db = cluster["Graphiquez"]
            self.collection = db["logs"]

            print("SUCCESFULLY CONNECTED TO THE -log- DATABASE!")
            self.logWrite("connectionTryLog")
        except:
            raise Exception("ConnectionError occured. Check your Ethernet connection! Trying again in 10 seconds...")
    
    def logWrite(self,process):
        try:
            sampleOnline={"ComputerName": socket.gethostname(),
                "IpAd":socket.gethostbyname(socket.gethostname()),
                "Time":time.gmtime(time.time()),
                "process":process} 
            self.collection.insert_one(sampleOnline)
            sampleLocal = sampleOnline["process"] 
            self.localLog.writeLog(sampleLocal)
        except:
            raise Exception("An error Occur. DatabaseLog/Write blocks.")
                


class Database():
    def __init__(self, password="9f4fa4e56a989e9c32fa7a" ):
        self.__password = password
        self.__address = f"mongodb+srv://graphiquez:{self.__password}@graphiquez.1jh7a.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.collection = None
        self.DBLog = DatabaseLog()
        try:
            self.DBLog.connect()
        except: 
            raise Exception("Could not connect to database. Trying again in 5 seconds.")
        self.localLog = localLogFile()

    def connect(self):
        try:
            cluster = pymongo.MongoClient(self.__address)
            db = cluster["Graphiquez"]
            self.collection = db["accounts"]
            print("SUCCESFULLY CONNECTED TO THE -acc- DATABASE!")
            self.DBLog.logWrite("connectionTryAcc")
        except:
            raise Exception("ConnectionError occured. Check your Ethernet connection! Trying again in 10 seconds...")

    def turnToHash(self,password):
        encrpyt = hashlib.sha256()
        encrpyt.update(str(password).encode("utf-8"))
        hash = encrpyt.hexdigest()
        return hash


        


    def writeNewAcc(self,accId,passw,draft=10):
        self.DBLog.logWrite(f"newAccount-{accId}")
        passw = self.turnToHash(passw)
        sample ={"accId":accId,"password":passw,"draft":draft,"random_key":0}
        self.collection.insert_one(sample)

    def newAcc(self):
        
        allowedTo = ["?","!","+","-","/","(",")","_","-"]
        flag = False
        print(f"\n\nPlase type only alphabet characters and digits. These characters are also allowed: {allowedTo}.")
        while True:
            print("If you want to exit this screen please just type 'q'")
            requirements = True
            userName = input("Please type your userName: ")
            if userName == "q":
                return False,"Exit"
            password = input("Please type your password: ")

            if len(userName) > 20 or len(password) > 20:
                print("Username and password can not be longer than 20! \n \n")
                continue
            elif len(userName) < 2:
                print("Username can not be shorter than 2. \n \n")
                continue
            elif len(password) < 3:
                print("Password can not be shorter than 3. \n \n")  
                continue

            thereExist,problem = self.isPasswordCorrect(userName,"-")
            if problem != "noAccount":
                print("\nThere is a user that has this name! Please choose another username. \n")
                continue

            for i in userName:
                if (i.isalpha() or i.isdigit()  or (i in allowedTo)):
                    continue
                else:
                    print(f"\nYour username does not meet the requirements.")
                    requirements = False
                    break
            for i in password:
                if (i.isalpha() or i.isdigit()  or (i in allowedTo)):
                    continue
                else:
                    requirements = False
                    print(f"Your password does not meet the requirements.\n\n")
                    break
            
            if requirements == True:
                self.writeNewAcc(userName,password)
                self.localLog.writeLog("NewAccCreated")
                print("\nYou are succesfully registered.")
                print("You are redirected to the login screen.\n \n")
                return True,"1"

            else:
                continue
               
            
                    
    def isPasswordCorrect(self,username,password):
        password = self.turnToHash(password)
        thereExist = False
        isPasswordCorrect = False
        allData = self.collection.find()
        for datum in allData:
            if username == datum["accId"]:
                thereExist = True
                if password == datum["password"]:
                    isPasswordCorrect = True
            else:
                continue
        
        if thereExist == True and isPasswordCorrect == False:
            return False,"wrongPass"
        if thereExist == False:
            return False,"noAccount"
        if thereExist == True and isPasswordCorrect == True:
            return True,"NoProblem"
        
    def generateRandom(self,username):
        computer_name = socket.gethostname()
        ip_address = socket.gethostbyname(socket.gethostname())
        toWrite1 = str(computer_name)+str(ip_address)
        toWrite1 = self.turnToHash(toWrite1)
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        toWrite2 = ""
        for i in range(7):
            toWrite2 += random.choice(alphabet)
        for i in range(7):
            toWrite2 += str(random.choice(list(range(10))))
        for i in range(7):
            toWrite2 += random.choice(alphabet)
        for i in range(7):
            toWrite2 += str(random.choice(list(range(10))))
        toWrite2 = self.turnToHash(toWrite2)
        totalToWrite = toWrite1+"-"+toWrite2
        search = {"accId":username}
        update = {"$set":{"random_key":totalToWrite}}
        self.collection.update_one(search,update)
        return totalToWrite

        

    def rememberMe(self,generated_random):
        if generated_random == "0":
            return None,None
        allData = self.collection.find()
        for datum in allData:
            if str(generated_random) == str(datum["random_key"]):
                return "NoProblem",datum["accId"]
        return None,None

    def draft_diminuer(self,username):
        allData = self.collection.find()
        for datum in allData:
            if datum["accId"] == username:
                drafts = datum["draft"] - 1
        search = {"accId":username}
        update = {"$set":{"draft":drafts}}
        self.collection.update_one(search,update)
    
    def draft_number(self,username):
        allData = self.collection.find()
        for datum in allData:
            if datum["accId"] == username:
                drafts = datum["draft"]
        return drafts
    
    def password_changer(self,username,newpassword):
        allData = self.collection.find()
        newpassword = self.turnToHash(newpassword)
        search = {"accId":username}
        update = {"$set":{"password":newpassword}}
        self.collection.update_one(search,update)
        update2 = update = {"$set":{"random_key":"0"}}
        self.collection.update_one(search,update2)
        print("Password change is succesful.")
        


                

if __name__ == "__main__":      
    database = Database()
    database.connect()
    #database.newAcc()
    #database.generateRandom("ITUADMIN")        
    #print(database.isPasswordCorrect("esradasdan","esradsadan5858"))
                
                
            
            
