'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to create a null vector of size 10 and update sixth value to 11.

'''
import numpy as np

np_arr=np.zeros(10) 
print(np_arr)
np_arr[5]=11 #index 5 =6th element
print("Updated 6th elemment to 11",np_arr)
