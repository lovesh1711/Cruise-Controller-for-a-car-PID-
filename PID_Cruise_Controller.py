
# Cruise Control for a car for a fixed set-point velocity


import matplotlib.pyplot as plt
import numpy as np

m=500                       # mass of the car
b=10                        # damping constant       
v=0                         # intial velocity

# PID tunning parameters
kp=100 
ki=0.5
kd=5

v_desired=60                # desired velocity

# creating a array to store velocity and time values to plot the graph later.
velocity=[]   
time=[]

ei=0
e_old=14
for i in range(1000):
    t=i
    e=v_desired-v
    ei=ei+e
    ed=e-e_old
    u=ki*ei + kp*e + kd*ed   # control equation
    v_new=(u-b*v)/m+v        # Cruise control dynamics derived by newton's laws
    v=v_new
    velocity.append(v_new)
    time.append(t)
x1=[0,1000]
y1=[60,60]

# plot the graph using Matplotlib library
plt.plot(time,velocity)
plt.plot(x1,y1,label="reference line")
plt.show()
