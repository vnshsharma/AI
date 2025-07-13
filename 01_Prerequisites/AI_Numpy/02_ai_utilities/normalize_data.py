# Normalization is the process of scaling data values to a specific range, typically between 0 and 1.

'''
Because in AI and ML, when features (data values) have different scales — like one ranging from 1-1000 and another from 0-1 — it can confuse models, especially those based on distance (like KNN, SVM, Neural Networks).
So, we normalize them to bring everything to the same scale.
'''

import numpy as np 
data = np.array([10,20,30,40,50])
normalized = (data-np.min(data))/(np.max(data)-np.min(data))
print("Original Data ",data)
print("Normailzed Data ",normalized)