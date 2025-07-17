import numpy as np 
import matplotlib.pyplot as plt 

data = np.random.randn(1000)

plt.hist(data,bins=30,color='orange',edgecolor='black')
plt.title('Histograms')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()