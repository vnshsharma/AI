import pandas as pd
data = {
    'Name': ['Shaktimaan','Naagraj','Bhokal','Jaadu'],
    'Subject': ['Math','Science','Math','Science'],
    'Marks': [85,90,88,80]
}
df = pd.DataFrame(data)
print(df)

# Group by 'Name' and find average marks
print("Average Marks by Name: ")
print(df.groupby('Name')['Marks'].mean())

# Group by 'Subject' and find total marks
print('Total marks by subject')
print(df.groupby('Subject')['Marks'].sum())