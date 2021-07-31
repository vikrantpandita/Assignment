# Assignment
===================================================================================================
Question 1 : Write a program to get data from API and write it to excel.
The below API returns JSON response. Get the data from API and save as excel. The first row in
the excel file should be header with same column names as JSON keys.


import pandas as pd  //first ,Installed pandas and imported it as pd
url = 'https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog'  //
x = pd.read_csv(url)   //used .read_csv function for reading any delimited text file
s=x.describe()    //  describe() is used to view some basic statistical details 
print(s)  
s.to_excel('test.xlsx')  // to_excel() method is used to export the DataFrame to the excel file

=====================================================================================================
QUESTION 2
Write a program which accepts text input from user and saves it in a text file. This file should be
saved in a directory named after today’s date(dd-mm-yyyy). A new file should be created each
time the user runs this program. Feel free to have any file name of your choice.


import time
import os

timestr = time.strftime("%Y-%m-%d")  // used time module function to get current date 
directory = timestr
  
parent_dir = "D:\coding"
  
path = os.path.join(parent_dir, directory) 
if os.path.isdir(path): // checking if the directory with the same name already exists 
    pass
else:
    os.mkdir(path) // creating directory if directory does not exit
    print("Directory '% s' created" % directory)
os.chdir(path)  // changing directory to newly created directory 
where = input('name of the file  ')


text = input('taking input from user ')


saveFile = open(where, 'w')
saveFile.write(text)
saveFile.close()
