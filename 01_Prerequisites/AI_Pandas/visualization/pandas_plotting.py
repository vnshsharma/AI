import pandas as pd 
import matplotlib.pyplot as plt 
data  = {
    'Name': ['Shaktimaan','Naagraaj','Bhokal'],
    'Age': [20,30,40],
}
df = pd.DataFrame(data)

# Plot a bar chart
df.plot(x='Name',y='Age',kind='bar',color='skyblue')
plt.title("Name vs Age")
plt.ylabel("Age")
plt.tight_layout()
plt.show()