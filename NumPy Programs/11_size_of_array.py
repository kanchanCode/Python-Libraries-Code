'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title :Write a Python program to find the number of elements of an array, length of one
array element in bytes and total bytes consumed by the elements.
'''
import numpy as np
np_arr=np.array([1,2,3])
print("Size of array ",np_arr.size)
print("Length of the array ",np_arr.itemsize )
#array.itemsize =Length of one array element in bytes.
#array.nbytes = function return total bytes consumed by the elements of the array.
#print("Total bytes comsumed by the array ",np_arr.itemsize*np_arr.size)
print("Total bytes comsumed by the array ",np_arr.nbytes)
