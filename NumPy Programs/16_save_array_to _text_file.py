'''
@Author: Kanchan
@Date: 2021-12-31
@Last Modified by: Kanchan
@Last Modified time: 2021-12-31
@Title : Write a Python program to save a NumPy array to a text file.
'''
import numpy as np
array1=np.arange(1,11)
np.savetxt('16_file.out',array1,delimiter=',',header="Array1 is ",footer="End")
#numpy.savetxt(fname, X, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None) : This method is used to save an array to a text file.
'''
Parameters:
fname : If the filename ends in .gz, the file is automatically saved in compressed gzip format. loadtxt understands gzipped files transparently.
X : [1D or 2D array_like] Data to be saved to a text file.
fmt : A single format (%10.5f), a sequence of formats, or a multi-format string, e.g. ‘Iteration %d – %10.5f’, in which case delimiter is ignored.
delimiter : String or character separating columns.
newline : String or character separating lines.
header : String that will be written at the beginning of the file.
footer : String that will be written at the end of the file.
comments : String that will be prepended to the header and footer strings, to mark them as comments. Default: ‘# ‘, as expected by e.g. numpy.loadtxt.
encoding : Encoding used to encode the output file. Does not apply to output streams. 

'''
 