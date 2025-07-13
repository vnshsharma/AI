import numpy as np 
matrix = np.array([[5,-2],[2,3]])
eigen_values,eigen_vector = np.linalg.eig(matrix)
print("Eigen Values: ",eigen_values)
print("Eigen Vector: \n",eigen_vector)