# Data Preprocessing

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1:].values

#dataset.isnull().values.any()

from sklearn.linear_model import LinearRegression
regressior = LinearRegression()
regressior.fit(X, y)

y_pred = regressior.predict(np.array([[6.5]]))

#Plotting train data
%matplotlib auto
plt.scatter(X, y, color = "Blue", marker = "x")
plt.plot(X, regressior.predict(X), color = "Red")
plt.xlabel('Years Experience')
plt.ylabel("Salary")
plt.title("Salary vs years of Experience on Train Data")
plt.show()

from sklearn.preprocessing import PolynomialFeatures 
poly_reg = PolynomialFeatures(degree = 3)
ploy_X = poly_reg.fit_transform(X)

poly_regressior = LinearRegression()
poly_regressior.fit(ploy_X, y)

%matplotlib auto
plt.scatter(X, y, color = "Blue", marker = "x")
plt.plot(X, poly_regressior.predict(ploy_X), color = "Red")
plt.xlabel('Years Experience')
plt.ylabel("Salary")
plt.title("Salary vs years of Experience on Train Data")
plt.show()

