import pandas as pd
data = {
    'Name': ['Sam','Harry','Simran'],
    'Age': [20,21,23],
    'Score': [88,92,91]
}
df = pd.DataFrame(data)

X = df[['Age']]     # Features 
Y = df['Score']   # Target
print("Age: \n",X)
print("Score: \n",Y)