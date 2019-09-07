import pandas as pd


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                    index=['K0', 'K1', 'K2'])

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2']},
                     index=['K0', 'K1', 'K3'])

print("================Default join=================")
print(left.join(right))