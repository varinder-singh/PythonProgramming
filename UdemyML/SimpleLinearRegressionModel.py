import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import Imputer, LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

################ Importing dataset
data_set = pd.read_csv('Salary_Data.csv')
X = data_set.iloc[:, :-1].values
y = data_set.iloc[:, 1].values


################ Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)


# ########### Scaling my data
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train)
# X_test = sc_X.transform(X_test)

print(X)
print("="*40)
print(y)
print("="*40)
print(X_train)

############################# Creating the object of Linear Regressor and fit the training set on it
reg = LinearRegression()
reg.fit(X_train, y_train)

# Prediction now
y_pred = reg.predict(X_test)

# Plotting now
plt.scatter(X_train, y_train, color = 'red')
