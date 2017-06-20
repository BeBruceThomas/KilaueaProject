#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 10:42:25 2017

@author: gps
"""


import matplotlib.pyplot as plt
import numpy as np

from clawpack.geoclaw import dtopotools
from clawpack.visclaw.JSAnimation import IPython_display
import clawpack.visclaw.JSAnimation.JSAnimation_frametools as J

def set_fault(strike, dip, rake, depth):
    """
    Set the subfault parameters.
    Most are fixed for the examples below,
    and only the strike, dip, and rake will be varied.
    """
    subfault = dtopotools.SubFault()
    subfault.strike = strike
    subfault.dip = dip
    subfault.rake = rake
    subfault.length = 100.e3
    subfault.width = 50.e3
    subfault.depth = depth
    subfault.slip = 1.
    subfault.longitude = 0.
    subfault.latitude = 0.
    subfault.coordinate_specification = "top center"

    fault = dtopotools.Fault()
    fault.subfaults = [subfault]
    return fault, subfault

# Create a sample fault and print out some information about it...
fault, subfault = set_fault(0,0,0,5e3)
print ("This sample fault has %s meter of slip over a %s by %s km patch" \
       % (subfault.slip,subfault.length/1e3,subfault.width/1e3))
print ("With shear modulus %4.1e Pa the seismic moment is %4.1e" % (subfault.mu, subfault.Mo()))
print ("   corresponding to an earthquake with moment magnitude %s" % fault.Mw())
print ("The depth at the top edge of the fault plane is %s km" % (subfault.depth/1e3))

def plot_okada(strike, dip, rake, depth, verbose=False):
    """
    Make 3 plots to illustrate the Okada solution.
    """

    fault,subfault = set_fault(strike, dip, rake, depth)
    ax1 = plt.subplot(2,2,1)
    ax2 = plt.subplot(2,2,2)
    ax3 = plt.subplot(2,2,3)
    ax4 = plt.subplot(2,2,4)

    # Subfault projection on surface on ax1:
    ax = fault.plot_subfaults(axes=ax1, plot_rake=True, xylim=[-.5,1.5, -1,1])
    plt.text(0.6,0.8,"Strike = %5.1f" % strike, fontsize=12)
    plt.text(0.6,0.6,"Dip = %5.1f" % dip, fontsize=12)
    plt.text(0.6,0.4,"Rake = %5.1f" % rake, fontsize=12)
    plt.text(0.6,0.2,"Depth = %5.1f km" % (depth/1e3), fontsize=12)
    ax1.set_ylabel('latitude (degrees)')

    # Depth profile on ax3:
    z_top = -subfault.centers[0][2] / 1e3 # convert to km
    z_bottom = -subfault.centers[2][2] / 1e3 # convert to km
    ax3.plot([0,np.cos(subfault.dip*np.pi/180.)*subfault.width/1.e3], [z_top, z_bottom])
    ax3.set_xlim(-50,150)
    ax3.set_ylim(-55,0)
    ax3.set_xlabel('distance orthogonal to strike')
    ax3.set_ylabel('depth (km)')
    ax3.set_title('Depth profile')


    # Grid to use for evaluating and plotting dz
    x = np.linspace(-0.5, 1., 101)
    y = np.linspace(-1., 1., 101)
    times = [1.]

    # color map of deformation dz on ax2:
    fault.create_dtopography(x,y,times,verbose=verbose)
    dtopo = fault.dtopo
    dtopo.plot_dZ_colors(t=1., axes=ax2)

    # transect of dz on ax4:
    dZ = dtopo.dZ[-1,50,:]
    ax4.plot(x,dZ)
    ax4.set_ylim(-0.5,0.5)
    ax4.set_title('Transect of dz along y=0')
    ax4.set_xlabel('Longitude (degrees)')
    ax4.set_ylabel('Seafloor deformation (m)')


fig=plt.figure(figsize=(10,10))
plot_okada(strike=0, dip=10, rake=80, depth=5e3, verbose=True)




plotdir = 'okada_strike_plots'
J.make_plotdir(plotdir, clobber=True)
fig=plt.figure(figsize=(10,10))
for k,strike in enumerate(np.linspace(0,340,18)):
    plt.clf()
    plot_okada(strike, 10., 80., 5e3)
    J.save_frame(k, plotdir=plotdir, verbose=False)

plt.clf()
anim = J.make_anim(plotdir)
anim


plotdir = 'okada_dip_plots'
J.make_plotdir(plotdir, clobber=True)
fig=plt.figure(figsize=(10,10))
for k,dip in enumerate(np.linspace(0,90,10)):
    plt.clf()
    plot_okada(0., dip, 90., 5e3)
    J.save_frame(k, plotdir=plotdir, verbose=False)

plt.clf()
anim = J.make_anim(plotdir)
anim


plotdir = 'okada_rake_plots'
J.make_plotdir(plotdir, clobber=True)
fig=plt.figure(figsize=(9,9))
for k,rake in enumerate(np.linspace(-90,90,19)):
    plt.clf()
    plot_okada(0., 10., rake, 5e3)
    J.save_frame(k, plotdir=plotdir, verbose=False)

plt.clf()
anim = J.make_anim(plotdir)
anim


plotdir = 'okada_depth_plots'
J.make_plotdir(plotdir, clobber=True)
fig=plt.figure(figsize=(9,9))
for k,depth in enumerate(np.arange(0,40,2)*1e3):
    plt.clf()
    plot_okada(0., 10., 80, depth)
    J.save_frame(k, plotdir=plotdir, verbose=False)

plt.clf()
anim = J.make_anim(plotdir)
anim

