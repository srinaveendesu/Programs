# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 02:30:48 2018

@author: sd186076
"""

#importing the data set
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:,1:2].values
Y = dataset.iloc[:,2].values

#fitting the RFR to dataset
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=300 , random_state =0)
regressor.fit(X, Y)

#predicting the new result
regressor.predict(6.5)

#plot the Regression (for higher resolution and smoother curve)
x_grid = np.arange(min(X), max(X), 0.01)
x_grid = x_grid.reshape((len(x_grid),1))
plt.scatter(X,Y, color= 'red')
plt.plot(x_grid, regressor.predict(x_grid), color = 'blue')
plt.title('truth vs bluff [Random forrest regression]')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show