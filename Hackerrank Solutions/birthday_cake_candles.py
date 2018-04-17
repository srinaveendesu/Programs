#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]
height.sort()
h = height[-1]
count =0
for val in height :
    if val == h:
        count +=1

print (count)      
