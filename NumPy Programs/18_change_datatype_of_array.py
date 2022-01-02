'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title : Write a Python program to change the data type of an array.


'''
import numpy as np
np_array=np.array([[2,4,6],[6,8,10]])
print(np_array)
print(np_array.dtype)

float_arr=np_array.astype(float)
#astype()=change the data type of array
print(float_arr)
print(float_arr.dtype)

