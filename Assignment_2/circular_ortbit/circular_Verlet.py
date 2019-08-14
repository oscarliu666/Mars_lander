import numpy as np
import matplotlib.pyplot as plt
import math

# mass, spring constant, initial position and velocity
Mars_radius = 3.39e6
x = np.array([0,0,Mars_radius+100])
v = np.array([4500,0,0])
Mars_M = 6.42e23
G_constant = 6.67e-11

# Creating first two data using Euler's method
t_max = 0.2
dt = 0.1
t_array = np.arange(0, t_max, dt)
x_list = []
v_list = []
for t in t_array:
    x_list.append(x)
    v_list.append(v)
    magni = math.sqrt((x[0]**2)+(x[1]**2)+(x[2]**2))
    a = (x/magni)*(-G_constant*Mars_M)/(magni**2)
    x = x + dt * v
    v = v + dt * a

# Verlet method    
t_max = 15000
dt = 0.1
t_array = np.arange(0.2, t_max, dt)

counter = 1
# Euler integration
for t in t_array:
    # append current state to trajectories
    # calculate new position and velocity
    magni = math.sqrt((x[0]**2)+(x[1]**2)+(x[2]**2))
    a = (x/magni)*(-G_constant*Mars_M)/(magni**2)
    x = 2*x_list[counter]-x_list[counter-1]+(dt**2)*a 
    v = (1/dt)*(x-x_list[counter])    
    x_list.append(x)
    v_list.append(v)
    counter +=1
# convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
x_listx = []
x_listz = []
v_list1 = []
for i in x_list:
    x_listx.append(i[0])
for j in x_list:
    x_listz.append(j[2])
for m in v_list:
    magni = math.sqrt((m[0]**2)+(m[1]**2)+(m[2]**2))
    v_list1.append(magni)
x_arrayx = np.array(x_listx)
x_arrayz = np.array(x_listz)
v_array = np.array(v_list1)
# plot the trajectory graph

t_array1 = np.arange(0,t_max,dt)
plt.figure(1)
plt.clf()
plt.xlabel('x/m')
plt.ylabel("z/m")
plt.grid()
plt.plot(x_arrayx, x_arrayz, label='trajectory')
plt.legend()
plt.show()
# plot the velocity graph
t_array1 = np.arange(0,t_max,dt)
plt.figure(1)
plt.clf()
plt.xlabel('v/m*s-1')
plt.ylabel("t/s")
plt.grid()
plt.plot(t_array1, v_array, label='velocity vs time')
plt.legend()
plt.show()


