from matplotlib import projections
import settings as stg
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import time
import os
import sys
import csv
import pandas as pd
import pickle
from bs4 import BeautifulSoup
import requests
class FileHandler():
    def __init__(self):
        self.settings = stg.Settings()
        self.settings.read_settings()
        self.read_location = self.settings.get_setting("read_location")

    def get_all_files(self):
        all_files = []
        dir_list = os.listdir(self.read_location)
        for path in dir_list:
            if os.path.isfile(os.path.join(self.read_location,path)):
                if path.endswith(".csv") or path.endswith(".xlsx") or path.endswith(".xls"):
                    all_files.append(path)
        return all_files

    def print_all_files(self):
        all_files = self.get_all_files()
        str = ""
        i = 0
        while i<len(all_files)-1:
            toadd1 = all_files[i]
            toadd2 = all_files[i+1]
            tempo = f"{toadd1:^30} {toadd2:^30} \n"
            str += tempo
            i = i + 2
        print(str)

    def read_csv(self,filename,row=None,column=None):
        try:
            csv_data = pd.read_csv(self.read_location + f"/{filename}")
        except:
            raise ValueError("File could not be found")
        
        if row == None and column != None:
            column = int(column)
            try:
                wanteddata = csv_data.iloc[:,column]
                wanteddata = wanteddata.dropna()
                return wanteddata
            except:
                raise ValueError("Wanted column number can not be greater than no.of col. in data")
        elif row != None and column == None:
            row = int(row)
            try:
                wanteddata = csv_data.loc[2]
                wanteddata = wanteddata.dropna()
                return wanteddata
            except:
                raise ValueError("Row can not be greater than no.of rows in data")
        else:
            raise ValueError("without row or column and with both row and column, read_csv function can not be called.")

        """ data = []
        try:
            with open(self.read_location + f"/{filename}",errors="replace") as file:
                csvreader = csv.reader(file)
                header = next(csvreader)
                for aRow in csvreader:
                    flag = 0 
                    for char in aRow:
                        if char in ("NA","N/A","na","non"):
                            flag = 1 
                    if flag == 0:
                        data.append(aRow)
        except:
            raise ValueError("File could not be found.")
        
        if row == None and column != None:
            column = int(column)
            if column >= len(data[0]):
                raise ValueError("Wanted column number can not be greater than the number of columns in the file.")
            
            for j in range(len(data)):
                if j == column:
                    wanted_column = []
                    for i in range(len(data)):
                        wanted_column.append(data[i][j])
                    print("coming from read_csv::",wanted_column)
                    return wanted_column

        elif row != None and column == None:
            row = int(row)
            try:
                print("coming from read_csv::",data[row-1])
                return data[row-2]
            except:
                raise ValueError("Wanted row number can not be greater than the number of rows in the file.")
        
        else:
            raise ValueError("without row or column and with both row and column, read_csv function can not be called.")
        """
    #----Z>>>>>!!!!!!!return the wanted column.!!!!!!!
    def read_xlsx(self,filename,row=None,column=None):
        try:
            excel_data = pd.read_excel(self.read_location + f"/{filename}")
        except FileNotFoundError as fe:
            raise ValueError(fe)
        
        if row == None and column != None:
            column = int(column)
            try: 
                wanteddata = excel_data.iloc[:,column]
                wanteddata = wanteddata.dropna()
                return wanteddata
            except:
                raise ValueError("Wanted column number can not be greater than no.of col. in data")

        elif row != None and column == None:
            row = int(row)
            try:
                wanteddata = excel_data.loc[2]
                wanteddata = wanteddata.dropna()
                return wanteddata

            except:
                raise ValueError("Row can not be greater than no.of rows in data")
        
        else:
            raise ValueError("without row or column and with both row and column, read_xls'x function can not be called.")



    def read_path_csv(self,filepath,row=None,column=None):
        try:
            csv_data = pd.read_csv(filepath)
        except:
            raise ValueError("File could not be found")
        
        if row == None and column != None:
            column = int(column)
            try:
                wanteddata = csv_data.iloc[:,column]
                wanteddata = wanteddata.dropna()
                return wanteddata
            except:
                raise ValueError("Wanted column number can not be greater than no.of col. in data")
        elif row != None and column == None:
            row = int(row)
            try:
                wanteddata = csv_data.loc[2]
                wanteddata = wanteddata.dropna()
                return wanteddata
            except:
                raise ValueError("Row can not be greater than no.of rows in data")
        else:
            raise ValueError("without row or column and with both row and column, read_csv function can not be called.")


    def read_path_xlsx(self,filepath,row=None,column=None):
        try:
            excel_data = pd.read_excel(filepath)
        except:
            raise ValueError(f"There is no such file in {filepath}")

        if row == None and column != None:
            column = int(column)
            try: 
                wanteddata = excel_data.iloc[:,column]
                wanteddata = wanteddata.dropna()
                return wanteddata
            except:
                raise ValueError("Wanted column number can not be greater than no.of col. in data")

        elif row != None and column == None:
            row = int(row)
            try:
                wanteddata = excel_data.loc[2]
                wanteddata = wanteddata.dropna()
                return wanteddata

            except:
                raise ValueError("Row can not be greater than no.of rows in data")
        
        else:
            raise ValueError("without row or column and with both row and column, read_xls'x function can not be called.")

        
        

    def via_link(self,link,roworcol):
        URL = link
        try:
            response = requests.get(URL)
        except:
            return "nolink",[None,None]
        text_content = response.text

        soup = BeautifulSoup(text_content, "html.parser")
        #print(soup.prettify())
        tables = soup.find_all("table")
        print(f"Number of Tables in the page {len(tables)}")
        table1 = tables[0]
        body = table1.find_all("tr")
        head = body[0] 
        body_rows = body[1:]
        headings = []
        for item in head.find_all("th"):
            item = (item.text).rstrip("\n")
            headings.append(item)
        all_rows = [] 
        for row_num in range(len(body_rows)): 
            row = [] 
            for row_item in body_rows[row_num].find_all("td"):
                row.append(row_item.text.strip())
            all_rows.append(row)
        all_rows = pd.DataFrame(all_rows)
        theInput = roworcol
        if theInput.startswith("row-"):
            theInput = theInput.split("-")
            try:
                willparameter = int(theInput[1])
            except:
                print("You did not say which row you want. Try again.")
                return "rcproblem",[link,None]
            try:
                wanteddata = all_rows.loc[willparameter]
                wanteddata = wanteddata.dropna()
                return "noproblem",[link,wanteddata]
            except ValueError as ve:
                print(ve)
                
        elif theInput.startswith("column-"):
            theInput = theInput.split("-")
            try:
                willparameter = int(theInput[1])
            except:
                print("You did not say which column you want. Try again")
                
            try:
                wanteddata = all_rows.iloc[:,willparameter]
                wanteddata = wanteddata.dropna()
                return "noproblem",[link,wanteddata]
                
            except ValueError as ve:
                print(ve)
                
        else:
            return "rcproblem",[link,None]
        
        
    
