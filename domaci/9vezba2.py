import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Funkcija koja opisuje diferencijalnu jednačinu ravnoteže toplote
def promena_temperature(t, T, k, T_okoline):
    dTdt = -k * (T - T_okoline)
    return dTdt

# Početni uslovi
T_pocetna = 100.0       # početna temperatura tela
k = 1/60                 # koeficijent prenosa toplote
T_okoline = 25.0        # temperatura okoline

# Vreme na kojem želimo rešenje
t_span = (0,180) 
t_eval = np.linspace(t_span[0], t_span[1], 100)

# Poziv solve_ivp funkcije
solution = solve_ivp(fun=lambda t, T: promena_temperature(t, T, k, T_okoline),
                t_span=t_span,
                y0=[T_pocetna],
                t_eval=t_eval)

value=solution.y[0][solution.t==60]
print(value.dtype)
np.set_printoptions(precision=3,suppress=True) #postavljam na 3 decimalna mesta

# Prikaz rezultata
plt.plot(solution.t, solution.y[0])
plt.scatter(solution.t[solution.t==60],solution.y[0][solution.t==60],color='red')
plt.text(solution.t[solution.t==60]+2,solution.y[0][solution.t==60],f"{value}")
plt.xlabel('Vreme [s]')
plt.ylabel('Temperatura [C]')
plt.title('Modeliranje promene temperature tela u homogenom i stacionarnom gravitacionom polju okruzenim beskonacnim gasom')
plt.show()