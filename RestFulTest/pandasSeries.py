# Creating a pandas series

import pandas as pd
import numpy as np

labels = ['A', 'B', 'C', 'D']
my_list = [1, 2, 3, 4]
arr = np.array(my_list)
d = {'a': 10, 'b': 'Varinder', 'c': 30}

# Creating series using list with default indexing

s1 = pd.Series(data=my_list)
print("================= Default Indexing : Series ===================")
print(s1)

# Creating series using list with user-defined indexing

s2 = pd.Series(data=my_list, index=labels)
print("================= Defined Indexing : Series ===================")
print(s2)

# Creating series using NumPy arrays

s3 = pd.Series(data=arr)
print("================= NumPy Arrays : Series ===================")
print(s3)

# Creating series using Dictionary

s4 = pd.Series(data=d)
print("================= Dictionary : Series ===================")
print(s4)

# Creating seried using functions as data

s5 = pd.Series([len, sum])
print("================= Python Functions : Series ===================")
print(s5)

# Hands on Indexing

ser1 = pd.Series([1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
print("================= Labelling : Series ===================")
print(ser1)

print("Value for Germany : {}".format(ser1['Germany']))