import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :4].values
y = dataset.iloc[:, -1:].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
xLabelEncoder = LabelEncoder()
X[:, 3] = xLabelEncoder.fit_transform(X[:, 3])

xOneHotEncoder = OneHotEncoder(categorical_features= [3])
X = xOneHotEncoder.fit_transform(X).toarray()

X = X[:, 1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .8, random_state = 0)


from sklearn.linear_model import LinearRegression
regressior = LinearRegression()
regressior.fit(X_train, y_train)

y_pred = regressior.predict(X_test)


# Backward Elimination
import statsmodels.formula.api as sm
X = np.append(arr = np.ones(shape = (50,1)).astype(int), values = X, axis = 1)
X_opt = X[:, [0, 1, 2, 3, 4, 5]] # optimized array
regressor_OLS = sm.OLS(endog = y, exog= X_opt).fit()
regressor_OLS.summary()

# We will continue eliminating column untill we found p_value>.05
X_opt = X[:, [0, 1, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog= X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog = y, exog= X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 5]]
regressor_OLS = sm.OLS(endog = y, exog= X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3]]  # finally the most optimal column is R&D
regressor_OLS = sm.OLS(endog = y, exog= X_opt).fit()
regressor_OLS.summary()


# predict values with optimal features
regressor_opt = LinearRegression()
regressor_opt.fit(X_train[:, 2:3], y_train)

y_pred_opt = regressor_opt.predict(X_test[:, 2:3])
