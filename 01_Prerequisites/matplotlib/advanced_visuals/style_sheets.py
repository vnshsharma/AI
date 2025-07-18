import matplotlib.pyplot as plt 

plt.style.use('ggplot')

x = [1,2,3,4]
y = [15,25,10,30]

plt.plot(x,y,marker='o')
plt.title('Styled Plot with ggplot')
plt.show() 