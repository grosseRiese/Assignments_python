# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 23:24:18 2022

@author: omrdh
"""
import numpy as np 

tal = np.array([1, 2, 2, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 1, 7, 9])

def antalet_sekvenser(arr):
    
    count = {} #dictionary
    
    for i in arr: 
        if not i in count:
            count[i] = 0
        else:
            count[i] += 1
    
    for i,(k,v) in enumerate(count.items()):#key, value loop
        print(f"Array har {v} sekvenser av längd {k}")
    #print(f"\n  {count} ")
   
antalet_sekvenser(tal)