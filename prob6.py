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
number=np.linspace(n0,4e-4,100)
time=np.empty(len(number))
for i in range(len(number)):
    time[i]=t(number[i])           #writing t as a function of n
ta=np.linspace(0,time[-1],20)
na=[]
for i in range(len(ta)):
    na.append(n0*np.exp(-ld*ta[i]))     #analytical values of n    
plt.plot(time,number,label='numerical integration values')
plt.scatter(ta,na,label='analytical values')    
plt.title('decay')
plt.xlabel('time(s)')
plt.ylabel('n(cm^-3)')
plt.legend()
plt.show()
