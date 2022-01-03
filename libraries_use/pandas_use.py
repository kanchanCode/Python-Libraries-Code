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

newdf=pd.DataFrame(np.random.rand(100,5))
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

#DATAFRAME

newdf1=pd.DataFrame(np.random.rand(334,5),index=np.arange(334))
#pandas.DataFrame( data, index, columns, dtype, copy)

print(newdf1)
print(newdf.head(5))

df=pd.DataFrame() 
# empty dataframe

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)
#list to dataframe

data={'name':['Abc','Xyz'],'age':[60,20]}
df=pd.DataFrame(data,index=np.arange(2))
print(df)
print(type(df))
#dict to dataframe

print(newdf.describe())
print(newdf.dtypes)

print(newdf.index)
print(newdf.columns)
print(newdf.to_numpy())
print(type(newdf.to_numpy()))
#pandas t numpy

print(newdf.T) #transpose
print(newdf.sort_index(axis=0,ascending=False))  #sort rows descending

print(newdf[0])
print(type(newdf[0])) #series
# combination of series->data frame

#copy and view in pandas

newdf2=newdf # it is a view for newdf
newdf3=newdf.copy() # to copy

newdf[0][0]=12346  # changing original data
#newdf3[0][0]=8757

print(newdf2) # view is getting reflected with the change
print(newdf3) #no change 
 
newdf.loc[0,0]=654  #  use loc to change the value
print(newdf.head())
print(newdf2.head())
print(newdf3.head())

newdf.columns=list("ABCDE") #clumn name change
print(newdf.head(2))

print(newdf.drop('D',axis=1)) # drop column

print(newdf.loc[[1,2],['C','D']]) # returns a copy of it 
print(newdf.loc[:,['C','D']]) # returns all row and C,D column
print(newdf.loc[[1,2],:]) # returns all columns and 1,2 row


#DATABASE TYPE QUERIES
print(newdf.loc[newdf ['A']<0.3])

print(newdf.loc[(newdf ['A']<0.3) & (newdf['C']>0.1)])