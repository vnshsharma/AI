import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0,10,100)
y1 = np.sin(x)
y2 = np.sin(x+1)
y3 = np.sin(x+2)

plt.subplot(3,1,1)
plt.plot(x,y1,label='sin(x)')
plt.grid()
plt.legend()

plt.subplot(3,1,2)
plt.plot(x,y2,label='sin(x+1)',color='orange')
plt.grid()
plt.legend()

plt.subplot(3,1,3)
plt.plot(x,y3,label='sin(x+3)',color='green')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show() 