'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to create a 2d array with 1 on the border and 0 inside.


'''
import numpy as np

np_arr=np.ones((5,5)) # to create 5X5 array with 1 filled in it
print(np_arr)

#np_arr[1][1]=0
#np_arr[1,1]=0
np_arr[1:-1,1:-1]=0  # to access specified elements and change value 
print("1 on borders and 0 inside",np_arr)

