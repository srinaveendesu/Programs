# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 20:29:32 2018

@author: sd186076
"""

#import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import the dataset
dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:,[3, 4]].values

#Using the Dendogram to find the optimum no. of clusters
import scipy.cluster.hierarchy as sch
dendogram = sch.dendrogram(sch.linkage(x, method= 'ward'))
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Euclidian distance')
plt.show()

#fitting hierarichial clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters=5, affinity= 'euclidean', linkage= 'ward')
y_hc = hc.fit_predict(x)

#Visualising the clusters
plt.scatter(x[y_hc==0, 0], x[y_hc==0, 1], s=100, c = 'red', label='careful 1' )
plt.scatter(x[y_hc==1, 0], x[y_hc==1, 1], s=100, c = 'blue', label='standard' )
plt.scatter(x[y_hc==2, 0], x[y_hc==2, 1], s=100, c = 'green', label='target' )
plt.scatter(x[y_hc==3, 0], x[y_hc==3, 1], s=100, c = 'cyan', label='careless' )
plt.scatter(x[y_hc==4, 0], x[y_hc==4, 1], s=100, c = 'magenta', label='sensible' )
plt.title('Clusters of clients')
plt.xlabel('Annual income')
plt.ylabel('Spending score')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()