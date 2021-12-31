'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
'''
import numpy as np

np_arr=np.zeros((8,8)) # to create 5X5 array with 1 filled in it
print(np_arr)

np_arr[1::2,::2]=1 #for axis=1
#seq[start:stop:step]
#[::2] alternate items from 0,2,4,6
#[1::2 ]# to find alternate items
np_arr[::2,1::2]=1 #for axis=0
print("Check board Pattern")
print(np_arr)
