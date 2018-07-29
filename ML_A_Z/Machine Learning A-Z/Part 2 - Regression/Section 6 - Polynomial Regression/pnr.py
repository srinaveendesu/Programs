# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:18:47 2018

@author: sd186076
"""

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#loading the dataset

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

#fitting the linear regression to data set
from sklearn.linear_model  import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, Y)

#fitting the polynomial regression to data set
from sklearn.preprocessing  import PolynomialFeatures
poly_reg = PolynomialFeatures(degree =4)
x_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(x_poly, Y)

#Visualising the linear regression model
plt.scatter(X, Y, color = 'red')
plt.plot(X, lin_reg.predict(X), color= 'blue')
plt.title('Truth or bluff (linearRegressor)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()


#Visualising the ploynomial regression model
plt.scatter(X, Y, color = 'red')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)), color= 'blue')
plt.title('Truth or bluff (linearRegressor)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

#Visualising the ploynomial regression model (for higher resolution and smoother curves)
x_grid = np.arange(min(X), max(X), 0.1)
x_grid = x_grid.reshape((len(x_grid), 1))
plt.scatter(X, Y, color = 'red')
plt.plot(x_grid, lin_reg2.predict(poly_reg.fit_transform(x_grid)), color= 'blue')
plt.title('Truth or bluff (linearRegressor)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()


#prdicting a new result with linear regression
lin_reg.predict(6.5)

#prdicting a new result with polynomial regression
lin_reg2.predict(poly_reg.fit_transform(6.5))