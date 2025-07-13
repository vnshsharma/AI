'''
Flatten means converting a multi-dimensional array into a single 1D array.
For example:
[[1, 2],
[3, 4]]
becomes [1, 2, 3, 4]
'''

import numpy as np 
matrix = np.array([[1,2],[3,4]])
print("Original Matrix: \n", matrix)

# Flatten the matrix to a 1D array using flatten() function
flattened = matrix.flatten()
print("Flattened Array: \n",flattened)