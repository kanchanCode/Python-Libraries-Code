'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to append values to the end of an array.
'''
import numpy as np

np_arr=[10,20,30]
print("Original array")
print(np_arr)
np_arr=np.append(np_arr,[[30,40,50],[60,70,80]]) #using np.append()
print("After appending values")
print(np_arr)