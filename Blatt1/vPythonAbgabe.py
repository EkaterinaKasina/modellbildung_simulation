#from vpython import *
from visual import *
import numpy as np

scene.caption = """
yellow: based on position measurement
green: based on velocity measurement
red: based on acceleration measurement
As we can see, the position based an acceleration based one agree quite well with each other, while the velocity based one runs a little too far.
"""

def height(x):
    x
    lower = 9.0
    upper = 32.0
    if x <= lower:
        return 0.0
    if x <= upper:
        return -(x-lower)*21.8/(upper - lower)
    return -21.8

def acc(x):
    t1 = 7.75
    t2 = 8.9
    t3 = 10
    t4 = 30.5
    t5 = 31.5
    t6 = 32.75
    amp_n = 0.85
    amp_p = 0.85
    default = 0.0 #0.05
    
    if x < t1: #flat
        return 0.0 + default
    if x < t2: #down
        return -(x-t1)*amp_n/(t2-t1) + default
    if x < t3: #up
        return (x-t2)*amp_n/(t3-t2)-amp_n + default
    if x < t4: #flat
        return 0.0 + default
    if x < t5: #up
        return (x-t4)*amp_p/(t5-t4) + default
    if x < t6: #down
        return -(x-t5)*amp_p/(t6-t5)+amp_p + default
    return 0.0 + default #flat

def vel(x):
    if x <= 6.0:
        return 0.0
    if x <= 12.0:
        return -(x-6)/6.0
    if x <= 29.0:
        return -1.0
    if x <= 35.0:
        return (x-29)/6.0-1
    return 0.0
	
k1 = sphere(pos=vector(-10,0,0), radius=1, color=color.yellow, make_trail=True, trail_type='points', interval=10, retain=20)
k2 = sphere(pos=vector(0,0,0), radius=1, color=color.green, make_trail=True, trail_type='points', interval=10, retain=20)
k3 = sphere(pos=vector(10,0,0), radius=1, color=color.red, make_trail=True, trail_type='points', interval=10, retain=20)
	
while True:
	k1.pos = vector(0,0,0)
	k2.pos = vector(10,0,0)
	k3.pos = vector(20,0,0)
	
	k3.p = vector(0,0,0)
	k3.mass = 1
	dt = 0.05
	for t in arange(0,50,dt):
		rate(200)
		k1.pos = vector(0, height(t), 0)
		k2.pos = k2.pos + vector(0, dt * vel(t), 0)
		k3.p = k3.p + vector(0, acc(t), 0) * dt
		k3.pos = k3.pos + (k3.p / k3.mass) * dt
		
		
		
		
		
