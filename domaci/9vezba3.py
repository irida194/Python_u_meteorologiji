import numpy as np
import matplotlib.pyplot as plt

def pritisak(z):
    ro0=1.2 #kg/m3
    p0=101325 #Pa
    g=9.81 #m/s2
    p=p0*np.exp(-(ro0*g*z)/p0)
    return p

z=np.linspace(0,10,11)
p=pritisak(z*1000)/100

plt.plot(z,p)
plt.grid()