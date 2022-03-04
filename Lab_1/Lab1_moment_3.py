# -*- coding: utf-8 -*-

"""
Eftersom π är ett irrationellt tal är 
det omöjligt att hitta den närmaste rationella 
approximationen, även om vi kan vara väldigt,
väldigt oerhört noggranna, men aldrig exakta.
   --------------------------------------
Pi = 3.1415926535897932384...
"""
 
import matplotlib.pyplot as plt
import numpy as np
from fractions import *
from math import *

from zmq import NULL

def pie_Approximation():
    best_diff = np.abs( (355/113) - np.pi )
    less_values={}
    
    for d in range(1, 100000):
        
        nf = int(np.floor(np.pi * d)) #nf = p, #d = q
        nc = int(np.ceil(np.pi * d))  #nc = p, #d = q
        
        nf_diff = np.abs(nf / d - np.pi)
        nc_diff = np.abs(nc / d - np.pi)
        
        if nf_diff < best_diff:
            best_diff = nf_diff
            #print('{} / {}: {:.2e}'.format(nf, d, best_diff))
            less_values.update({nf:d}) #Python update() method updates the dictionary with the key and value pairs. It inserts key/value if it is not present. It updates key/value if it is already present in the dictionary.
        
        elif nc_diff < best_diff:
            best_diff = nc_diff
            ##print('{} / {}: {:.2e}'.format(nc, d, best_diff))
            less_values.update({nc:d})
            
    new_key = less_values.keys()
    minim_k = min(new_key)
    #print("minim_k, min value: ",minim_k,less_values[minim_k])
    the_valid_one= np.abs((minim_k/less_values[minim_k])-np.pi)
    
    print('{} / {} has less- Error/Difference = : {:.2e}'.format(minim_k, less_values[minim_k],the_valid_one) )

pie_Approximation()


        
"""
7/ 2 = 3.5 [ 0]

10/ 3 = 3.33 [ 0]

13/ 4 = 3.25 [ 0]

16/ 5 = 3.20 [ 1]

19/ 6 = 3.16 [ 1]

22/ 7 = 3.142 [ 2]

179/ 57 = 3.140 [ 2]

201/ 64 = 3.1406 [ 3]

...

311/ 99 = 3.1414 [ 3]

333/ 106 = 3.14150 [ 4]

==>  355/ 113 = 3.1415929 [ 6]  <==

52163/ 16604 = 3.1415923 [ 6]

52518/ 16717 = 3.1415923 [ 6]

...
"""


class Approxamations:
    def __init__(self,_frac,id):
        
        self.numerator = (_frac.numerator)
        self.denominator = (_frac.denominator)
        self.brak = np.absolute((_frac.numerator/_frac.denominator)- np.pi)
        self.counter = id
        
    def getNumerator(self):
        return self.numerator
    def getDenominator(self):
        return self.denominator
    def getBrak(self):
        return self.brak
    def getCounter(self):
        return self.counter
    
class Collection_Approxamations:
    def __init__(self):
        self.items = []
        
    def add_Item(self,newTerm):
        self.items.append(newTerm)
        
    def get_Item(self,id):
        tal = 0
        for i in self.items:
            left_side = np.absolute((i.getNumerator()/i.getDenominator())- np.pi)
            right_side = np.absolute((355/113)-np.pi)
            
            if left_side < right_side :
                #tal = i.getBrak() 
                #print("|(p/q)-π| = ",i.getBrak())
                tal =(f"p/q => {i.getNumerator()} / {i.getDenominator()}")
                #print(f"p = {i.getNumerator()} , q = {i.getDenominator()}") 
                #print(f"{i.getCounter()}") 

        return tal


#using a 64-bit numerator and denominator
def approximation_pi_fraction():
    #[a_0; a_1, a_2, a_3, ...] = [3; 7, 15, 1, 292, ...].
    digits = [3, 7, 15, 1, 292, 1, 1, 1]
    #digits = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, 1, 1, 2, 2, 2, 2, 1, 84, 2, 1, 1, 15, 3, 13, 1, 4, 2, 6, 6, 99, 1, 2, 2, 6, 3, 5, 1, 1, 6, 8, 1, 7, 1, 2, 3, 7, 1, 2, 1, 1, 12, 1, 1, 1, 3, 1, 1, 8, 1, 1, 2, 1, 6, 1, 1, 5, 2, 2, 3, 1, 2, 4, 4, 16, 1, 161]
    counter = 0
    for i in range(len(digits)):
        
        #Börja med den sista siffran
        f = Fraction(digits[i]);  
        
        #Fortsätt att skriva om det som term + 1 / föregående
        #range(start, stop, step)
        for j in range(i-1, -1, -1):
            f = digits[j] + 1 / f
        #Sluta om vi skjuter förbi
        #if f.numerator >= 2**64 or f.denominator >= 2**64: break
    
        # Print the approximation we found
        #print(f)
        counter +=1
        
        #create an object to the class to access the methods etc...
        appCollection = Collection_Approxamations()
        appCollection.add_Item(Approxamations(f,counter))
                
        #the index of the fraction in the list
        if counter<6 and counter > 4:
            print(appCollection.get_Item(counter) )      
#approximation_pi_fraction()  