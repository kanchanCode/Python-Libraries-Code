import numpy as np
import pandas as pd 
import random
'''
Pandas -> data analysis open source library 
Can use excel data in code
leverages the power and speed of numpy to make data analysis and prepocessing
provides rich and highly robust data operation

Pandas has two types pf data structures
1. Series- It is 1D array with indexes, it stores a single column or row of data in a dataframe
                     OR
            1D array(labeled) capable of holding any type of data is called series         
2.Dataframe- It is a tabular spreadsheet like structure representing rows each of which
             contains one or multiple columns 
                  OR
            2D data structure with columns of potentially diff data types is called Dataframe

'''


#IMPLEMENTATION

#creating a dataframe

ser=pd.Series(np.random.rand(34))
print(ser)
print(type(ser))

newdf=pd.DataFrame(np.random).rand(100,5)
print(newdf )
print(newdf)

dict1={"name":['Kanchan','Abc','Xyz'],
      "city":['Delhi','Mumbai','Agra']}

df=pd.DataFrame(dict1)
print(df)
print(type(df))
print(type(dict1.keys ))
#dictionary to dataframe

csv_file=df.to_csv('dataIndexFalse.csv',index=False)
print(csv_file)
#convert to csv file/excel file
print(df.head(2)) #first 2 lines
print(df.tail(2)) #last 2 lines
print(df.describe()) #will calculate count,mean,std,min etc

name=pd.read_csv('data.csv')
print(name)
# read csv file

#accessing data
print(name['city'])
print(name['city'][0])
name['city'][0]='UP'              #updated value of 'city'='UP'
name1=pd.read_csv('data.csv')
print(name)

name.index=['first','second','third']
print(name)
#to fetch rows ->use index
#to fetch column -? column name