import settings as stg
import os
import sys
import matplotlib.pyplot as plt
import numpy as np






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
                if path.endswith(".csv") or path.endswith(".docx") or path.endswith(".xlsx") or path.endswith(".py"):
                    all_files.append(path)
        return all_files

    def print_all_files(self):
        all_files = self.get_all_files()
        str = ""
        i = 0
        while i<len(all_files)-1:
            toadd1 = all_files[i]
            toadd2 = all_files[i+1]
            tempo = f"{toadd1:50} {toadd2:50} \n"
            str += tempo
            i = i + 2
        print(str)

a = """1-      export_location      -> /Users/serdarnazli/Desktop/ITU/21-22 Bahar/YZV104E/Graphiquez/main 
2-       read_location       -> /Users/serdarnazli/Desktop/ITU/21-22 Bahar/YZV104E/Graphiquez/main 
3-     export_extension      ->           .jpeg           
4-           color           ->             b             
5-          xlabel           ->          Axis X           
6-          ylabel           ->          Axis Y           
7-         linestyle         ->           solid           
8-            dpi            ->            250            
9-        marker_plot        ->           None            
10-      marker_scatter       ->             o             
11-      legend_location      ->        upper left         
13-           mode            ->            pro       """

"""a = a.split("\n")
print(a[0],a[1],a[2],a[3],sep="\n")
b = []
for i in range(len(a)):
    row = a[i].split("->")
    index = row[0].index("-")
    row[0] = row[0][index+1:].strip()
    row[1] = row[1].strip()
    b.append(row)
for i in b:
    print(i)

print(b[2])"""
"""
a = "      draw color   =   red   title= moruk     "
a = a.strip()
print(a)
a = a[4:]
i = 0
while i  < len(a):
    if a[i] == "=":
        a = a[:i] + a[i+1:]
    i += 1 

a = a.split()
print(a)
temp = list()
for i in a:
    if i == "=":
        continue
    elif "=" in i:
        try:
            i = i.split("=")
            temp.append(i[0],i[2])
        except:
            print("somethings wrong with your code. try again.")
    else:
        temp.append(i)

print(temp)
"""

"""formula = "x**2-2*x"
i = 0
while i<len(formula):
    if formula[i] == "x":
        formula = formula[:i] + "(" + formula[i] + ")" +  formula[i+1:]
        i += 3
    else:
        i += 1
        
print(formula)"""


fig = plt.figure()
ax = fig.add_subplot(projection="3d")
x = np.linspace(-50,50,20)
y = np.linspace(-50,50,20)
#x,y= np.meshgrid(x,y)
z = x*y
ax.plot(x,y,z)
ax.set_title("title")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid()
fig.savefig("selamlarcanım.jpg")
plt.show()