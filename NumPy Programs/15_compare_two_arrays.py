'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title : Write a Python program compare two arrays using numpy.
'''
import numpy as np
np_arr1=np.array([1,2])
print("array1 is",np_arr1)

np_arr2=np.array( [4,5])
print("array2 is",np_arr2)

print("array1 > array2")
print(np.greater(np_arr1,np_arr2))

print("array1 >= array2")
print(np.greater_equal(np_arr1,np_arr2))

print("array1 < array2")
print(np.less(np_arr1,np_arr2))

print("array1 <= array2")
print(np.less_equal(np_arr1,np_arr2))

# comparison= np_arr1==np_arr2
# equal_arrays=comparison.all()
# print(equal_arrays)
#the == operator to compare two NumPy arrays to generate a new array object. Call ndarray.all() 
# with the new array object as ndarray to return True if the two NumPy arrays are equivalent.
