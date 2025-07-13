import numpy as np 
matrix = np.array([[1,2,3],[4,5,6]])
# Shape of the array (rows,columns)
print("Shape of a matrix: ",matrix.shape)
# Total number of elements in the array 
print("Size of matrix: ",matrix.size)
#Number of dimensions (1D, 2D, 3D,...)
print("Number of Dimensions: ",matrix.ndim)
# Data type of array elements
print("Data type: ",matrix.dtype)
# Reshape the matrix to (3,2)
reshaped_matrix = matrix.reshape(3,2)
print("Reshaped Matrix (3X2):\n",reshaped_matrix)