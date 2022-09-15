# GRAPHIQUEZ
### A data visualizer application that runs on terminal.








**After installing the requirements in the requirements.txt** All you have to do is **run main.py**



-
-
-
-
-

This project uses a cloud database which is mongodb atlas. In the database for log records, your ip adress and computer name will be saved. For enable you to manage your accounts this application also saves your username and your password-encrypted with SHA256-. 



        
----------------------------------------------------------------------------------------------------------------------------------------------------------
For the instructor who is reading this, 
You can use this account instead of creating a new one: username = ITUADMIN
                                                        password = ITUITUADMINADMIN1773
               
In the submission there is a file **accinfos** in the folder important which includes all information about database access. To manage the database, a completely new gmail account and mongodb account are created. I have shared the passwords information, birthday information, gender information etc.. 

---------------------------------------------------------------------------------------------------------------------------------------------------------
-
-

-
-
-
-
-
-
-
-






------------------------------------------
After logging in, you have 4 choices:
--------------------------------------


1. Settings 
  - You can change the settings in here.
2. Graphiquez for datasets
  - Choose datasets and plot them as you wish
3. Graphiquez for mathematical functions
  - Choose 2D or 3D and give the function, let it plot
4. Account
  - See the account informations
  
  
  
  
 -
 -
 -
 -
 -
 -
 -
 -
 -
 -
 
  
  
  
---------------------------------------------------------------
Graphiquez for dataset PRO mode
---------------------------------------------------------------

You will choose datasets that will be used for x axis and y axis. You have 3 options;
1. Use files that located on default folder 
2. Give the path 
  -You should give the complete path.
3. Give the link
  - Be sure that the link contains html table.

-
-
-
-
-




After choosing the datasets you will be greeted with something like terminal provided below. 
-->
-->
-->
In this section, there are some functions that you can use. 
Those are;


1. draw
  - Ables you to draw graphs
    - example: draw=scatter color=blue xlabel=xaxis ylabel=yaxis title=mygraph
2. show
  -It will show the graph
    - example: just type 'show'
3. savefigure
  - To save figure as a figure, not as a image. This will allow you to work on it again.
4. save
  - It will the figure as a image.
5. changedata 
  - This function allows you to change the dataset/row-column that you are working on.
    - e.g -> changedata=x file=example.xlsx column= 0 (the data for x axis changed with 0th column of example.csv)
6. reset
  - This will reset the figure. Everything will be deleted.
 
 

 
**__USAGES AND ALL PARAMETERS__**

Note: You do not have to give all of the parameters. The ones that you did not use will be default.
```
--DRAW--------------------------------------------------------------------------------------------------------------------------------------------------------
draw=line color= <red,blue,green...>   label= <name_it>  xlabel = <name_it>    ylabel = <name_it>    title = <name_it>    
          linestyle= <solid,dashed...>  marker = <o,-...>

draw=scatter color = <red....>   label = <name_it>    xlabel = <name_it   ylabel = <name_it>   title = <name_it> 
             marker = <o,-....>  
             
draw=bar  color = <...>     xlabel=<name_it>     ylabel=<name_it>       title = <name_it>          width = <e.g 0.7>

draw=pie  title=<name_it> 
--------------------------------------------------------------------------------------------------------------------------------------------------------------
-
-
-

-NON PARAMETER FUNCTIONS--------------------------------------------------------------------------------------------------------------------------------------

show

savefigure 

reset 

-------------------------------------------------------------------------------------------------------------------------------------------------------------
-
-
-
---SAVE----------------------------------------------------------------------------------------------------------------------------------------------------
#If you use 'name' parameter it will be saved on default folder. 
#If you use 'path' parameter it will be saved on the given path. 
#e.g -> path = /users/myname/desktop/myfolder/example 
        extension = .jpeg

save=<typeanythinghere>     extension = <.jpeg,.jpg,.png....>    'name = <nameoftheimage>    'OR'    export_location = <path> '        dpi = <250,300...>

----------------------------------------------------------------------------------------------------------------------------------------------------------
-
-
-
--------------CHANGEDATA------------------------------------------------------------------------------------------------------------------------------

#Be aware that 'file' parameter search the file on default folder. You can check/change default folder on settings section.

changedata = <x,y>      file=<nameofthefile.csv/xlsx>            'row = <rownumber>      'OR'     column = <columnnumber>'
changedata = <x,y>      path=<thepathofthefile.csv/xlsx>         'row = <rownumber>      'OR'     column = <columnnumber>'
changedata = <x,y>      link=<thelink>                           'row = <rownumber>      'OR'     column = <columnnumber>'

----------------------------------------------------------------------------------------------------------------------------------------------------------

```
     
----------------------------------------------------------------------------------------------------------------------------------------------------------
#GRAPHIQUEZ FOR AMATEURS
----------------------------------------------------------------------------------------------------------------------------------------------------------
Again, you will choose datasets for x and y axis. But this time the parameters will be given as ordinary inputs.
type 'default' to a input if you want a default parameter.



----------------------------------------------------------------------------------------------------------------------------------------------------------
#GRAPHIQUEZ FOR MATHEMATICAL FUNCTIONS.
----------------------------------------------------------------------------------------------------------------------------------------------------------
1. 2D
2. 3D
-
-

Firstly, it will ask you to type your function. _The functions only x and y are allowed. No sin, cos, etc._
Important note: 
Do **not** write _2x_

Do     write _2*x_

Do **not** write _x^2_

Do     write _x**2_

-
-

Then it will ask for the limits of x axis. Type as you wish.





