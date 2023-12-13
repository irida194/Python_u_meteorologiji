import math

# Define initial conditions
x = 0.0 # initial horizontal position
y = 0.0 # initial vertical position
vx = 10.0 # initial horizontal velocity
vy = 10.0 # initial vertical velocity
g = 9.8 # acceleration due to gravity

# Define time step and duration of simulation
dt = 0.01 # time step (in seconds)
tmax = 2.0 # duration of simulation (in seconds)
nsteps = int(tmax / dt) # number of time steps

# Define lists to store position and velocity at each time step
x_list = [x]
y_list = [y]
vx_list = [vx]
vy_list = [vy]

# Simulate motion using numerical integration
for i in range(nsteps):
    # Calculate new position and velocity using Euler's method
    x = x + vx*dt
    y = y + vy*dt
    vx = vx
    vy = vy - g*dt
    
    # Store new position and velocity in lists
    x_list.append(x)
    y_list.append(y)
    vx_list.append(vx)
    vy_list.append(vy)

# Plot the trajectory of the object
import matplotlib.pyplot as plt
plt.plot(x_list, y_list)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Projectile Motion')
plt.show()
