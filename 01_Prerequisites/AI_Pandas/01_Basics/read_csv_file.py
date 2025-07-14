import pandas as pd
file_path = ""

# Read the csv file into a Dataframe
df = pd.read_csv(file_path)

# Display the first 5 rows 
print(df.head())
print(" ")

# Get the shape of the dataframe
print("Shape of the Dataframe:",df.shape)
print(" ")

# List all the columns
# print("Columns in the DataFrame: ",df.columns.tolist())

# Show basic info about the DataFrame
print("Basic Information about the DataFrame")
print(df.info())