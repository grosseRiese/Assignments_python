# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from fractions import *
from math import *

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
                tal =(f"p/q => {i.getNumerator()} / {i.getDenominator()}")
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
        if f.numerator >= 2**64 or f.denominator >= 2**64: break
        counter +=1
        
        #create an object to the class to access the methods etc...
        appCollection = Collection_Approxamations()
        appCollection.add_Item(Approxamations(f,counter))
                
        #the index of the fraction in the list
        if counter<6 and counter > 4:
            print(appCollection.get_Item(counter) )
        
            
approximation_pi_fraction()