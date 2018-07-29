# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 00:36:55 2018

@author: sd186076
"""

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_y = StandardScaler()
sc_x = sc_x.fit(X)
X = sc_x.transform(X)
sc_y = sc_y.fit(Y.reshape(-1,1))
Y = sc_y.transform(Y.reshape(-1,1))
#np.array(Y)

#fitting the svr to dataset
#creating the regressor
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, Y)

#predicting a new result 
y_pred = sc_y.inverse_transform(regressor.predict(sc_x.transform(np.array([[6.5]]))))

#Visualising the SVR result
plt.scatter(X, Y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('truth or bluff [SVR]')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Visualising the SVR result (for higher resolution and smoother curve)
x_grid = np.arange(min(X), max(X), 0.1)
x_grid = x_grid.reshape(len(x_grid), 1)
plt.scatter(X, Y, color = 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('truth or bluff [SVR]')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()