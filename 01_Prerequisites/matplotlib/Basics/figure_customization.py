import matplotlib.pyplot as plt 

fig = plt.figure(figsize=(8,4),dpi=100)
ax = fig.add_subplot()

x = [0,1,2,3,4]
y = [0,1,4,9,16]

ax.plot(x,y,marker='s',color='green')
ax.set_title('Figure Customization')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid()

plt.show()