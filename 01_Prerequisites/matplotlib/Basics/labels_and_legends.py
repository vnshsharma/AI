import matplotlib.pyplot as plt 

x = [1,2,3,4,5]
y1 = [1,4,9,16,25]
y2 = [2,3,5,7,11]

plt.plot(x,y1,label='Squares')
plt.plot(x,y2,label='Prime')
plt.title('Labels and Legends')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid()
plt.show()