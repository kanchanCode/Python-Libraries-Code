'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a Python program to convert a list of numeric value into a one-dimensional
NumPy array. 
'''
import numpy as np

list1=[12.23,13.32,100,36.32]
print("List is",list1)
print(type(list1))

np_arr=np.array(list1) #converting it to array
print("NumPy array is",np_arr)
print(type(np_arr))