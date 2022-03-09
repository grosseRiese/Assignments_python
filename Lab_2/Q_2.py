# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:33:00 2022

@author: omrdh

Vi tittar pa tva pa varande foljande tal vi−1, vi. Om vi−1 = vi  ̈ar de en del av en sekvens av
likandana siffror, om daremot vi−1 6= vi ar vi−1 sista siffran i en sekvens och vi  ̈ar forsta siffran
i en ny sekvens av likadana siffror.
Vi anvander variabeln lgd for att berakna längden av alla delsekvenser av likadana siffror, sa
om vi−1 = vi  ̈okar vi lgd med 1. Om vi−1 6= vi har en ny delsekvens paborjats och vi later lgd
bli 1.
"""

import numpy as np 
pie5= np.load('pi5.npy')
e5= np.load('e5.npy')

# vektorlängd ett, dessutom finns inte alla siffror med
v1 = np.array([4]) 
# sekvensen avslutas med att vektorn "tar slut"                
v2 = np.array([1, 1, 1, 1, 1])  
# här avslutas sekvensen med annan siffra   
v3 = np.array([1, 1, 1, 1, 1, 2])  
# sekvenser av olika längder (med samma siffra), den längsta sekvensen kommer inte sist
v4 = np.array([2, 1, 1, 2, 3, 4, 1, 1, 1, 2, 2, 4,5,5,5,5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1])
v5 = np.array([2,1,1,9,3,4,1,9,9,9,9,9,9,5,5,1,1,1,9,1,5,5,1,1,1])
v6 = pie5
v7 = pie5[450099:453102]
v8 = pie5[710099:710108]
def langsta_sekvensen(arr):
  lgd = 1
    longest = [0 for ix in range(0,10)]
    stop_indices = [0 for ix in range(0,10)]
    start_indices = [0 for ix in range(0,10)]
    
    if len(arr) == 0: 
        print("An empty array is not allowed!")
        return 0
    elif len(arr) == 1:
        print("Just a single element, count the length yourself.")
        return 0
    
    for i in range(1,len(arr)): 

        if arr[i-1] == arr[i]:
            lgd = lgd + 1
            
        else:
            if lgd>longest[arr[i-1]]:
                longest[arr[i-1]] = lgd
                stop_indices[arr[i-1]] = i-1
                start_indices[arr[i-1]] = i-lgd    
            lgd = 1
            
    i = len(arr) - 1        
    if arr[i-1] != arr[i]:
        if longest[arr[i]] == 0:
            longest[arr[i]] = 1
            start_indices[arr[i]] = i
            stop_indices[arr[i]] = i
    else:
        if lgd>longest[arr[i-1]]:
                longest[arr[i-1]] = lgd
                stop_indices[arr[i-1]] = i-1
                start_indices[arr[i-1]] = i-lgd
    
    for d in range(0,10):
        print(f"Talet: {d} har en sekvens av längd {longest[d]} från {start_indices[d]} till {stop_indices[d]}")


langsta_sekvensen(v5)





"""
def longst_sekv(x):
    x = x.astype(int)
    lengths = np.zeros(10)
    indic = np.zeros(10,dtype=tuple)
    for i in range(10):
        indic[i] = (0,0)
    lengths[x[0]] +=1
    
    count = 1
    strt,end=0,0
    
"""


