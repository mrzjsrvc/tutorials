from __future__ import print_function
import numpy as np

a = np.array([[6, 7, 8],[6, 7, 8],[6, 7, 8]])

print("SHAPE:", a.shape)             # Get length of each dimension of numpy matrix
print("DIMNS:", a.ndim)              # Get amount of dimensions of numpy matrix
print("DTYPE:", a.dtype.name)        # Get data type of matrix
print("\n",a)

a[2,1] = 10                          # Change one cell's value
print(a,"\n")
print(a[2],"\n")                     # Print third row
print(a[:,0],"\n")                   # Print first column

b = np.arange(15)                    # Makes array: 0,1,2,3,...13,14
print(b,"\n")
b = b.reshape(3,5)                   # Makes 5x3 matrix of the array: [[0,1,2,3,4], [5,6,7,8,9], [10,11,12,13,14]]
print(b)
