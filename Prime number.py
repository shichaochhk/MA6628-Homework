# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:12:46 2018

@author: chao
"""

#A twin prime is a prime number that is either 2 less or 2 more than another prime number
#See for details here: https://en.wikipedia.org/wiki/Twin_prime.

import numpy as np

#Initialization
x=np.arange(1000000001,1000000010,2)
y=[]

#Define the function for iteration
def divident(x):
    counter=np.arange(3,x-1,2)
    #print(counter)
    for i in counter:
        #print(x)
        if x%i==0:
            return i
            break
    return 0

#Find out all the prime number within the given range
for counter in x:
    if divident(counter)>0:
        y.append(counter)

#Create twin prime number matrix
y1=np.insert(y,np.size(y),y[np.size(y)-1],axis=0)
y2=np.insert(y,0,y[0],axis=0)
yf=y1-y2
k=np.array([y2,y1])
k=k.T

#delete non twin prime pair
for i in range(np.size(yf)-1,-1,-1):
    if yf[i]!=2:
        #print("The number i equals to ",i)
        k=np.delete(k,[i],axis=0)
print("The total pair of twin prime number is ",np.size(k)/2)
print(k)