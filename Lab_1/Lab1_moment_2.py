# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 00:47:42 2022

@author: omrdh
"""

import numpy as np
import matplotlib.pyplot as plt


f = lambda x: (1-x**3)**(1/3)

def calculate_dx (a, b, n):
	return (b-a)/float(n)

def leftEndPoint_rektangelregel(a,b,f,n): 
    """ over-estimation """
    h = calculate_dx(a,b,n) 
    x = np.linspace(a,b-h,n) #x_left
    
    I = np.sum(h*f(x[0:n]) )
    print('vänster Integral = ', I)
      
    plt.subplot(2,2,1) # Skapa 4 fönster (2 rader och 2 kolumner) och aktivera första
    
    plt.title('Left Riemann Sum, N = {}'.format(n))
    plt.ylabel('h-värdena') # Text längs y-axeln
    plt.xlabel(' ')
    
    
    plt.plot(x,f(x), 'r',markersize=10)
    plt.bar(x,f(x),width = h ,color='pink',align='edge')
    
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='yellow', alpha = 0.3 )
      
leftEndPoint_rektangelregel(0,1,f,100)
    
def Hoger_rektangelregel(a,b,f,n): 
    """ under-estimation """
    h = calculate_dx(a,b,n)
    x = np.linspace(h,b,n) #x_right
   
    I = np.sum(h*f(x[0:n]))
    print('höger Integral = ', I)
    
    plt.subplot(2,2,2) # Aktivera andra fönstret
    
    plt.title('Right Riemann Sum, N = {}'.format(n))
    plt.xlabel(' ')
    
    plt.plot(x,f(x),'b',markersize=10)
    plt.bar(x,f(x),width =-h, color='green',align='edge')   # width = (b-a)/n = h = calculate_dx
    
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='red', alpha = 0.3 )
    
Hoger_rektangelregel(0,1,f,100)

def Mittpunkts_metoden(a,b,f,n):

    h = calculate_dx(a,b,n)
    x = np.linspace(h/2,b-h/2,n) #Domain from a to b
    
    I = np.sum(f(x) * h)
    print('Mittpunktsmetoden Integral = ', I)
    
    plt.subplot(2,2,3) # Aktivera andra fönstret
    plt.title('\n\n\n\n')
    plt.xlabel('Midpoint Riemann Sum, N = {}'.format(n))
    
    plt.plot(x,f(x),'y',markersize=10) # 'y':yellow
    plt.bar(x,f(x),width = h,color='teal',edgecolor='teal')
    
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='teal', alpha = 0.3 )
    
Mittpunkts_metoden(0,1,f,100)

def Trapezoidal(a,b,f,n):
    
    x = np.linspace(a,b,n+1) # N+1 points make N subintervals
    y = f(x)
    
    y_right = y[1:] # right endpoints array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1. ])
    y_left = y[:-1] # left endpoints array([0. , 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])
    
    dx = calculate_dx(a,b,n) 
    T = (dx/2) * np.sum(y_right + y_left)
    #return T
    print("Trapezoid area T: ", T)
    
    x = np.linspace(a,b,n)
    plt.subplot(2,2,4) # Aktivera andra fönstret
    plt.title('\n\n\n\n')
    plt.xlabel('Trapezoidal Riemann Sum, N = {}'.format(n))
    
    plt.plot(x,f(x),'y',markersize=10)
    plt.bar(x,f(x),width=dx,color='Orange',edgecolor='Orange')
    plt.axhline(color ='black')
    plt.fill_between(x, f(x),
                     where = [(x >= a) and (x <= b) for x in x],
                     color='teal', alpha = 0.3 )
    
Trapezoidal(0,1,f,100)
