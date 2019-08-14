import numpy as np
import matplotlib.pyplot as plt
import math

# mass, spring constant, initial position and velocity
Mars_radius = 3.39e6
x = np.array([0,0,Mars_radius+100])
v = np.array([0,0,0])
Mars_M = 6.42e23
G_constant = 6.67e-11

# simulation time, timestep and time
t_max = 7.41
dt = 0.01
t_array = np.arange(0, t_max, dt)

# initialise empty lists to record trajectories
x_list = []
v_list = []

# Euler integration
for t in t_array:
    # append current state to trajectories
    x_list.append(x)
    v_list.append(v)

    # calculate new position and velocity
    magni = math.sqrt((x[0]**2)+(x[1]**2)+(x[2]**2))
    a = (x/magni)*(-G_constant*Mars_M)/(magni**2)
    x = x + dt * v
    v = v + dt * a

#convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_list1 = []
v_list1 = []
for i in x_list:
    x_list1.append(i[2]-Mars_radius)
for j in v_list:
    v_list1.append(j[2])
x_array = np.array(x_list1)
v_array = np.array(v_list1)

# plot the position-time graph
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(t_array, x_array, label='x (m)')
plt.plot(t_array, v_array, label='v (m/s)')
plt.legend()
plt.show()
