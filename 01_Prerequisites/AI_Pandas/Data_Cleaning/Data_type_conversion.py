import pandas as pd 
data = {
    'Name': ['Vansh','Sam','Harry'],
    'Age': ['19','20','21'],
    'Marks': [85.5,90.0,88.5]
}
df = pd.DataFrame(data)
print(df)
# Type of dataframe 
print(df.dtypes)


# ========== Convert age column into integer ===========
df['Age'] = df['Age'].astype(int)

print('Dataframe after data type conversion')
print(df)
# Also check the type of that converted dataframe
print(f'The type of this dataframe is {df.dtypes}') 