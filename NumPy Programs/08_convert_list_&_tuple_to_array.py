'''
@Author: Kanchan
@Date: 2021-12-30
@Last Modified by: Kanchan
@Last Modified time: 2021-12-30
@Title :Write a list and tuple into arrays.
'''
import numpy as np

list1=[1,2,3,4,5,6]
print(type(list1))
print("List is",list1)
tuple1=(7,8,9,10,11,12)
print(type(tuple1))
print("Tuple is",tuple1)

tuple2=([7,8,9],[10,11,12])
print("List to array is ",np.asarray(list1))
#asarray=Convert the input to an array
#returns->ndarray
print(type(np.asarray(list1)))

print("Tuple to array is ",np.asarray(tuple1))
print(type(np.asarray(tuple1)))


print("Tuple to 2Darray is ")
print(np.asarray(tuple2))


