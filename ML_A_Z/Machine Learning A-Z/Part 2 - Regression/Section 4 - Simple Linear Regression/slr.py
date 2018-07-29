# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:46:48 2018

@author: sd186076
"""

#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importing the data set
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values

#splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y,  test_size=1/3, random_state =0)

#fitting simple linear regression on training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

#Predicting the test set results
y_pred = regressor.predict(x_test)

#Visualising the Training set results
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience [Training set]')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()

#Visualising the Training set results
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience [Training set]')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()