'''
@Author: Kanchan
@Date: 2022-01-01
@Last Modified by: Kanchan
@Last Modified time: 2022-01-01
@Title : Write a Python program to make an array immutable (read-only).

'''
import numpy as np
np_array=np.arange(1,11)
print("Araay is ",np_array)
np_array.flags.writeable=False
print("Trying to change the value of an array")
np_array[0]=3
print("Updated array is",np_array)

'''
numpy.flags

The ndarray object has the following attributes. Its current values are returned by this function.
Sr.No.	Attribute & Description
1	C_CONTIGUOUS (C)   The data is in a single, C-style contiguous segment

2	F_CONTIGUOUS (F)   The data is in a single, Fortran-style contiguous segment

3	OWNDATA (O)        The array owns the memory it uses or borrows it from another object

4	WRITEABLE (W)      The data area can be written to. Setting this to False locks the data, making it read-only

5	ALIGNED (A)        The data and all elements are aligned appropriately for the hardware

6	UPDATEIFCOPY (U)   This array is a copy of some other array. When this array is deallocated, the base array will be updated with the contents of this array
'''