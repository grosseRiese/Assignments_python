# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 23:24:18 2022

@author: omrdh
"""
import numpy as np 

class my_dictionary(dict): 
    # __init__ function 
    def __init__(self): 
        self = dict() 
        
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

tal = np.array([1, 2, 2, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 1, 7, 9])

def antalet_sekvenser(arr):
    dict_obj = my_dictionary() 
    count = {} #dictionary
    countNum = 0
    for i in np.arange(len(arr)):
    
    for i,(k,v) in enumerate(count.items()):#key, value loop
        print(f"Array har {v} sekvenser av längd {k}")
    #print(f"\n  {count} ")
    print(f"Longest: {000} ")
antalet_sekvenser(tal)