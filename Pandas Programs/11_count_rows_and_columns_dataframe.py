'''
@Author: Kanchan
@Date: 2022-01-03
@Last Modified by: Kanchan
@Last Modified time: 2022-01-03
@Title : Write a Python program to count the number of rows and columns of a DataFrame.

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
print("Total number of rows : ",len(df.axes[0]))  #axis 0 =rows
print("Total number of columns : ",len(df.axes[1])) #axis 1= column