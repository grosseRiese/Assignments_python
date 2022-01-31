# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 01:11:24 2022

@author: omrdh
"""


from numpy import load
pi5=load('pi5.npy')
e5=load('e5.npy')
print(pi5[0:31])

print(pi5[999999:1000005])  # siffror nummer 1000000 till och med 1000005

print(pi5[-5:])             # de fem sista siffrorna

print(e5[0:16] )                     # analogt för e

print(pi5[710099:710108])        # sju treor i rad