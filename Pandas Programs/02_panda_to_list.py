'''
@Author: Kanchan
@Date: 2022-01-02
@Last Modified by: Kanchan
@Last Modified time: 2022-01-02
@Title :Write a Python program to convert a Panda module Series to Python list and it's type.
'''

import pandas as pd
pd_ds=pd.Series([2,4,6,8,10])
#series
print(pd_ds)
print(type(pd_ds))
print("Converted list is")
print(pd_ds.tolist())
print(type(pd_ds.tolist()))
