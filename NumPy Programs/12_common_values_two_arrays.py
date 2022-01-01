'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title :12. Write a Python program to find common values between two arrays.
'''
import numpy as np
np_arr1=np.array([10,20,30])
np_arr2=np.array([40,20,30])
print("Array1 is",np_arr1)
print("Array2 is",np_arr2)
print("Common elements between array1 and array2 are")
print(np.intersect1d(np_arr1,np_arr2))
'''
intersect1d(ar1, ar2)
Find the intersection of two arrays.
Return the sorted, unique values that are in both of the input arrays.
'''
# #for multi_dimension array
# def multidim_intersect(np_arr1, np_arr2):
#     arr1_view = np_arr1.view([('',np_arr1.dtype)]*np_arr1.shape[1])
#     #ndarray.view([dtype][, type])
#     #New view of array with the same data.

#     arr2_view = np_arr2.view([('',np_arr2.dtype)]*np_arr2.shape[1])
#     intersected = np.intersect1d(arr1_view, arr2_view)
#     return intersected.view(np_arr1.dtype).reshape(-1, np_arr1.shape[1])

# multidim_intersect(np_arr1,np_arr2)
