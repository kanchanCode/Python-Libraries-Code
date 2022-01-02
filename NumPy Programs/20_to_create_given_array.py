'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title : Write a Python program to create an array which looks like below array.

'''
import numpy as np

np_arr = np.tri(4, 3, -1)
#numpy.tri(R, C = None, k = 0, dtype = ‘float’)
#tri()=An array with ones at and below the given diagonal and zeros elsewhere.
#k : [int, optional, 0 by default]
#Diagonal we require; k>0 means diagonal above main diagonal or vice versa.
print(np_arr)