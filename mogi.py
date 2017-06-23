#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 12:40:08 2017

@author: gps
"""

"""
Code for computing mogi model as a function of horintal distance from 
source (radius) and plotting

Nick Voss 
USF geodesy lab

October 2015

Bruce Thomas modification june 2017
"""

import numpy as np
import matplotlib.pylab as plt


poisson_ratio = 0.25
mu = 30.0
lmda = 2 * mu * poisson_ratio / (1 - 2 * poisson_ratio)
alpha = (lmda + mu) / (lmda + 2 * mu)

x = np.arange(0, 14, .01)#set up array of horizontal values to compute 
#alpha = 0.2 #km radius of body
d = 1.0 #km depth
delV = 0.2 #km^3 change in volume
v = .25 #poissons ratio

#calculate horizontal displacement
h = (3.0/4.0)*(delV/np.pi)*(x/((x**2+d**2)**(3/2))) #units of km
h = [i*100000 for i in h] # convert km to cm

#calculate vertical displacement 
v = (3.0/4.0)*(delV/np.pi)*(d/((x**2+d**2)**(3/2)))
v = [i*100000 for i in v] #convert km to cm
# plot results
ax = plt.subplot(211)
plt.plot(x,v)
plt.title('Displacement due to a Mogi Source')
plt.ylabel('Vertical Displacement in (cm)')

plt.subplot(212, sharex = ax)
plt.plot(x,h)
plt.xlabel('Horizontal distance from center of sphere (km)')
plt.ylabel('Horizontal displacement (cm)')
plt.savefig('mogiPython.png')
plt.show()