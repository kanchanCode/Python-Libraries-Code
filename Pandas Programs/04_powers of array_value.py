'''
@Author: Kanchan
@Date: 2022-01-02
@Last Modified by: Kanchan
@Last Modified time: 2022-01-02
@Title : Write a Python program to get the powers of an array values element-wise.

'''

import pandas as pd
import numpy as np
pd_ds=pd.Series([0,1,2,3,4,5,6])
print("Original array is")
print(pd_ds)
pow_arr=np.power(pd_ds,3)
print("Power of the array")
print(pow_arr)