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

"""
Vi tittar p ̊a tv ̊a p ̊a varande f ̈oljande tal vi−1, vi. Om vi−1 = vi  ̈ar de en del av en sekvens av
likandana siffror, om d ̈aremot vi−1 6= vi  ̈ar vi−1 sista siffran i en sekvens och vi  ̈ar f ̈orsta siffran
i en ny sekvens av likadana siffror.
Vi anv ̈ander variabeln lgd f ̈or att ber ̈akna l ̈angden av alla delsekvenser av likadana siffror, s ̊a
om vi−1 = vi  ̈okar vi lgd med 1. Om vi−1 6= vi har en ny delsekvens p ̊ab ̈orjats och vi l ̊ater lgd
bli 1.
"""
def langsta_sekvensen(arr):
    
    lgd = 1
    longest = 1
    element = 1
    
    if len(arr) == 0: 
        print("An empty array is not allowed!")
        return 0
    elif len(arr) == 1:
        print(f'Det blir en enda siffra: {arr[0]} ,och har {element} sekvens')
        return 0
    
    for i in np.arange(1,len(arr)): 

        if arr[i-1] == arr[i]:
            lgd = lgd + 1
        else:
            lgd = 1
            
        if lgd>longest:
            longest = lgd
            element= arr[i]
    
    print(f"Talet: {element} har {longest} sekvens")
   
langsta_sekvensen(v6)



