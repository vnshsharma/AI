import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

data = {
    'Name': ['Naagraaj','Shaktimaan','Bhokal'],
    'Age': [20,30,40],
    'Power': [89,91,87]
}
df = pd.DataFrame(data)
sns.scatterplot(data=df,x='Power',y='Age',hue='Name',palette='Set2')
plt.title('Age vs Power')
plt.xlabel('Power')
plt.ylabel('Age')
plt.grid()
plt.tight_layout()
plt.show() 