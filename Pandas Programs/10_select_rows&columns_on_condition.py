'''
@Author: Kanchan
@Date: 2022-01-02
@Last Modified by: Kanchan
@Last Modified time: 2022-01-02
@Title : Write a Python program to select the rows where the number of attempts in the
         examination is greater than 2.


'''

import pandas as pd
import numpy as np

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df=pd.DataFrame(exam_data,labels)
print("Summary is") 
#print(df.head(3)) #to print summary
print(df[df['attempts']>2]) # selecting dataframe rows where attempts >2
