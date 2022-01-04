'''
@Author: Kanchan
@Date: 2022-01-03
@Last Modified by: Kanchan
@Last Modified time: 2022-01-03
@Title : Write a Python program to insert a new column in existing DataFrame.
'''
import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df=pd.DataFrame(exam_data,index=labels)
age=[24,25,26,22,30,25,26,27,22,23]
df['age']=age
print("New column age is inserted")
print(df)