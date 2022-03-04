from math import sqrt
import numpy as np
import struct
from sympy import * 

class MinQuaternion:
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
       
    def __str__(self):
        txt = '('+str(self.a)+','+str(self.b)+','+str(self.c)+','+str(self.d)+')'
        return txt
    #1
    
    def qadd(self,q1,q2):
        quaternionObj1 = Quaternion(q1.a,q1.b,q1.c,q1.d)
        quaternionObj2 = Quaternion(q2.a,q2.b,q2.c,q2.d)
        Q1tQ2 = quaternionObj1.add(quaternionObj2)
        return Q1tQ2
    #2
    def qsub(self,q1,q2):
        Q1_Q2 = Quaternion( (q1.a - q2.a) ,(q1.b - q2.b),(q1.c - q2.c),(q1.d - q2.d))
        return Q1_Q2 
    #3
    def qmul(self,q1,q2):
        
        quaternionObj1 = Quaternion(q1.a,q1.b,q1.c,q1.d)
        quaternionObj2 = Quaternion(q2.a,q2.b,q2.c,q2.d)
        Q1xQ2 = quaternionObj1.mul(quaternionObj2)
        return Q1xQ2
        """
        x0, y0, z0, w0 = np.split(q1, 4, axis=-1)
        x1, y1, z1, w1 = np.split(q2, 4, axis=-1)
        return np.concatenate(
        (x1*w0 + y1*z0 - z1*y0 + w1*x0,
         -x1*z0 + y1*w0 + z1*x0 + w1*y0,
         x1*y0 - y1*x0 + z1*w0 + w1*z0,
         -x1*x0 - y1*y0 - z1*z0 + w1*w0),
        axis=-1)
        """
    #4
    def qdiv(self,q1,q2):
        quaternionObj1 = Quaternion(q1.a,q1.b,q1.c,q1.d)
        quaternionObj2 = Quaternion(1/q2.a,1/q2.b,1/q2.c,1/q2.d)
        Q1_div_Q2 = quaternionObj1.mul(quaternionObj2)
        return Q1_div_Q2
    
    #5
    def qinv(self,q1):
        self.a = q1.a
        self.b = q1.b
        self.c = q1.c
        self.d = q1.d
        Q1_inv = Quaternion((self.a) - (self.b) - (self.c) -(self.d) ) /( (self.a)**2+(self.b)**2+(self.c)**2+(self.d)**2)
        return Q1_inv
    
        
    #6
    def qabs(self,q1):
        x = sqrt( ( (self.a)**2+(self.b)**2+(self.c)**2+(self.d)**2) * Quaternion((self.a) - (self.b) - (self.c) -(self.d) ) )
        return np.absolute(x)
        
     #7
    def qconj(self,q1):
        self.a = q1.a
        self.b = q1.b
        self.c = q1.c
        self.d = q1.d
        konjugation = Quaternion((self.a) - (self.b) - (self.c) -(self.d) ) 
        return konjugation
     #8
    def qcons(self,a,b,c,d):
        """self.a = q1.a
        self.b = q1.b
        self.c = q1.c
        self.d = q1.d"""
        qConstru = Quaternion(q1.a,q1.b,q1.c,q1.d)
        return qConstru
    #9
    def qread(self):
        q2 = MinQuaternion(-2,5,7,6) 
        self.qprint(q1,q2)
        
        
    #10
    def qprint(self,q1,q2):
        print(f"---------------------------------------")
        print(f"1-Add:\n {q1.qadd(q1,q2)} ")
        print(f"---------------------------------------")
        print(f"2-Subtraction:\n {q1.qsub(q1,q2)} ")
        print(f"---------------------------------------")
        print(f"3-Multiplication:\n {q1.qmul(q1,q2) } ")
        print(f"---------------------------------------")
        print(f"4-Divide:\n {q1.qdiv(q1,q2) } ")
        print(f"---------------------------------------")
        print(f"5-Inverse:\n {q1.qinv(q1)} ")
        print(f"---------------------------------------")
        print(f"6-Absloute:\n {q1.qabs(q1) } ")
        print(f"---------------------------------------")
        print(f"7-Konjugation:\n  {q1.qconj(q1) } ")
        print(f"---------------------------------------")
        print(f"8-Constructs:\n {q1.qcons(q1.a,q1.b,q1.c,q1.d) } ")
        print(f"---------------------------------------")
        
        
val1 = input("Please enter value :\n a =...")
        
val2 = input("Please enter value :\n b =...")
        
val3 = input("Please enter value :\n c =...")
        
val4 = input("Please enter value :\n d =...")
        
print(f" You entered ... Q1 = ({val1} ,{val2} ,{val3} ,{val4} )")
print(f"---------------------------------------")
print(f"---------------------------------------")
        
q1 = MinQuaternion(int(val1),int(val2),int(val3),int(val4)) 
q1.qread()
