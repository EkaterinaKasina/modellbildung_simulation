import numpy as np     # get ODE solvers, numpy
import vpython as vp         # get VPython modules for animation
vec=vp.vector

def leapfrog(lfdiffeq, r0, v0, t, h):       # vectorized leapfrog
    """ vector leapfrog method using numpy arrays.
        It solves general (r,v) ODEs as: 
        dr[i]/dt = f[i](v), and dv[i]/dt = g[i](r).
        User supplied lfdiffeq(id, r, v, t) returns
        f[i](r) if id=0, or g[i](v) if id=1.
        It must return a numpy array if i>1 """
    hh = h/2.0
    r1 = r0 + hh*lfdiffeq(0, r0, v0, t)     # 1st: r at h/2 using v0    @\lbl{line:lf1}@
    v1 = v0 +  h*lfdiffeq(1, r1, v0, t+hh)  # 2nd: v1 using a(r) at h/2 @\lbl{line:lf2}@
    r1 = r1 + hh*lfdiffeq(0, r0, v1, t+h)   # 3rd: r1 at h using v1     @\lbl{line:lf3}@
    return r1, v1
  
     
def earth(id, r, v, t):            # return the eqns of motion
    if (id == 0): return v         # velocity, dr/dt
    s = vp.mag(np.array(r[0],r[1],0))   # $s=|\vec{r}|$
    return -GM*r/(s*s*s)           # accel dv/dt, faster than s**3  
        
def go():
    r = np.array([1.017, 0.0])     # initial x,y position for earth   
    v = np.array([0.0, 6.179])     # initial vx, vy                   
    
    # draw the scene, planet earth/path, sun/sunlight               
    #scene = vp.canvas(title='Planetary motion', background=vec(.2,.5,1), forward=vec(0,2,-1))
    planet= vp.sphere(pos=vec(r[0],r[1],0), radius=0.1, make_trail=True, up=vec(0,0,1))
    sun   = vp.sphere(pos=vec(0,0,0), radius=0.2, color=vp.color.yellow)
    sunlight = vp.local_light(pos=vec(0,0,0), color=vp.color.yellow) #scn end 
    
    t, h = 0.0, 0.001
    while True:
        vp.rate(200)   # limit animation speed
        r, v = leapfrog(earth, r, v, t, h)  # integrate 
        planet.pos = vec(r[0],r[1],0)           # move planet    

        
GM = 4*np.pi*np.pi          # G*Msun
go()
