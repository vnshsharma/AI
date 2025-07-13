import numpy as np 
data = np.array([[23,84,16],[45,12,55]])
normalized = (data-np.min(data))/(np.max(data)-np.min(data))
print("Normalized Matrix is:\n",normalized) 