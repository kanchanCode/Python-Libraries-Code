'''
@Author: Kanchan
@Date: 2022-01-02
@Last Modified by: Kanchan
@Last Modified time: 2022-01-02
@Title :Write a Python program to add, subtract, multiple and divide two Pandas Series.
'''

import pandas as pd
pd_ds=pd.Series([2,4,6,8,10])
print("Array1 is")
print(pd_ds)
pd_ds2=pd.Series([1,3,5,7,9])
print("Array2 is")
print(pd_ds2)

print("Addition of array1 and array2 is")
print(pd_ds+pd_ds2)

print("Subtion of array1 and array2 is")
print(pd_ds-pd_ds2)

print("Multiplication of array1 and array2 is")
print(pd_ds*pd_ds2)

print("Division of array1 and array2 is")
print(pd_ds/pd_ds2)