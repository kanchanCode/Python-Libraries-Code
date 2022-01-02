'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title : Write a Python program to find the set difference of two arrays. The set difference
will return the sorted, unique values in array1 that are not in array2.
'''
import numpy as np
np_arr1=np.array([0, 10, 20, 40, 60, 80])
np_arr2=np.array( [10, 30, 40, 50, 70, 90])
sorted_and_unique=np.setdiff1d(np_arr1,np_arr2)
print("Sorted and unique differnce ",sorted_and_unique)
#numpy.setdiff1d() function find the set difference of two arrays and return the unique values in arr1 that are not in arr2
#Return : [ndarray] 1D array of values in arr1 that are not in arr2. 
# The result is sorted when assume_unique = False, but otherwise only sorted if the input is sorted