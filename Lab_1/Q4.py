 # -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
from decimal import *

def exp_Approximation():
    # Låt q = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    q = np.arange(1,10)
    # För varje q-värd e best ̈am det bästa värdet på p.
    p = np.round(q*np.e) # p=[3, 5, 8, 11, 14, 16, 19, 22, 24]
    # Kvoterna
    p/q
    # Titta på skillnaden mellan approximationerna och e.
    abs(p/q - np.e)
    # Den bästa kvoten ̈ar 19/7 = 2.71
    bastaKvot = p[6]/q[6]
    
    for k in range(0,9):
        isClosed = np.isclose(p[k]/q[k], np.e,atol=0.008)
        if isClosed:  
            print(f"\n\nThe index we looking for is: => {[k]}") 
    print(f"Then the pair is : {(p[6],q[6])}")
    print(f'bastaKvot p[6]/q[6]: {bastaKvot}')
    print(f'Där (e)-värdet = :( {np.e} )\n')
    
exp_Approximation()