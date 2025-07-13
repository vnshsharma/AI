import numpy as np 
# Actual Values
actual = np.array([3,-0.5,2,7])
# Predicted Values
predicted = np.array([2.5,0.0,2,8])
# Mean Squared Error Calculation
mse = np.mean((actual-predicted)**2)

print("Actual Values: ",actual)
print("Predicted Values: ",predicted)
print("Mean Square Error (MSE): ",mse)