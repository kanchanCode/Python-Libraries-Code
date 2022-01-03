'''
@Author: Kanchan
@Date: 2022-01-01
@Last Modified by: Kanchan
@Last Modified time: 2022-01-01
@Title : Write a Python program to remove specific elements in a numpy array

'''
import numpy as np
np_arr=np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
index = [0, 3, 4]
print("Array is ")
print(np_arr)
print("After deleting 1,4,5 element ")
new_arr=np.delete(np_arr,index)
print(new_arr)