class Graphiquez():

    def __init__(self,database):
        self.database = database
        self.settings = stg.Settings()
        self.settings.read_settings()
        self.color = self.settings.get_setting("color")
        self.xlabel = self.settings.get_setting("xlabel")
        self.ylabel = self.settings.get_setting("ylabel")
        self.linestyle = self.settings.get_setting("linestyle")
        self.marker_plot = self.settings.get_setting("marker_plot")
        self.marker_scatter = self.settings.get_setting("marker_scatter")
        self.save_path = self.settings.get_setting("export_location")
        self.extension = self.settings.get_setting("export_extension")
        self.loc = self.settings.get_setting("legend_location")
        self.dpi = int(self.settings.get_setting("dpi"))
        self.fig , self.ax = plt.subplots()
        self.fileHandler = FileHandler()


        
        

    def default_save_name(self):
        today = date.today()
        name = str(today.strftime("%b-%d-%Y"))
        t = time.localtime()
        current_time = str(time.strftime("%H:%M:%S", t))
        current_time = current_time.replace(":","-")
        return name+current_time

    def bar(self,userInput,theFiles):
        try:
            xlabel = userInput["xlabel"]
        except:
            xlabel = self.xlabel
        try:
            ylabel = userInput["ylabel"]
        except:
            ylabel = self.ylabel
        try:
            color = userInput["color"]
        except:
            color = self.color
        try:
            title = userInput["title"]
        except:
            title = "bar chart"
        try:
            width = userInput["width"]
        except:
            width = 0.7
        
        x = theFiles[0][1]
        y = theFiles[1][1]

        try:
            self.ax.bar(x,y,color=color,linewidth=width)
            self.ax.set_title(title)
            self.ax.set_xlabel(xlabel)
            self.ax.set_ylabel(ylabel)
        except ValueError as ve:
            print(ve)
            return
        





    def plot(self,userInput,theFiles):
        try:
            color = userInput["color"]
        except:
            color = self.color
        try:
            xlabel = userInput["xlabel"]
        except:
            xlabel = self.xlabel
        try:
            ylabel = userInput["ylabel"]
        except:
            ylabel = self.ylabel
        try:
            linestyle = userInput["linestyle"]
        except:
            linestyle = self.linestyle
        try:
            marker = userInput["marker"]
        except:
            marker = self.marker_plot
        try:
            title = userInput["title"]
        except:
            title = "titleplot"
        try:
            loc = userInput["loc"]
        except:
            loc = self.loc
        try:
            label = userInput["label"]
        except:
            label = "line"

        x = theFiles[0][1]
        y = theFiles[1][1]
        """
        try:
            tempo = [float(i) for i in x]
            x = tempo
        except:
            pass
        try:
            tempo = [float(i) for i in y]
            y=tempo
        except:
            pass
        """
        try:
            data = x
            xtick = int(userInput["xtick"])
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                xtick = np.linspace(maxv,minv,xtick)
            else:
                xtick = [data[i] for i in range(0,len(data),xtick)]
        except:
            data = x
            print("THEDATA: ",data)
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                xtick = np.linspace(maxv,minv,10)
            else:
                xtick = [ data[i] for i in range(0,len(data),int(len(data)/10)) ]
        try:
            data = y
            ytick = int(userInput["ytick"])
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                ytick = np.linspace(maxv,minv,ytick)
            else:
                ytick = [data[i] for i in range(0,len(data),ytick)]
        except:
            data = y
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                ytick = np.linspace(maxv,minv,10)
            else:
                ytick = [ data[i] for i in range(0,len(data),int(len(data)/10)) ]




        try:
            self.ax.plot(x,y,color=color,linestyle = linestyle, marker = marker,label=label)
            self.ax.set(xlabel=xlabel,ylabel=ylabel,title=title)
            self.leg = self.ax.legend(loc=loc)
            """
            plt.xticks(xtick)
            plt.yticks(ytick)
            """
        except ValueError as ve:
            if str(ve).startswith("'color'"):
                print(f"Unrecognized color '{color}'. Try again")
                return
            print(ve,end=" ")
            print("Try again")





    
    def scatter(self,userInput,theFiles):
        try:
            color = userInput["color"]
        except:
            color = self.color
        try:
            xlabel = userInput["xlabel"]
        except:
            xlabel = self.xlabel
        try:
            ylabel = userInput["ylabel"]
        except:
            ylabel = self.ylabel
        try:
            linestyle = userInput["linestyle"]
        except:
            linestyle = self.linestyle
        try:
            marker = userInput["marker"]
        except:
            marker = self.marker_scatter
        try:
            title = userInput["title"]
        except:
            title = "titlescatter"
        try:
            loc = userInput["loc"]
        except:
            loc = self.loc
        try:
            label = userInput["label"]
        except:
            label = "scatter"

        x = theFiles[0][1]
        y = theFiles[1][1]

        """       try:
            tempo = [float(i) for i in x]
            x = tempo
        except:
            pass
        try:
            tempo = [float(i) for i in y]
            y=tempo
        except:
            pass"""
    
        try:
            data = x
            xtick = int(userInput["xtick"])
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                xtick = np.linspace(maxv,minv,xtick)
            else:
                xtick = [data[i] for i in range(0,len(data),xtick)]
        except:
            data = x
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                xtick = np.linspace(maxv,minv,10)
            else:
                xtick = [ data[i] for i in range(0,len(data),int(len(data)/10)) ]
        try:
            data = y
            ytick = int(userInput["ytick"])
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                ytick = np.linspace(maxv,minv,ytick)
            else:
                ytick = [data[i] for i in range(0,len(data),ytick)]
        except:
            data = y
            if isinstance(data[0],float):
                maxv = max(data)
                minv = min(data)
                ytick = np.linspace(maxv,minv,10)
            else:
                ytick = [ data[i] for i in range(0,len(data),int(len(data)/10)) ]

        try:
            self.ax.scatter(x,y,color=color,linestyle=linestyle,marker=marker,label=label)
            self.ax.set(xlabel=xlabel,ylabel=ylabel,title=title)
            self.leg = self.ax.legend(loc=loc)
            """
            plt.xticks(xtick)
            plt.yticks(ytick)
            """
        except ValueError as ve:
            if str(ve).startswith("'color'"):
                print(f"Unrecognized color '{color}'. Try again.")
                return
            
            print(ve,end=" ")
            print("Try again")
            return
        

        else:
            pass #saving process will be here.


        
    def pie(self,userInput,theFiles):
        try:
            title = userInput["title"]
        except:
            title = "titlepie"

        x = theFiles[0][1]
        y = theFiles[1][1]

        try:
            tempo = [float(i) for i in x]
            x = tempo
        except:
            pass
        try:
            tempo = [float(i) for i in y]
            y=tempo
        except:
            pass      


        try:
            self.ax.pie(y,labels=x,autopct="%1.1f%%")
            plt.title(title)
        except ValueError as ve:
            print(ve,end=" ")
            print("Try again.")

    
    def parse_input(self,userInput):
        userInput = userInput.strip()

        i = 0
        while i < len(userInput):
            if userInput[i] == "=":
                userInput = userInput[:i] +" "+ userInput[i+1:]
            
            i += 1 
        
        userInput = userInput.split()
        if len(userInput) % 2 == 1:
            raise ValueError("Something wrong with your code. Probably unmatched '='")

        inputDict = {}

        i = 0
        while i < len(userInput)-1:
            inputDict[userInput[i]] = userInput[i+1]
            i += 2
        return inputDict
    


    def file_chooser(self,axis):
        while True: #FILE CHOSE 
            self.fileHandler.print_all_files()
            print(f"Please choose the file that you will use FOR {axis} AXIS")
            theFile = input().strip()
            if theFile not in self.fileHandler.get_all_files():
                print(f"We could not found the file '{theFile}'. Please try again.")
                continue
            if theFile == "q":
                return
            print(f"You chose the file '{theFile}'. \nTo choose a row type row-(rownumber)\nTo choose a column type column-(columnnumber)\n")
            while True:
                theInput = input().strip()
                if not theInput:
                    continue
                if theInput == "q":
                    return
                if theInput.startswith("row-"):
                    theInput = theInput.split("-")
                    try:
                        willparameter = theInput[1]
                    except:
                        print("You did not say which row you want. Try again.")
                        continue
                    try:
                        if theFile.endswith(".csv"):
                            roworcol = self.fileHandler.read_csv(theFile,row=str(willparameter))
                        if theFile.endswith(".xlsx") or theFile.endswith(".xls"):
                            roworcol = self.fileHandler.read_xlsx(theFile,row=str(willparameter))
                        break
                    except ValueError as ve:
                        print(ve)
                        continue
                elif theInput.startswith("column-"):
                    theInput = theInput.split("-")
                    try:
                        willparameter = theInput[1]
                    except:
                        print("You did not say which column you want. Try again")
                        continue
                    try:
                        if theFile.endswith(".csv"):
                            roworcol = self.fileHandler.read_csv(theFile,column=willparameter)
                        if theFile.endswith(".xlsx") or theFile.endswith(".xls"):
                            roworcol = self.fileHandler.read_xlsx(theFile,column=willparameter)
                        break
                    except ValueError as ve:
                        print(ve)
                        continue
                else:
                    continue
                
            print("coming from filechooser::",roworcol)
            return [theFile,roworcol]
            
    def file_chooser_path(self,axis):
        while True: #FILE CHOSE 
            print(f"Please give the path of the file that you will use FOR {axis} AXIS")
            theFile = input().strip()
            try:
                with open(theFile):
                    pass
            except:
                print(f"We could not found the file '{theFile}'. Please try again.")
                continue
            if theFile == "q":
                return
            print(f"You chose the file '{theFile}'. \nTo choose a row type row-(rownumber)\nTo choose a column type column-(columnnumber)\n")
            while True:
                theInput = input().strip()
                if not theInput:
                    continue
                if theInput == "q":
                    return
                if theInput.startswith("row-"):
                    theInput = theInput.split("-")
                    try:
                        willparameter = theInput[1]
                    except:
                        print("You did not say which row you want. Try again.")
                        continue
                    try:
                        if theFile.endswith(".csv"):
                            roworcol = self.fileHandler.read_path_csv(theFile,row=str(willparameter))
                        if theFile.endswith(".xlsx") or theFile.endswith(".xls"):
                            roworcol = self.fileHandler.read_path_xlsx(theFile,row=str(willparameter))
                        break
                    except ValueError as ve:
                        print(ve)
                        continue
                elif theInput.startswith("column-"):
                    theInput = theInput.split("-")
                    try:
                        willparameter = theInput[1]
                    except:
                        print("You did not say which column you want. Try again")
                        continue
                    try:
                        if theFile.endswith(".csv"):
                            roworcol = self.fileHandler.read_path_csv(theFile,column=str(willparameter))
                        if theFile.endswith(".xlsx") or theFile.endswith(".xls"):
                            roworcol = self.fileHandler.read_path_xlsx(theFile,column=str(willparameter))
                        break
                    except ValueError as ve:
                        print(ve)
                        continue
                else:
                    continue
                
            print("coming from filechooser::",roworcol)
            return [theFile,roworcol]


    def change_file_data(self,userInput,theFiles):
        try:
            axis=userInput["changedata"].upper()      
        except:
            raise ValueError("...File could not be changed.")
            
        try:
            file=userInput["file"]
        except:
            file=None
        try:
            path = userInput["path"]
        except:
            path = None
        try:
            link = userInput["link"]
        except:
            link = None
        try:
            row = userInput["row"]
        except:
            row = None
        try:
            column = userInput["column"]
        except:
            column = None
        if row and column:
            raise ValueError("Both row and column can not be given")
        if not row:
            roworcol = "column-"+column
        if not column:
            roworcol = "row-" + row
        if not row and not column:
            raise ValueError("...No column or row information.")

        if not file and not path and not link:
            raise ValueError("...No file information.")
        elif file:
            try:
                if file.endswith(".csv"):
                    data = self.fileHandler.read_csv(file,row=row,column=column)
                if file.endswith(".xlsx") or file.endswith(".xls"):
                    data = self.fileHandler.read_xlsx(file,row=row,column=column)
            except ValueError as ve:
                print(ve)
                return
            if axis == "X":
                theFiles[0] = [file,data]
            if axis == "Y":
                theFiles[1] = [file,data]
            if axis == "Z":
                try:
                    theFiles[2] = [file,data]
                except:
                    raise ValueError("There is no Z axis.")
            return theFiles
        elif link:
            message,myFile = self.fileHandler.via_link(link,roworcol)
            if message == "nolink":
                raise ValueError("link could not be found")
            elif message == "rcproblem":
                raise ValueError("row column information must be defined well.")
            else:
                if axis == "X":
                    theFiles[0] = myFile
                if axis == "Y":
                    theFiles[1] = myFile
                if axis == "Z":
                    try:
                        theFiles[2] = myFile
                    except:
                        raise ValueError("There is no Z axis.")
            return theFiles
        elif path:
            try:
                if path.endswith(".csv"):
                    data = self.fileHandler.read_path_csv(path,row=row,column=column)
                if path.endswith(".xlsx") or path.endswith(".xls"):
                    data = self.fileHandler.read_path_xlsx(path,row=row,column=column)
            except ValueError as ve:
                print(ve)
                return
            if axis == "X":
                theFiles[0] == [path,data]
            if axis == "Y":
                theFiles[1] == [path,data]
            if axis == "Z":
                try:
                    theFiles[2] = [path,data]
                except:
                    raise ValueError("There is no Z axis.")
            return theFiles






    def complete_chooser(self,later=False,d3=False):
        theFiles = []
        while True:
            print("FOR X AXIS\n1->Use locations from settings.\n2->I want to give the path of the file\n3->Via link")
            number = input("Number: ").strip()
         
            if not number:
                if later:
                    theFiles.append(["None","None"])
                    break
                else:
                    continue
            if number == "1":
                myFile = self.file_chooser("X")
                theFiles.append(myFile)
                break
            if number == "2":
                myFile = self.file_chooser_path("X")
                theFiles.append(myFile)
                break
            if number == "3":
                link = input("\nPlease give the link: ")
                roworcol = input("row/col-number: ")
                message,myFile = self.fileHandler.via_link(link,roworcol)
                if message == "nolink":
                    print("link could not be found.")
                    continue
                if message == "noproblem":
                    theFiles.append(myFile)
                    break
                if message == "rcproblem":
                    print("row/column should be defined well!")
                    continue
        while True:
            print("FOR Y AXIS\n1->Use locations from settings.\n2->I want to give the path of the file\n3->Via link")
            number = input("Number: ").strip()
   
            if not number:
                if later:
                    theFiles.append(["None","None"])
                    break
                else:
                    continue
            if number == "1":
                myFile = self.file_chooser("Y")
                theFiles.append(myFile)
                break
            if number == "2":
                myFile = self.file_chooser_path("Y")
                theFiles.append(myFile)
                break
            if number == "3":
                link = input("\nPlease give the link: ")
                roworcol = input("row/col-number: ")
                message,myFile = self.fileHandler.via_link(link,roworcol)
                if message == "nolink":
                    print("link could not be found.")
                    continue
                if message == "noproblem":
                    theFiles.append(myFile)
                    break
                if message == "rcproblem":
                    print("row/column should be defined well!")
                    continue 
        while d3:
            print("FOR Z AXIS\n1->Use locations from settings.\n2->I want to give the path of the file\n3->Via link")
            number = input("Number: ").strip()
            
            if not number:
                if later:
                    theFiles.append(["None","None"])
                    break
                else:
                    continue
            if number == "1":
                myFile = self.file_chooser("Z")
                theFiles.append(myFile)
                break
            if number == "2":
                myFile = self.file_chooser_path("Z")
                theFiles.append(myFile)
                break
            if number == "3":
                link = input("\nPlease give the link: ")
                roworcol = input("row/col-number: ")
                message,myFile = self.fileHandler.via_link(link,roworcol)
                if message == "nolink":
                    print("link could not be found.")
                    continue
                if message == "noproblem":
                    theFiles.append(myFile)
                    break
                if message == "rcproblem":
                    print("row/column should be defined well!")
                    continue 
        return theFiles   

    def amateur_main(self):
        self.fig,self.ax = plt.subplots()
        sayac = 0 
        while True:
            if sayac == 0:
                pass
            else:
                proc = input("Do you want to continue to make graphs or you wish to go back?\n0->Continue\n1->Go back").strip()
                if proc == "0":
                    pass
                else:
                    break


            userInput = {}
            d3 = False
            theFiles = self.complete_chooser(later=False, d3=d3)
            title=input("What should be the title? To use default type 'default'\n").strip()
            if title =="default":
                title = None
            while True:
                color = input("Which color do you wish?\n0->default\n1->red\n2->blue\n3->green\n4->yellow\n").strip()
                if color == "1":
                    userInput["color"] = "red"
                    break
                elif color == "0":
                    break
                elif color == "2":
                    userInput["color"] = "blue"
                    break
                elif color == "3":
                    userInput["color"] = "green"
                    break
                elif color == "4":
                    userInput["color"] = "yellow"
                    break
                else:
                    continue
            xlabel = input("Please type the name of the x axis\n").strip()
            if xlabel == "default":
                pass
            else:
                userInput["xlabel"] = xlabel

            ylabel = input("Please type the name of the y axis\n").strip()
            if ylabel == "default":
                pass
            else:
                userInput["ylabel"] = ylabel

            print("Graphiquez works it on...")
            time.sleep(1)
            self.plot(userInput,theFiles)
            while True:
                process = input("Your graph is ready.\n0->Save it without showing\n1->Show me\n").strip()
                if process == "1":
                    self.show()
                    process = input("Do you want to save it?\n 0->No\n1->Yes\n").strip()
                    if process == "1":
                        userInput2 = {}
                        filename = input("Please give the name of the file. 'default' for default.\n").strip()
                        if filename != "default":
                            userInput2["name"] = filename
                        else:
                            pass
                        self.save(userInput2)
                        sayac += 1
                        break
                    else:
                        sayac += 1
                        break
                elif process =="0":
                    userInput2 = {}
                    filename = input("Please give the name of the file. 'default' for default \n")
                    if filename != "default":
                        userInput2["name"] = filename
                    else:
                        pass
                    self.save(userInput2)
                    sayac += 1
                    break


            

                



    def pro_main(self):
        while True:
            while True:
                d3 = input("---------------\nType '1' for load previous figures\nType '2' for 2D\nType 'q' for exit\n")
                d3 = d3.strip()
                if d3 == "2":
                    self.fig,self.ax = plt.subplots()
                    d3 = False
                    break
                if d3 == "1":
                    d3 = False
                    self.load_figure()
                    break
                elif d3 == "3":
                    continue
                elif d3 == "q":
                    return
                else:
                    continue
            

            theFiles = self.complete_chooser(later=False,d3=d3)

            while not d3:
                userInput = input("-->").strip()
                if userInput == "q":
                    self.fig,self.ax = plt.subplots()
                    break
                
                if userInput.startswith("draw"):
                    try:
                        userInput = self.parse_input(userInput)
                    except ValueError as ve:
                        print(ve)
                        continue

                    self.draw(userInput,theFiles)
                    continue

                elif userInput.startswith("show"):
                    self.show()
                    continue


                elif userInput.startswith("savefigure"):
                    try:
                        self.saveFigure()
                        print("Figure saved succesfully.")
                        continue
                    except ValueError as ve:
                        print(ve)
                        continue


                elif userInput.startswith("save"):
                    try:
                        userInput = self.parse_input(userInput)
                    except ValueError as ve:
                        print(ve)
                        continue
                    self.save(userInput)
                    print("Saved succesfully.")
                    return


                   

                elif userInput.startswith("help"):
                    self.help()
                
                elif userInput.startswith("exit"):
                    return
                elif userInput.startswith("changedata"):
                    try:
                        userInput = self.parse_input(userInput)
                        theFiles = self.change_file_data(userInput,theFiles)
                    except ValueError as ve:
                        print(ve)
                        continue
                elif userInput.startswith("print"):
                    for i in theFiles:
                        print(i[1])
                elif userInput.startswith("reset"):
                    self.fig, self.ax = plt.subplots()
                else:
                    print(f"..Unknown command for '{userInput}'")
                    continue
            
            while d3:
                pass

    def mathFunctions_main(self):
        self.fig,self.ax = plt.subplots()
        while True:
            process = input("q->quit\n2->2D\n3->3D\nNumber: ").strip()
            if process == "2":
                break
            elif process == "3":
                break
            elif process == "q":
                return
            else:
                print("That number does not exist.")
                continue
        
        if process == "2":
            while True:
                os.system("cls||clear")
                function = input("Please type your function\nq->quit\nDo not forget to add operators\n2x->Not allowed\n2*x->Allowed\nOnly paranthesis and x are allowed.\nFunction: ").strip()
                if function == "q":
                    return
                else:
                    for i in function:
                        if i not in ["(",")","*","-","+","/","x","1","2","3","4","5","6","7","8","9","0"]:
                            print(f"Your function contains things that are not allowed '{i}'")
                            time.sleep(1)
                            break
                        else:
                            continue
                    
                    i = 0
                    while i<len(function):
                        if function[i] == "x":
                            function = function[:i] + "(" + function[i] + ")" + function[i+1:]
                            i += 3
                        else:
                            i += 1
                    while True:

                        fromwhere=input("What should be the 'start' of the x axis?").strip()
                        towhere =input("What should be the 'end' of the x axis?").strip()

                        try:
                            fromwhere = int(fromwhere)
                            towhere = int(towhere)
                            break
                        except:
                            print("Not supported start-end points.")
                            time.sleep(1)
                            continue
                    
                    color = self.color
                    while True:
                        plotorscatter = input("1->Line graph\n2->Scatter graph\n")
                        if plotorscatter == "q":
                            return
                        elif plotorscatter == "1":
                            break
                        elif plotorscatter == "2":
                            break
                        else:
                            print("Only type 1 and 2.")
                            continue
                    
                    xaxis = list(np.linspace(fromwhere,towhere,100))
                    yaxis = []
                    for i in xaxis:
                        newfunction = function.replace("x",str(i))
                        try:
                            solve = eval(newfunction)
                        except:
                            print("Probably something wrong with your function. Try again.")
                            return
                        yaxis.append(solve)
                    
                    if plotorscatter == "1":
                        self.ax.plot(xaxis,yaxis,color=color)
                        self.ax.grid()
                        self.show()
                    elif plotorscatter == "2":
                        self.ax.scatter(xaxis,yaxis,color=color)
                        self.ax.grid()
                        self.show()
                    
                    

                    save = input("If you want to save please type 0\n").strip()
                    if save == "0":
                        filename = input("What should be the filename?")
                        self.fig.savefig(self.save_path + "/" + filename + self.extension)
                        print("Figure saved.")
                    else:
                        continue

        if process == "3":
            fig = plt.figure()
            ax = fig.add_subplot(projection = "3d")
            while True:
                
                os.system("cls||clear")
                function = input("Please type your function\nq->quit\nDo not forget to add operators\n2x->Not allowed\n2*x->Allowed\nOnly paranthesis,x and y are allowed.\nFunction: ").strip()
                if function == "q":
                    return
                for i in function:
                    if i not in ["(",")","*","-","+","/","x","y","1","2","3","4","5","6","7","8","9","0"]:
                        print(f"Your function contains nonsupported char '{i}'")
                        time.sleep(1)
                        break
                    else:
                        continue
                
                i = 0 
                while i<len(function):
                    if function[i] == "x" or function[i] == "y":
                        function = function[:i] + "(" + function[i] + ")" + function[i+1:]
                        i += 3
                    else:
                        i += 1
                
                print("If you want to use default do not type anything.")
                color = input("color: ")
                if not color:
                    color = self.color

                xlabel = input("xlabel: ")
                if not xlabel:
                    xlabel = self.xlabel
                ylabel = input("ylabel: ")
                if not ylabel:
                    ylabel = self.ylabel
                zlabel = input("zlabel: ")
                if not zlabel:
                    zlabel = "z axis"
                title=input("title: ")
                if not title:
                    title = "noTitle"
                while True:
                    fromwherex=input("What should be the 'start' of the ''X'' axis?\n").strip()
                    towherex =input("What should be the 'end' of the ''X'' axis?\n").strip()          
                    fromwherey = input("What should be the 'start' of the ''Y'' axis\n").strip()
                    towherey = input("What should be the 'end' of the ''Y'' axis\n").strip()
                    try:
                        fromwherex=int(fromwherex)
                        towherex = int(towherex)
                        fromwherey = int(fromwherey)
                        towherey = int(towherey)
                        break
                    except:
                        print("Not supported start-end points.")
                        time.sleep(1)
                        continue
                
                while True:
                    surplotscat = input("1->Line graph\n2->Scatter\nNumber: ").strip()
                    if surplotscat == "q":
                        return
                    elif surplotscat == "1" or surplotscat == "2":
                        break
                    else:
                        print("Please type only 1,2 and 3.")
                        continue
                        
                xaxis = list(np.linspace(fromwherex,towherex))
                yaxis = list(np.linspace(fromwherey,towherey))
                zaxis = []

                for i in range(len(xaxis)):
                    xvalue = xaxis[i]
                    yvalue = xaxis[i]
                    tempofunc = function.replace("x",str(xvalue))
                    newfunction = tempofunc.replace("y",str(yvalue))
                    try:
                        solve = eval(newfunction)
                    except:
                        print("Probably something wrong with your function. Process can not be done.")
                        time.sleep(3)
                        return
                    zaxis.append(solve)

                if surplotscat == "1":
                    ax.plot(xaxis,yaxis,zaxis,color=color)
                    ax.set_title(title)
                    ax.set_xlabel(xlabel)
                    ax.set_ylabel(ylabel)
                    ax.set_zlabel(zlabel)
                    ax.grid()
                    plt.show()
                elif surplotscat == "2":
                    ax.scatter(xaxis,yaxis,zaxis,color=color)
                    ax.grid()
                    plt.show()
                
                save = input("Do you want to save it\n0->Yes\nAnything else->No\n").strip()
                if save == "0":
                    filename = input("what should be the filename?\n")
                    fig.savefig(self.save_path + "/" + filename + self.extension)
                    print("Figure saved.")
                    time.sleep(2)
                    continue
                else:
                    continue

                    

                    
                    
                    
                    



                

                    


                    

                    



    def draw(self,userInput,theFiles):
        print(userInput)
        if userInput["draw"] == "line":
            self.plot(userInput,theFiles)
        elif userInput["draw"] == "scatter":
            self.scatter(userInput,theFiles)
        elif userInput["draw"] == "pie":
            self.pie(userInput,theFiles)
        elif userInput["draw"] == "bar":
            self.bar(userInput,theFiles)

    def help(self):
        print("drawing example:\n draw=<line,scatter..> color=<red,blue,green...> xlabel=.. ylabel=.. ....")
        print("\nSaving the figure: \n-->savefigure\nsave as a image:\n-->save")
        print("\nShowing the figure:\n-->show")
        print("\nExit/quit:\n-->exit \nor\n-->q")
    def save(self,userInput):
        try:
            saveloc = userInput["export_location"]
        except:
            saveloc = self.save_path
        try:
            extension = userInput["extension"]
        except:
            extension = self.extension
        try:
            name = userInput["name"]
        except:
            name= self.default_save_name()
        try:
            dpi = userInput["dpi"]
        except:
            dpi = self.dpi

        finalloc = saveloc.strip() +"/"+ name+extension.strip()
        print(finalloc)
        try:
            self.fig.savefig(finalloc,dpi=dpi)
        except:
            print("Could not be saved.")

        
    def __read(self):
        figx = pickle.load(open("tempofigureobject.fig.pickle","rb"))
        time.sleep(1)
        self.fig = figx
        self.ax = figx.axes[0]
        self.fig.set_dpi(self.dpi)

    def show(self):

        pickle.dump(self.fig,open("tempofigureobject.fig.pickle","wb"))
        time.sleep(1)
        self.fig.show()
        self.__read()

    def load_figure(self):
        all_files = []
        current_path = os.path.abspath(sys.argv[0]+"/../..")
        dir_list = os.listdir(current_path)
        for path in dir_list:
            if os.path.isfile(os.path.join(current_path,path)):
                if path.endswith(".pickle") and not path.startswith("tempo"):
                    all_files.append(path)
        mystr = ""
        
        if not all_files:
            print("There is not any file to load.")
            return
        for i in range(len(all_files)):
            if i != 0 and i %2 == 0:
                mystr += f"{all_files[i]:^30}    "
            else:
                mystr += f"{all_files[i]:30}\n"
        print(mystr)
        wantedfile = input("please type the name of the file that you want to load:\n-> ").strip()
        if wantedfile not in all_files:
            print("File could not be found.")
            time.sleep(1)
            return
        else:
            figx = pickle.load(open(wantedfile,"rb"))
            self.fig = figx
            self.ax = figx.axes[0]
            self.fig.set_dpi(self.dpi)



    #------->>>> SAVE THE FIGURE <<<<<<------
    def saveFigure(self):
        filename = input("please type the name(for time stamp type none)\n-> ").strip()
        if filename == "none":
            filename = self.default_save_name()
        filename += ".fig.pickle"
        pickle.dump(self.fig,open(filename,"wb"))



    
    def remove(self,labelName):
        for line in self.ax.lines:
            if str(line).endswith(f"({labelName})"):
                line.remove()
        for collection in self.ax.collections:
            collection.remove()


    #---->>>>> UPDATE PROCESSS <<<<<<<-------
    def update(self,labelName,color):
        pass

if __name__ == "__main__":
    x = range(10)
    y = list(map(lambda x:x*x,x))
    graph = Graphiquez()
    graph.scatter(x,y)