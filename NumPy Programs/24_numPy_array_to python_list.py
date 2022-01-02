'''
@Author: Kanchan
@Date: 2022-01-01
@Last Modified by: Kanchan
@Last Modified time: 2022-01-01
@Title : Write a Python program to convert a NumPy array into Python list structure.
Expected Output:
Original array elements:
[[0 1]
[2 3]
[4 5]]
Array to list:
[[0, 1], [2, 3], [4, 5]]

'''
import numpy as np

np_arr=np.arange(6).reshape(3,2)
print("Array is ")
print(np_arr)
print("List is ",np_arr.tolist())