#Clausius-Clapeyron equation
import math
import matplotlib.pyplot as plt

def es_f(L,t):
    e0 = 6.113 # mb
    Rv = 461 #J/K*KG
    t0 = 273.15 #k
    x = (L/Rv)* ((1/t0) - (1/t))
    es = e0 * math.exp(x)
    return es

#Latent heat of evaporation for water
Lw = 2.5 * math.pow(10,6) #J/KG
# #Latent heat of evaporation for ice
Ld = 2.83 * math.pow(10,6)
"""Koriste se negativne temp jer se voda moze naci na jako niskim temp
prehladjena voda.. Pokazuje se da Berzenovo pravilo da se kristal leda hrani isparavenjem kapljice"""
#staviti sto veci broj u posl argumentu linespace, da bi korak temp bio sto manji i precizniji rez na y osi

my_t=[223.15]
for i in range(60):
    t = 223.15+(i+1)
    my_t.append(t)
print(my_t)

#KELVIN mora da udje u formulu!
my_es_w = [es_f(Lw, t) for t in my_t]
my_es_d = [es_f(Ld, t) for t in my_t]

#crtam temp u C

my_tc=[t-273.16 for t in my_t]
plt.plot(my_tc, my_es_w, label = 'Zasicenje iznad prehladjene vode', color = 'blue')
plt.plot(my_tc, my_es_d, label = 'Zasicenje iznad leda', color = 'purple')
plt.legend()
plt.xlabel('T [$^\circ$C]')
plt.ylabel('es [mb]')