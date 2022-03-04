# -*- coding: utf-8 -*-

"""
    Skriv en Pythonfunktion som räknar ut antalet sekvenser av längd ett,
    antalet sekvenser av längd två etc.
    Ex: tal = [1, 2, 2, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 1, 7, 9] har fyra sekvenser
    av längd ett, en av längd två, två av längd tre och en av längd fyra.
    Det skall räcka att anropa funktionen en gång för att få ut alla resultat.
    Man anropar lämpligen funktionen från ett huvudprogram som sköter utskrifter
    och liknande.
"""
import numpy as np 

pie5 = np.load('pi5.npy')

tal = np.array([6,1, 2, 2, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 1, 7, 9])

def antalet_sekvenser(arr):
    lgd = 1
    count = {} #dictionary
    
    for k,v in enumerate(arr):
        if k == len(arr)-1:
            if str(lgd) in count:
                   count[str(lgd)] += 1 
            else:
                count[str(lgd)] = 1 
            break
        elif v == arr[k+1]: 
            lgd += 1 
        else:
            if str(lgd) in count:
                count[str(lgd)] += 1
            else:
                count[str(lgd)] = 1
            lgd = 1
        
    return count    

print(antalet_sekvenser(pie5))
#print(antalet_sekvenser(tal) )

#################################################################


