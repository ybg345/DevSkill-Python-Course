# Data Preprocessing

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :1].values
y = dataset.iloc[:, -1:].values

#dataset.isnull().values.any()

# Splitting the data into test and train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .8, random_state = 0)


from sklearn.linear_model import LinearRegression
regressior = LinearRegression()
regressior.fit(X_train, y_train)


y_pred = regressior.predict(X_test)


#Plotting train data
%matplotlib auto
plt.scatter(X_train, y_train, color = "Blue", marker = "x")
plt.plot(X_train, regressior.predict(X_train), color = "Red")
plt.xlabel('Years Experience')
plt.ylabel("Salary")
plt.title("Salary vs years of Experience on Train Data")
plt.show()

%matplotlib auto
plt.scatter(X_test, y_test, color = "Green", marker = "o")
plt.plot(X_train, regressior.predict(X_train), color = "Red")
plt.xlabel('Years Experience')
plt.ylabel("Salary")
plt.title("Salary vs years of Experience on Test Data")
plt.show()



