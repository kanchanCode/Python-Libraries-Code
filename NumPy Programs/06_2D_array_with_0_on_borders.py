'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to add a border (filled with 0's) around an existing array

'''
import numpy as np

np_arr=np.zeros((5,5)) # to create 5X5 array with 1 filled in it
print(np_arr)

#np_arr[1][1]=1
#np_arr[1,1]=1
np_arr[1:-1,1:-1]=1  # to access specified elements and change value 
print("0 on borders and 1 inside\n",np_arr)
