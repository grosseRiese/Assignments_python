# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 00:25:42 2022

@author: omrdh
"""
import numpy as np 
#from numpy import  load
from collections import Counter

pie5= np.load('pi5.npy')
e5= np.load('e5.npy')

def countX(lst):
    for x in range(0,10):
        d = Counter(lst)
        print('{} has occurred {} times'.format(x, d[x]))
    
countX(pie5) 
#countX(e5) 

#Set
def countOccurrences(arr):
    arr.sort() # Sort the List in Ascending Order
    occ_dict ={}
    for item in arr:
        if item not in occ_dict:
            occ_dict[item] = 1
        else:
            occ_dict[item] +=1
    for j in occ_dict:
        print(f" {int(j)} has occurred: {occ_dict[j]} times")
    #print(f"\n {occ_dict} \n")
#countOccurrences(e5)
countOccurrences(pie5)


