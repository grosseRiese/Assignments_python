 # -*- coding: utf-8 -*-

from asyncio.windows_events import NULL
import matplotlib.pyplot as plt
import numpy as np
import math
from decimal import *

def e_Approximation():
    best_value = 1
    best_p_q_value = (NULL,NULL)
    for q in np.arange(1,100):
        p = round(q * np.e)
        if abs((p/q) - np.e) < best_value:
            best_value = abs(p/q-np.e)
            best_p_q_value = (p, q)
    print("(p,q)-par : ",best_p_q_value)
    print(f"The best value/Error/Difference .. : {best_value}")
e_Approximation()








"""
q = 7 p = 19
q = 71 p = 193
q = 536 p = 1457
q = 9545 p = 25946
q = 99990 p = 271801
q = 398959 p = 1084483
"""

""" 
# The first cast...
def exp_Approximation():   
    q = np.arange(1,10)
    p = np.round(q*np.e) 
    p/q
    # Titta på skillnaden mellan approximationerna och e.
    a = abs(p/q - np.e)
    print("A : ",a)
    # Den bästa kvoten ̈ar 19/7 = 2.71
    bastaKvot = p[6]/q[6]
    
    index_k = 0
    for k in range(1,100):
        isClosed = np.isclose(p[k]/q[k], np.e,rtol=0.008)   #atol=0.008
        if isClosed:                    #(k < 2.718 and k >= 2.70): 
            index_k = k
            print(f"\n\nThe index we looking for is: => {[index_k]}")
            #print(f"\n\nThe index we looking for is: => {[k]}") 
            
    print(f"Då paret är : {(p[index_k],q[index_k])}")
    print(f'bastaKvot p[{index_k}]/q[{index_k}]: {bastaKvot}')
    print(f'Där (e)-värdet = :( {np.e} )\n')
    
exp_Approximation()
"""