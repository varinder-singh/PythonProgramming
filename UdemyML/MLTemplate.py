import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# use imputer for substituting missing or Null values with NaN
# Imputer is deprecated in version 0.2 use SimpleImputer instead
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split

################ Importing dataset
data_set = pd.read_csv('Data.csv')
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 3].values

######################### Missing data
# Imputer object created below used to substitute Null values in the data with the Mean value of the particular column
# Strategy can be a mean. median or most frequently occurring value in the column
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])



################ Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


########### Scaling my data
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


