import pandas as pd
data = {
    'Age': [20,30,40],
    'Power': [89,91,87]
}
df = pd.DataFrame(data) 
# Min-Max normalization
normalized_df = (df-df.min())/(df.max()-df.min())
print("Normalized Data: \n",normalized_df)