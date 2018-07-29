# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:49:45 2018

@author: sd186076
"""

#Decision tree regression
# import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Getting the data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

#fitting the regressor
from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor(random_state = 0)
regressor.fit(X, Y)

#predicting a new result
y_pred = regressor.predict(6.5)

#Visualising the Decision tree results (for higher resolution and smoother curve)
x_grid = np.arange(min(X), max(X), 0.01)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color='blue')
plt.title('truth or bluff ( Decision tree)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()