import numpy as np
import matplotlib.pyplot as plt

# mass, spring constant, initial position and velocity
m = 1
k = 1
x = 0
v = 1

# Creating first two data using Euler's method
t_max = 0.2
dt = 0.1
t_array = np.arange(0, t_max, dt)
x_list = []
v_list = []
for t in t_array:
    x_list.append(x)
    v_list.append(v)
    a = -k * x / m
    x = x + dt * v
    v = v + dt * a

# Verlet method    
t_max = 10
dt = 0.1
t_array = np.arange(0.2, t_max, dt)

# initialise empty lists to record trajectories
counter = 1
# Euler integration
for t in t_array:
    # append current state to trajectories
    # calculate new position and velocity
    a = -k * x / m
    x = 2*x_list[counter]-x_list[counter-1]+(dt**2)*a 
    v = (1/dt)*(x-x_list[counter])    
    x_list.append(x)
    v_list.append(v)
    counter +=1
# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_array = np.array(x_list)
v_array = np.array(v_list)


t_array_plot = np.arange(0, t_max, dt)
# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array_plot, x_array, label='x (m)')
plt.plot(t_array_plot, v_array, label='v (m/s)')
plt.legend()
plt.show()

