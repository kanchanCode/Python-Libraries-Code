'''
@Author: Kanchan
@Date: 2022-01-01
@Last Modified by: Kanchan
@Last Modified time: 2022-01-01
@Title : Write a Python program to concatenate two 2-dimensional arrays.

'''
import numpy as np
# Creating two 2D arrays
# arr1 = np.arange(1,10).reshape(3,3)
# arr2 = np.arange(10,19).reshape(3,3)

array1=np.array([[0, 1, 3], [5, 7, 9]])
array2=np.array([[0, 2, 4], [6, 8, 10]])
print(array1)
print("and")
print(array2)
# Concatenating operation
# axis = 1 implies that it is being done column-wise
print("Contacted array is ")
print(np.concatenate((array1,array2),axis=1))
 