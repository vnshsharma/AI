import pandas as pd
data = {
    'Name': ['Naagraj','Shaktimaan','Bhokal'],
    'Age': [20,30,40],
    'Marks': [85,90,95]
}
df  = pd.DataFrame(data)

# Add new row in this dataframe 
new_row = {
    'Name': 'Supermaan',
    'Age': 19,
    'Marks': 100
}
df = pd.concat([df,pd.DataFrame([new_row])])
print(df)