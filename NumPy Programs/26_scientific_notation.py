'''
@Author: Kanchan
@Date: 2022-01-01
@Last Modified by: Kanchan
@Last Modified time: 2022-01-01
@Title : Write a Python program to suppresses the use of scientific notation for small
numbers in numpy array.
'''
import numpy as np
np_arr=np.array([1.6e-10, 1.6, 1200, .235])
print("Array is ",np_arr)
np.set_printoptions(suppress=True)
print(np_arr)