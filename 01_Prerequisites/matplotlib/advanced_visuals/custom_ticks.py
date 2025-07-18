import matplotlib.pyplot as plt 

x = [0,1,2,3,4]
y = [10,20,15,30,25]

plt.plot(x,y)
plt.title('Custom Ticks')

plt.xticks([0,1,2,3,4],['Zero','One','Two','Three','Four'])
plt.yticks([10,20,30],['Low','Medium','High'])

plt.show() 