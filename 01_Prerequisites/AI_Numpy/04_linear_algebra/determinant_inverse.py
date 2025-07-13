import numpy as np 

matrix = np.array([[4,7,2],[3,6,1],[2,5,3]])

# Calculate Determinant 
det = np.linalg.det(matrix)
print("Determinant: ",det)

# Check if matrix is invertible (det!=0)
if det != 0:
    inverse = np.linalg.inv(matrix)
    print("Inverse: \n",inverse)
else:
    print("Matrix is singular, no inverse exists.")