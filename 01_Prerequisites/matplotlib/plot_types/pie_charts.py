import matplotlib.pyplot as plt 

sizes = [25, 35, 20, 20]
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']
colors = ['red', 'yellow', 'pink', 'brown']

plt.pie(sizes, labels=labels, colors=colors)
plt.title("Pie Chart Example")
plt.show()