#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:36:26 2019

@author: chintan
"""
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline
from scipy.optimize import newton
from matplotlib import pyplot as plt
fname='data_5.txt'
a=np.loadtxt(fname,skiprows=5,usecols=(0,1))
th=a[0:len(a),0]
d=a[0:len(a),1]
df=InterpolatedUnivariateSpline(th,d,k=3)    #cubic spline(interpolation function)
thf=np.arange(0,10,.01)
plt.plot(thf,df(thf),label='interpolated function')
plt.scatter(th,d,label='data')
plt.title('d vs theta')
plt.legend()
plt.xlabel('theta')
plt.ylabel('d')
plt.show()
#root finding(Secant method)
def f(x):
    return(df(x)-370.4)
root=newton(f,.7)   #started the iteration with 0.7 as starting point
print(root)
 
    
