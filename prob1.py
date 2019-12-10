import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import romberg #using gauss quadrature technique
rho=10
def dm(r):                               #differential mass function definition
	return(rho*4*np.pi*r**2)
def m(r):
	return(romberg(dm,0,r))
rl=np.arange(0,10,.01)
ml=np.empty(len(rl))
for i in range(len(rl)):
    ml[i]=m(rl[i])
plt.plot(rl,ml)
plt.title('Mass as a function of distance from center')
plt.xlabel('r(m)')
plt.ylabel('M(r)(kg)')
plt.show()

