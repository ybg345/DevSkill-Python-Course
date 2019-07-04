#importing Libreries
import pandas as pd
import numpy as np

# importing data
Dataset = pd.read_csv('Data.csv')
X = Dataset.iloc[:, :-1].values # we need to see the values in console by typing x
y = Dataset.iloc[:, -1:].values



# Handling missing values (preprocess data) -> If there is no null value then we need not to do imputer process
from sklearn.preprocessing import Imputer     # imputer is a class. Now we will make an object
imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)

# Now we need to first 'fit' data and then 'transform'
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
# =============================================================================
# Another way of fit and transform
# x[:, 1:3] = imputer.fit_transform(x[:, 1:3])
# =============================================================================



# Handling Catagorical Variable:
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# for label x
xLabelEncoder = LabelEncoder()
X[:, 0] = xLabelEncoder.fit_transform(X[:, 0])

xOneHotEncoder = OneHotEncoder(categorical_features= [0])
X = xOneHotEncoder.fit_transform(X).toarray()

# for label y
# x and y always must be in two dimensional
# we need not to think about output i.e y. Cause it is dependendent on output. 

yLabelEncoder = LabelEncoder()
y[:, 0] = yLabelEncoder.fit_transform(y[:, 0])


# In input (x), in 'country' column 0, 1, 2 denotes three catagory. 
# But among these three one column is the transpose of any of the two. So we 
# can ingore any of the three column. 
# this is called "Dummy variable trap" for two catagories.


# Splitting the data into test and train:
# it is done for testing performance
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = .8, random_state = 0)



# Feature Scaling
# This is done because of large Eucleadian distance among the rows and columns
# Scaling is done in background in most of the languages. 
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
X_train = sc_x.fit_transform(X_train)
# We only transform x_test because we alredy fit x_train. And since x_train
# and x_test are of same data type. 
X_test = sc_x.transform(X_test)








