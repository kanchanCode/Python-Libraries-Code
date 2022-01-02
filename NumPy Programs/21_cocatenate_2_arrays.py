'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title : Write a Python program to concatenate two 2-dimensional arrays.

'''
import numpy as np
# Program to concatenate two 2D arrays column-wise
# import numpy

# Creating two 2D arrays
arr1 = np.arange(1,10).reshape(3,3)
arr2 = np.arange(10,19).reshape(3,3)
print(arr1,"and",arr2)

# Concatenating operation
# axis = 1 implies that it is being done column-wise
print(np.concatenate((arr1,arr2),axis=1))
