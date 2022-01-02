'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title :Write a Python program to find the set exclusive-or of two arrays. Set exclusive-or
will return the sorted, unique values that are in only one (not both) of the input arrays.
'''
import numpy as np
np_arr1=np.array([0, 10, 20, 40, 60, 80])
np_arr2=np.array( [10, 30, 40, 50, 70, 90])
sorted_and_exclusive=np.setxor1d(np_arr1,np_arr2)
print("Sorted and unique differnce ",sorted_and_exclusive)
#numpy.setxor1d() function find the set exclusive-or of two arrays and return the sorted, unique values 
# that are in only one (not both) of the input arrays.
#Return : [ndarray] Sorted 1D array of unique values that are in only one of the input arrays

