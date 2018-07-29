# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:27:56 2018

@author: sd186076
"""

#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# improting the dataset
dataset = pd.read_csv('Mall_Customers.csv')
x = dataset.iloc[:,[3,4]].values

#using the elbow method to find the optimum number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init= 'k-means++', n_init = 10, max_iter =300 , random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title('THe elbow Method')
plt.xlabel('No. of Clusters')
plt.ylabel('WCSS')
plt.show()

#Applying Kmeans to the dataset
kmeans = KMeans(n_clusters = 5, init= 'k-means++', n_init = 10, max_iter =300 , random_state = 0)
y_kmeans = kmeans.fit_predict(x)

#Visualising the clusters
plt.scatter(x[y_kmeans==0, 0], x[y_kmeans==0, 1], s=100, c = 'red', label='careful 1' )
plt.scatter(x[y_kmeans==1, 0], x[y_kmeans==1, 1], s=100, c = 'blue', label='standard' )
plt.scatter(x[y_kmeans==2, 0], x[y_kmeans==2, 1], s=100, c = 'green', label='target' )
plt.scatter(x[y_kmeans==3, 0], x[y_kmeans==3, 1], s=100, c = 'cyan', label='careless' )
plt.scatter(x[y_kmeans==4, 0], x[y_kmeans==4, 1], s=100, c = 'magenta', label='sensible' )
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1], s=300, c = 'yellow', label='centroids')
plt.title('Clusters of clients')
plt.xlabel('Annual income')
plt.ylabel('Spending score')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()