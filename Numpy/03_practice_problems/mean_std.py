import numpy as np 
actual = np.array([3,-0.5,2,7])
predicted = np.array([2.5,0.0,2,8])
mse = np.mean((actual-predicted)**2)

print("Mean Square Error is: ",mse)