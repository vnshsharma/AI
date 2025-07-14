import pandas as pd 
# ============== Creating from dictionary ==============
'''
data = {
    'Name': ['IronMan','Aamir','Hitler'],
    'Age': [18,19,20],
    'Country': ['USA','India','Germany']
}
# Convert dictionary into DataFrame
df = pd.DataFrame(data)
print(df)
'''

# ============== Create empty dataframe and then add rows ==============
'''
df = pd.DataFrame(columns=['Name','Age','Country'])
# Adding rows 
df.loc[0] = ['IronMan',18,'USA']
df.loc[1] = ['Hitler',20,'Germany']
print(df)
'''

# ============= Create from list to lists ===============
data = [['IronMan',18,'USA'],
        ['Hitler',20,'Germany']]
df = pd.DataFrame(data,columns=['Name','Age','Country'])
print(df)