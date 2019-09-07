import pandas as pd
import numpy as np
from numpy.random import randn

df = pd.DataFrame(randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print("================= DataFrame with indexing and columns ======================")
print(df)
print("================ Indexing ==========")
print(df[['X', 'Z']])

# Adding a  new column using existing columns

df['NEW'] = df['X'] + df['Y']

print("====== New DF with DF[NEW]========")
print(df)

# Dropping coulmn

df.drop('NEW', axis=1, inplace=True)
print("====== Dropping DF[NEW]========")
print(df)

# Selecting a row with all columns

print("============ Selecting a row ==========")
print(df.loc['C'])

# Selecting a row with all columns
print("============ Selecting a row with indexed==========")
print(df.iloc[2])

################## Conditional seletion #######################

print("============ Conditional Selection ================")
print(df > 0)

print("============ More Index Details ============")
temp = df.reset_index()
print(temp)

############### Multiple indexes ###########################

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside,inside))
print("=============== Hierarchial indexes ======================")
print(hier_index)
hier_index = pd.MultiIndex.from_tuples(hier_index)
print(hier_index)