'''

Solve:
2x + y = 8  
3x + 4y = 18

'''
import numpy as np 

# Coefficient matrix
A = np.array([[2,1],
              [3,4]])

# Constant terms
B = np.array([8,18])

# Solve for variable
solution = np.linalg.solve(A,B)

print("Solution [x,y]: ",solution)