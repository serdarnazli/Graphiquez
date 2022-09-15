import os 
import sys



class Text():
    def __init__(self):
        self.path = os.path.abspath(sys.argv[0]+"/.."+"/..") + "/text/"
        self.login = self.__text_login()
        self.kvkk = self.__text_kvkk()
        self.signed_main = self.__text_signed_main()
    def __text_login(self):
        with open(self.path+"login.txt","r") as file:
            lines = file.readlines()
            myDict = dict()
            for line in lines:
                line = line.strip()
                line = line.split("'")
                myDict[line[0]] = line[1]

            return myDict

    def get_login(self,element):
        return self.login[element]

    def __text_kvkk(self):
        with open(self.path+"kvkk.txt","r") as file:
            theText = ""
            lines = file.readlines()
            for line in lines:
                theText += line
            return theText

    def get_kvkk(self):
        return self.kvkk

    def __text_signed_main(self):
        with open(self.path+"signed_main.txt") as file:
            text = file.read()
            return text
    
    def get_signed_main(self):
        return self.signed_main

if __name__ == "__main__":
    text = Text()
