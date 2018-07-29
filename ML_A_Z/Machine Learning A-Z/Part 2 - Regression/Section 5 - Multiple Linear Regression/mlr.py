# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 01:21:04 2018

@author: sd186076
"""

#Assumptions in a linear regression
#1. Linearity
#2. Homoscedasticity
#3. Multivariate normality
#4. Independence of errors
#5. Lack of multicollinearity
# Not considered in this course

#5 methoda of building models
#1. All-in
#2. Backward Elimination
#3. Forward Selection
#4. Bidirectional Elimination
#5. Score comparision

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing the data set
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,4].values


#ecoding to remove the categorical data 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_x = LabelEncoder()
X[:,3] = labelencoder_x.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the dummy variable trap
X = X[:, 1:]

#splitting the dataset in training set and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state= 0)

#fitting multiple linear regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

#predicting the Test set resutls
y_pred = regressor.predict(x_test)

#building the optimal modeul using backward elimination
import statsmodels.formula.api as sm
X = np.append(arr= np.ones((50,1)).astype(int), values =X, axis=1 )
x_opt = X[:, [0, 1, 2, 3, 4, 5]]
regressor_ols = sm.OLS(endog = Y, exog=x_opt).fit()
regressor_ols.summary()
x_opt = X[:, [0, 1, 3, 4, 5]]
regressor_ols = sm.OLS(endog = Y, exog=x_opt).fit()
regressor_ols.summary()
x_opt = X[:, [0, 3, 4, 5]]
regressor_ols = sm.OLS(endog = Y, exog=x_opt).fit()
regressor_ols.summary()
x_opt = X[:, [0, 3, 5]]
regressor_ols = sm.OLS(endog = Y, exog=x_opt).fit()
regressor_ols.summary()
x_opt = X[:, [0, 3]]
regressor_ols = sm.OLS(endog = Y, exog=x_opt).fit()
regressor_ols.summary()
