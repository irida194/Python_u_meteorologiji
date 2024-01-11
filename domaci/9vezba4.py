import numpy as np
import matplotlib.pyplot as plt

def potential_temperature(T, P, P0=1000, R=287.05, cp=1004):
    """
    Calculate potential temperature.

    Parameters:
    - T (numpy array): u kelvinima
    - P (numpy array): Ppritisak u mb
    - P0 (float, optional): 1000mb
    - R (float, optional): Specific gas constant for dry air (default is 287.05 J/(kg·K)).
    - cp (float, optional): Specific heat at constant pressure for dry air (default is 1004 J/(kg·K)).

    Returns:
    - numpy array: Potential temperature profile.
    """
    theta = T * (P0 / P) ** (R / cp)
    return theta

def pritisak(z):
    ro0=1.2 #kg/m3
    p0=101325 #Pa
    g=9.81 #m/s2
    p=p0*np.exp(-(ro0*g*z)/p0)
    return p

# altituda troposfera od 0 do 10km
alt = np.linspace(0, 10, 100)
tsfc = 288  #kelvin
grad =6.5 #grad in Kelvin per km
temp_profile = tsfc - grad * alt
#print(temperature_profile)


pressure_profile=pritisak(alt*1000)/100
potential_temperature_profile = potential_temperature(temp_profile, pressure_profile)


plt.subplot(2, 1, 1)
plt.plot(potential_temperature_profile, alt, color='blue', label='Potential Temperature')
plt.xlabel('Potential Temperature (K)')
plt.ylabel('Altitude (km)')
plt.title('Potential Temperature Profile in the Troposphere')
plt.legend()
plt.grid(True)


plt.subplot(2,1,2)
plt.plot(pressure_profile, alt, color='black',label='Promena pritiska sa visinom')
plt.xlabel('pritisak')
plt.ylabel('Visina(km)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
