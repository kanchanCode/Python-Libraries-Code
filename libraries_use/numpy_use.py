import numpy as np
#NumPy provides efficient storage(it takes relatively less memory to store data)
#It provides better ways handling data for processing
#It is fast
myarr= np.array([3,6,9,12])
print(type(myarr))
print(myarr)


myarr1= np.array([[3,6,9,12]],np.int8) #int type references read 
print(myarr1[0][1])
myarr1[0][1]=90 # to change the value 
print(myarr1) 


print(myarr1.shape)
#to get the array undrstanding
#(1,4) 1 row 4 columns
print(myarr1.dtype)
#to get datatype of array

#ARRAY CREATION METHOD
# from Python objects to array -> e.g above one is created with the help of lists
listarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(listarray)
print(listarray.dtype)
print(listarray.shape)
print(listarray.size)

dict_arr=print(np.array({34:'n',34:'m',67:'o'})) 
print(dict_arr)

#Intinsic numpy array creation obj(eg: arrange,ones,zeros etc)
zeros=np.zeros((2,5)) #create array and fills it with zero
print(zeros)
print(zeros.dtype)

rng=np.arange(45) #creates array for that range
print(rng)
print(rng.reshape(5,9)) #to reshape the array
print(rng.ravel())  #creates 1D array

lspace=np.linspace(1,12) #linear spaced array /Equal space
print(lspace)
lspace1=np.linspace(1,50,10) #linear spaced array /Equal space between 1 to 50 and 10 elements should be there in that array
print(lspace1)


emp=np.empty((4,6)) #empty array of 4X6 filled with random nums
print(emp)

emp_like=np.empty_like(lspace)#empty array of the size given (previous array)
print(emp_like)

ide=np.identity(12)
print(ide)

#reading array from disk(kisi aur file se )
#from raw bytesthrough the use of strings
#use of special libraries

#axis0= rows
#axis1=column
#1D array has axis 0 only

print(listarray.sum(axis=0))
print(listarray.sum(axis=1))

print(listarray.T) # to transpose rows-> column and columns->rows

for item in listarray.flat: # to print elements one by one
    print(item)

print("no. of dimensions",listarray.ndim) #no.of dimensions 

print(listarray.nbytes) #total bytes consumed by array elements

oneD_arr=np.array([1,3,4,5,66,9])
print(oneD_arr.argmax()) #index of max elements
print(oneD_arr.argmin()) #index of min elements
print(oneD_arr.argsort()) #sort the array and gives the index of sorted

#in 2D array
print(listarray)
print(listarray.argmax()) #converts to 1D and gives result
print(listarray.argmax(axis=0)) #teeno rows k max elements ka index return krega

print(listarray.argsort(axis=0)) #teeno rows ko sort krke index return krega
listarray2=np.array([[9,8,7],[6,5,4],[3,2,1]])

#adding two matrix
print(listarray+listarray2)
print(listarray*listarray2)

print(np.sqrt(listarray2)) #sqrt of each element
print(listarray2.sum())
print(listarray2.max())
print(listarray2.min())
print(np.where(listarray>5)) #to find elemts and returns tuple
print(np.count_nonzero(listarray2)) #gives count of non zero 
print(np.nonzero(listarray2)) #for each axis return tuple of index

import sys
py_ar=[0,9,7,5]
np_ar=np.array(py_ar)

print(sys.getsizeof(1)*len(py_ar)) #size of python array
print(np_ar.itemsize*np_ar.size) # size of numpy array