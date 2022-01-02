'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title : Write a Python program to create a contiguous flattened array.

'''
import numpy as np
np_arr = np.array([[10, 20, 30], [20, 40, 50]])
print("Original array:")
print(np_arr)
new_arr = np.ravel(np_arr)
# ravel creates 1D array
print("New flattened array:")
print(new_arr)
