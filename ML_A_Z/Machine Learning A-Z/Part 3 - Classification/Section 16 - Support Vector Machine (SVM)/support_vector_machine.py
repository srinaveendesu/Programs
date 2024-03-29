# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:07:02 2018

@author: sd186076
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,4].values

#splitting the dataset into train and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc_fit_x = sc.fit(x_train)
x_train = sc_fit_x.transform(x_train)
x_test = sc_fit_x.transform(x_test)

#Fitting the SVm to data set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state= 0)
classifier.fit(x_train,y_train)

#predicting the result
y_pred = classifier.predict(x_test)

#making the confusion matrics
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

#Visualizing the training set
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start = x_set[:,0].min() -1, stop = x_set[:,0].max() +1 , step = 0.01),
                     np.arange(start = x_set[:,1].min() -1, stop = x_set[:,1].max() +1 , step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape), 
             alpha = 0.75,cmap = ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[ y_set==j , 0], x_set[ y_set == j, 1], c=ListedColormap(('red','green'))(i), label = j )
plt.title('SVM [training set]')
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()    

#Visualizing the test set
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start = x_set[:,0].min() -1, stop = x_set[:,0].max() +1 , step = 0.01),
                     np.arange(start = x_set[:,1].min() -1, stop = x_set[:,1].max() +1 , step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape), 
             alpha = 0.75,cmap = ListedColormap(('red','green')))
plt.xlim(x1.min(),x1.max())
plt.ylim(x2.min(),x2.max())
for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[ y_set==j , 0], x_set[ y_set == j, 1], c=ListedColormap(('red','green'))(i), label = j )
plt.title('SVM [test set]')
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()
    