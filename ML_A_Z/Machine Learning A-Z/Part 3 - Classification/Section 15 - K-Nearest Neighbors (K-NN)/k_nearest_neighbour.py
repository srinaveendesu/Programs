# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 23:01:47 2018

@author: sd186076
"""

#import modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import the data set
dataset = pd.read_csv('Social_Network_Ads.csv')
x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,4].values

#splitting the dataset into training set and test set
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0 )

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
sc_fit_x = sc_x.fit(x_train)
x_train = sc_fit_x.transform(x_train)
x_test = sc_fit_x.transform(x_test)

#fitting the classifier to training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p =2, metric = 'minkowski')
classifier.fit(x_train, y_train)

#predicting from training set
y_pred = classifier.predict(x_test)

#making the confusion matric
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)

#visualising the training set
from matplotlib.colors import ListedColormap
x_set, y_set = x_train, y_train
x1, x2 = np.meshgrid(np.arange(start= x_set[:,0].min() -1, stop = x_set[:,0].max() +1, step = 0.01),
                     np.arange(start= x_set[:,1].min() -1, stop = x_set[:,1].max() +1, step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape),alpha= 0.75, cmap = ListedColormap(('red', 'green')) )
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j )
plt.title('Knn [training set]')
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()
    

#visualising the training set
from matplotlib.colors import ListedColormap
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start= x_set[:,0].min() -1, stop = x_set[:,0].max() +1, step = 0.01),
                     np.arange(start= x_set[:,1].min() -1, stop = x_set[:,1].max() +1, step = 0.01))
plt.contourf(x1, x2, classifier.predict(np.array([x1.ravel(),x2.ravel()]).T).reshape(x1.shape)
        ,alpha= 0.75, cmap = ListedColormap(('yellow', 'green')) )
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j )
plt.title('Knn [training set]')
plt.xlabel('age')
plt.ylabel('salary')
plt.legend()
plt.show()