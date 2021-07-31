# Assignment
Question 1 : Write a program to get data from API and write it to excel.
The below API returns JSON response. Get the data from API and save as excel. The first row in
the excel file should be header with same column names as JSON keys.


import pandas as pd  //first ,Installed pandas and imported it as pd
url = 'https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog'  //
x = pd.read_csv(url)   //used .read_csv function for reading any delimited text file
s=x.describe()    //  describe() is used to view some basic statistical details 
print(s)  
s.to_excel('test.xlsx')  // to_excel() method is used to export the DataFrame to the excel file
