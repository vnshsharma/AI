import pandas as pd 
data = {
    'Name': ['Naagraaj','Shaktimaan','Jaadu'],
    'Age': [75,80,1002],
    'Marks': [20,30,100]
}
df = pd.DataFrame(data)
print(df)

# Remove duplicates rows

# drop_duplicates() → removes all rows that are completely identical.
df_no_duplicates = df.drop_duplicates()
print(df_no_duplicates)