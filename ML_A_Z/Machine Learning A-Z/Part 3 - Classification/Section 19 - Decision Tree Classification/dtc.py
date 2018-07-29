# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 16:42:09 2018

@author: sd186076
"""


#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:, 4].values

#splitting the dataset into train and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25 , random_state = 0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc_fit_x = sc.fit(x_train)
x_train = sc_fit_x.transform(x_train)
x_test = sc_fit_x.transform(x_test)

#Classifying the dataset
from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier( criterion = 'entropy' ,random_state=0)
classifier.fit(x_train , y_train)

#predicting the test results
y_pred = classifier.predict(x_test)

#Consufion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#visualising the training set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() -1, stop= x_set[:, 0].max() + 1,step=0.01),
                     np.arange(start = x_set[:, 1].min() -1, stop= x_set[:, 1].max() + 1,step=0.01))
plt.contourf(x1,x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha= 0.75 , cmap= ListedColormap(('red', 'green')))
plt.xlim(x1.min() -1, x1.max() + 1 )
plt.ylim(x2.min() -1, x2.max() + 1 )
for i, j in enumerate (np.unique(y_set)):
    plt.scatter(x_set[y_set==j, 0], x_set[y_set==j, 1], c=ListedColormap(('red', 'green'))(i), label=j)
plt.title('Decision Tree Classifier [training set]')
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()    

#visualising the test set results
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start = x_set[:, 0].min() -1, stop= x_set[:, 0].max() + 1,step=0.01),
                     np.arange(start = x_set[:, 1].min() -1, stop= x_set[:, 1].max() + 1,step=0.01))
plt.contourf(x1,x2, classifier.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
             alpha= 0.75 , cmap= ListedColormap(('red', 'green')))
plt.xlim(x1.min() -1, x1.max() + 1 )
plt.ylim(x2.min() -1, x2.max() + 1 )
for i, j in enumerate (np.unique(y_set)):
    plt.scatter(x_set[y_set==j, 0], x_set[y_set==j, 1], c=ListedColormap(('red', 'green'))(i), label=j)
plt.title('Decision Tree Classifier [test set]')
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()    