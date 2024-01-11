import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm


# Define grid parameters
x_min, x_max = 0, 2
y_min, y_max = 0, 1
nx, ny = 20, 20

# Create a rectangular grid using meshgrid
x = np.linspace(x_min, x_max, nx)
y = np.linspace(y_min, y_max, ny)
X, Y = np.meshgrid(x, y)

# Define velocity components (example: u = x, v = y)
u = np.sin(X)
v = np.sin(Y)
#print(x)

#izracunavanje parcijalnih izvoda pomocu np.gradient()
du_dx, du_dy = np.gradient(u, axis=(1, 0))  
#0 je gradijent po vrstama, 1 po kolonama, po defaultu je axis=(0,1)
#po defaultu bi bilo du_dy, du_dx=np.gradient(u)
dv_dx, dv_dy = np.gradient(v, axis=(1, 0))


# Calculate divergence
divergence = du_dx + dv_dy

# Plotting
plt.figure(figsize=(12, 6)) #Width, height in inches.

plt.subplot(1, 2, 1)
plt.quiver(X,Y,u,v)
plt.title('Velocity Field')


plt.subplot(1, 2, 2)
plt.pcolormesh(X,Y,divergence,cmap=cm.jet)
plt.colorbar(label='Divergence')
plt.title('Divergence of Velocity')

plt.tight_layout()
plt.show()