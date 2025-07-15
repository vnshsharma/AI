import pandas as pd
data = {
    'Name': ['Shaktimaan','Naagraj','Bhokal'],
    'Age': [21,22,23],
    'Marks': [85,90,88]
}
df = pd.DataFrame(data)
print(df)

# Sort by 'Marks in descending order
print('Sorted by Marks (Descending)')
print(df.sort_values(by='Marks',ascending=False))

# Filter student with marks greater than 85
print('Students with marks > 85')
print(df[df['Marks']>85])