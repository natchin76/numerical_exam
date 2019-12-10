#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:12:41 2019

@author: chintan
"""
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import romberg
ld=1.5
n0=10
def dt(n):        #taking dt on RHS,LHS will be the function to be integrated
    return(-1/(ld*n))
def t(n):
    return(romberg(dt,n0,n))       #integrating lhs from n0 to n
number=np.arange(n0,.1,-.01)
time=np.empty(len(number))
for i in range(len(number)):
    time[i]=t(number[i])           #writing t as a function of n
plt.plot(time,number)    
plt.title('decay')
plt.xlabel('time(s)')
plt.ylabel('number')
plt.show()
