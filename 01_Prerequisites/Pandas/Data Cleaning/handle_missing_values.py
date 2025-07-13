import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['Vansh', 'Siddharth', 'Aryan', 'Kunal'],
    'Age': [20, np.nan, 19, 22],
    'Marks': [85, 90, np.nan, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame with Missing Values:")
print(df)

# Fill missing values with a fixed value
df_filled = df.fillna(0)
print("\nDataFrame after fillna(0):")
print(df_filled)

# Drop rows with any missing value
df_dropped = df.dropna()
print("\nDataFrame after dropna():")
print(df_dropped)

# Fill missing values with the mean of the column
df_mean_filled = df.copy()
df_mean_filled['Age'].fillna(df['Age'].mean(), inplace=True)
df_mean_filled['Marks'].fillna(df['Marks'].mean(), inplace=True)

print("\nDataFrame after filling with column mean:")
print(df_mean_filled)
