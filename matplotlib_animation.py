# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 13:01:21 2021

@author: matthew
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def getS(u, a, t):
    
    sx = u[0]*t + 0.5*a[0]*t**2
    sy = u[1]*t + 0.5*a[1]*t**2
    
    return (sx, sy)

def getV(u, a, t):
    
    vx = u[0] + a[0]*t
    vy = u[1] + a[1]*t
    
    return (vx, vy)

a = (0, -10)
inc = 10

noArrows = 10
arrowScale = 10

angleSpace = np.linspace(30, 80, inc)
velSpace = np.linspace(50, 120, inc)

solutions = []

tmax = 40
dt = 1

t = np.linspace(0, tmax, int(tmax/dt))

v0Space = [(vel*np.cos(np.radians(angle)), vel*np.sin(np.radians(angle))) for vel, angle in zip(velSpace, angleSpace)]

    
for vx, vy in v0Space:
        
    s = getS((vx, vy), a, t)
    v = getV((vx, vy), a, t)
    
    solutions.append((s,v))
        
plt.figure(figsize=(10,10))
ax = plt.gca()



#maxDim = max(max(s[0]), max(s[1]))
minDim = -1000
maxDim = 1000
ax.set_xlim(minDim, maxDim)
ax.set_ylim(minDim, maxDim)

ax.hlines(0, minDim, maxDim, color='black')


arrowDispSc = int(len(s[0])/noArrows)

apple = (400*np.cos(np.radians(60)), 400*np.sin(np.radians(60)))
ax.plot(*apple, marker='x', color='red', markersize=20)

viridis = plt.cm.get_cmap('jet', 12)

color = np.linspace(0,1,len(solutions))

for solution, color in zip(solutions, color):
    
    ax.plot(solution[0][0], solution[0][1], color=viridis(color))
    ax.quiver(solution[0][0][::arrowDispSc], solution[0][1][::arrowDispSc], solution[1][0][::arrowDispSc], solution[1][1][::arrowDispSc], color=viridis(color), units='xy', width=2, scale=arrowScale)
    ax.quiver(solution[0][0][::arrowDispSc], solution[0][1][::arrowDispSc], a[0], a[1], color=(1,0,0,1), units='xy', width=2, scale=arrowScale)



plt.show()
    
#print(f's = {s}, v = {v}')


# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# writer = animation.FFMpegWriter(
#     fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)



#print(min(s[0][np.where(s[1]<0)]))
