import pandas as pd

data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

df = pd.DataFrame(data)

print(df)

print("========= DF with groupBY=============")
temp_df = df.groupby('Company')
print(temp_df.mean())
print("========= Standard Deviation =========")
print(temp_df.std())
