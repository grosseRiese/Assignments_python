# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 00:05:00 2022

@author: omrdh
"""
import numpy as np
import matplotlib.pyplot as plt


    
def method_Monte_Carlo():
    r = 1/2     # radie (-1/2,1/2)
    n = 10000
    # Här används 4 listor för att visualisera sen.
    X_in=[]     # x-punkt in circel
    Y_in=[]     # Y-punkt in circel
    X_out=[]     # x-punkt out circel
    Y_out=[]     # Y-punkt out circel
    

    for _ in range(n):
        # random.uniform(low=0.0, high=1.0, size=None)
        x = np.random.uniform(-r,r)
        y = np.random.uniform(-r,r)
        #print("X: ",x)
        #print("Y: ",y)

        # Pythagoras sats i en rätvinklig triangel
        #c^2 = a^2 +b^2
        if np.sqrt(x**2 + y**2) <= (r):
            X_in.append(x)
            Y_in.append(y)
        else:
            X_out.append(x)
            Y_out.append(y)

            
        #print("X in circel:\n ", X_in)
        #print("Y in circel:\n ", Y_in)
        #print("\nX out circel:\n ", X_out)
        #print("Y out circel:\n ", Y_out)
    __pi =( 4 * len(X_in)/n)
    print(f'pi = {__pi}')
    
    #graph_Monte_Carlo(X_in,X_out,Y_in,Y_out)
    
    
    plt.figure(figsize=(10,10))
    plt.xlim(-0.605,0.605)
    plt.ylim(-0.605,0.605)

    plt.plot(X_in,Y_in,'mo',markersize=10)
    plt.plot(X_out,Y_out,'co',markersize=10)
    
    plt.show()
    
#for _ in range(8):
method_Monte_Carlo()
    



