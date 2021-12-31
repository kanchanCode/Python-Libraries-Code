'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to reverse an array (first element becomes last).

'''
import numpy as np

np_arr=np.arange(12,38)
print(type(np_arr))
print("Original array is ",np_arr)
np_arr=np_arr[::-1]   #using slice to reverse
print("Reverse of array is",np_arr)