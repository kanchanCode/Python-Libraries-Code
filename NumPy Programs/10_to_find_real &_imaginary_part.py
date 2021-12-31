'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to find the real and imaginary parts of an array of complex
numbers.

'''
import numpy as np

np_arr=np.array([[1+0.j],[0+0.70710678j]])
print("Original array is ")
print(np_arr)
print("Real part of the array")
print(np_arr.real)
print("Imaginary part of the array")
print(np_arr.imag)

# x = np.sqrt([1+0j])
# y = np.sqrt([0+1j])
# print("Original array:x ",x)
# print("Original array:y ",y)
# print("Real part of the array:")
# print(x.real)
# print(y.real)
# print("Imaginary part of the array:")
# print(x.imag)
# print(y.imag)