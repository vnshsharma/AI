import pandas as pd 

# Create a simple DataFrame 
data = {
    'Name': ['Naagraj','shaktimaan','Bhokal'],
    'Age': [45,46,47],
    'City': ['California','London','Laxmi Nagar']
}
df = pd.DataFrame(data)
print(df)

# Add a new coulumn 'Occupation'
df['Language'] = ['Python','JavaScript','C++']
print(df)

# Remove age column from this dataframe with axis=1 to specify column removal
df = df.drop('Age',axis=1)
print(df)