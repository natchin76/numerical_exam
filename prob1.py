import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import romberg #using gauss quadrature technique
rho=10
def dm(r):                               #differential mass function definition
	return(rho*4*np.pi*r**2)
def m(r):
	return(romberg(dm,0,r))     #integrate dm from 0 to r
rl=np.arange(0,10,.01)
ml=np.empty(len(rl))
for i in range(len(rl)):
    ml[i]=m(rl[i])
ra=np.linspace(0,10,20)
ma=[]
for i in range(len(ra)):
    ma.append(4/3*rho*np.pi*ra[i]**3)    #analytical values on selected points
plt.scatter(ra,ma,label='analytical values')    
plt.plot(rl,ml,label='integrated function')
plt.title('Mass as a function of distance from center')
plt.xlabel('r(m)')
plt.ylabel('M(r)(kg)')
plt.legend()
plt.show()

