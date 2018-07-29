# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:17:16 2018

@author: sd186076
"""

#impporting the libraries
import pandas as pd
import numpy as no
import matplotlib.pyplot as plt

#importing the data set
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

#implementing UCB
import math
N = 10000
d = 10
number_of_selection = [0] * d
sum_of_rewards = [0] * d
ads_selected = []
total_reward = 0
for n in range(0, N):
    max_upper_bound = 0
    ad = 0
    for i in range(0,d):
        
        if number_of_selection[i]>0:
            avg_reward = sum_of_rewards[i] /  number_of_selection[i]
            delta_i = math.sqrt(3/2 * math.log(n+1) / number_of_selection[i])
            upper_bound = avg_reward + delta_i
        else:
            upper_bound = 1e400
        
        if max_upper_bound < upper_bound :
            max_upper_bound = upper_bound
            ad = i
            
    ads_selected.append(ad)
    number_of_selection[ad] = number_of_selection[ad] + 1
    reward = dataset.values[n, ad]
    sum_of_rewards[ad ] = sum_of_rewards[ad ] + reward
    total_reward = total_reward + reward
    
    
# Visualising the results
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()