# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:12:20 2018

@author: sd186076
"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []

for i in range(0,7501):
    transactions.append([str(dataset.values[ i, j]) for j in range(0,20)])
    

#Training Apriori on the dataset
#min suppeort is . min 3 items purchased per day. for week = 3*7 /7500    
from apriori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence= 0.2, min_lift= 3, min_length =2)

#Visualising the results
results = list(rules)

for val in results:
    print (val)