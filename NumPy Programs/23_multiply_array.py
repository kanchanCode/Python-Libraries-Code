'''
@Author: Kanchan
@Date: 2022-01-01
@Last Modified by: Kanchan
@Last Modified time: 2022-01-01
@Title : Write a Python program to create an array of (3, 4) shape, multiply every element
value by 3 and display the new array

'''
import numpy as np
np_array=np.arange(0,12).reshape((3,4))
print("Array is ")
print(np_array)
for i in np.nditer(np_array,op_flags=['readwrite']):
    i[...]=3*i
print("After multiplication ")
print(np_array)
#nditer()=It is an efficient multidimensional iterator object using which it is possible to iterate over an array

'''
op_flagslist of list of str, optional
This is a list of flags for each operand. At minimum, one of readonly, readwrite, or writeonly must be specified.

readonly indicates the operand will only be read from.

readwrite indicates the operand will be read from and written to.

writeonly indicates the operand will only be written to.

no_broadcast prevents the operand from being broadcasted.

contig forces the operand data to be contiguous.

aligned forces the operand data to be aligned.

nbo forces the operand data to be in native byte order.

copy allows a temporary read-only copy if required.

updateifcopy allows a temporary read-write copy if required.

allocate causes the array to be allocated if it is None in the op parameter.

no_subtype prevents an allocate operand from using a subtype.

arraymask indicates that this operand is the mask to use for selecting elements when writing to operands with the ‘writemasked’ flag set. The iterator does not enforce this, but when writing from a buffer back to the array, it only copies those elements indicated by this mask.

writemasked indicates that only elements where the chosen arraymask operand is True will be written to.

overlap_assume_elementwise can be used to mark operands that are accessed only in the iterator order, to allow less conservative copying when copy_if_overlap is present.
'''