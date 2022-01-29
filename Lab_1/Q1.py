# -*- coding: utf-8 -*-
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
        x = np.random.uniform(-r,r)
        y = np.random.uniform(-r,r)
        
        if np.sqrt(x**2 + y**2) <= (r):
            X_in.append(x)
            Y_in.append(y)
        else:
            X_out.append(x)
            Y_out.append(y)
    __pi =( 4 * len(X_in)/n)
    print(f'pi = {__pi}')
    
    plt.figure(figsize=(10,10))
    plt.xlim(-0.605,0.605)
    plt.ylim(-0.605,0.605)

    plt.plot(X_in,Y_in,'mo',markersize=10)
    plt.plot(X_out,Y_out,'co',markersize=10)
    
    plt.show()
method_Monte_Carlo()
    