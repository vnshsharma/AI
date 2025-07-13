import pandas as pd

# Create DataFrame from a dictionary
data = {
    'Name': ['Vansh', 'Siddharth', 'Aryan', 'Kunal'],
    'Age': [20, 21, 19, 22],
    'City': ['Delhi', 'Mumbai', 'Jaipur', 'Lucknow']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Check basic properties
print("\nDataFrame Shape:", df.shape)
print("\nDataFrame Info:")
print(df.info())
print("\nDataFrame Describe:")
print(df.describe(include='all'))
