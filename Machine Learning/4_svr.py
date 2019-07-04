# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 10:55:05 2018

@author: Mehedi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1:].values


from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
X = sc_x.fit_transform(X)
y = sc_y.fit_transform(y)

from sklearn.svm import SVR
sr_x = SVR(kernel = 'rbf')
sr_x.fit(X, y)

y_pred = sc_y.inverse_transform(sr_x.predict(sc_x.transform(np.array([[6.5]]))))

%matplotlib auto
plt.scatter(X, y, color = "Blue", marker = "x")
plt.plot(X, sr_x.predict(X), color= "Red")
plt.show()



