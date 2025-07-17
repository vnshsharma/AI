import matplotlib.pyplot as plt 
x = [1,2,3,4,5]
y = [5,7,6,8,7]

plt.plot(x,y,linestyle='--',color='red',marker='o')
plt.title('Custom Plot Styles')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.grid()
plt.show()