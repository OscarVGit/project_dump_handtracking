import pandas as pd
import re

df = pd.read_csv('./Pokemon Dataset/pokemon_data.csv')

#df_xlxs = pd.read_excel('pokemon_data.xlxs')

df.columns

#Read each column
#print(df[['Name', 'Type 1', 'HP']])

#Read each row
#print(df.iloc[0:4])
#for index, row in df.iterrows():
#    print(index, row)

#print(df.loc[df['Type 1'] == "Fire"])

# Read a specific location (R, C)
#print(df.iloc[2,1])

# Sorting Describing data
df.sort_values(['Type 1', 'HP'],ascending=False)

# Making changes to the data
#df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

df['Total'] = df.iloc[:, 4:10].sum(axis=1)

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]]+cols[4:12]]

#print(df.head(5))

# Saving data into exportable format
#df.to_csv('modified.csv', index=False)

# Filtering data
#new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]

df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex = True)]

#new_df = new_df.reset_index(drop=True, inplace=True)

# Conditional changes, changes fire type to flamer type
df.loc[df['Type 1'] == 'Fire','Type 1'] = 'Flamer'

# Aggregate statistics

