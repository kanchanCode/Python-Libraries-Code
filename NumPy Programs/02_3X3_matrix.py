'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Create a 3x3 matrix with values ranging from 2 to 10
'''
import numpy as np

np_matrix=np.arange(2,11).reshape(3,3) 
# arange to get range from 2 to 10
# reshape to shape it as 3X3 matrix
print(np_matrix)