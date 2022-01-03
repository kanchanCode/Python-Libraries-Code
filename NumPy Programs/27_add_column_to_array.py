'''
@Author: Kanchan
@Date: 2022-01-01
@Last Modified by: Kanchan
@Last Modified time: 2022-01-01
@Title : Write a Python program to how to add an extra column to an numpy array.

'''
import numpy as np
np_array=np.array([[10,20,30],[40,50,60]])
print("Array is ")
print(np_array)
column=np.array([[100],[200]])
print("Added column ")
print(np.append(np_array,column,axis=1))