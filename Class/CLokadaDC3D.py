#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the OKADA Class - DC3D
IN PROGRESS 
"""

import os
cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))

os.chdir("/gps/Bruce/KilaueaProject")

cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in '%s': %s" % (cwd, files))

# Moduls imported
from okada_wrapper.okada_wrapper.okada_wrapper import dc3d0wrapper, dc3dwrapper
import numpy as np
import matplotlib.pyplot as plt
import time

# Load Data
from Data import dataForOkada
from Data import site_neu



plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Computer Modern Roman']
plt.rcParams['text.usetex'] = True
plt.rcParams['font.size'] = 14
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'
plt.rcParams['lines.linewidth'] = 1



class OkadaDC3D():
 
    
    def __init__(self, name):
        self.name = name
    
    
    def get_params(self):
        
        poisson_ration = dataForOkada.okada_start[10]
        mu = 30
        #mu = 1.0
        lmda = (2 * mu * poisson_ratio) / (1 - 2 * poisson_ratio)
        alpha = (lmda + mu) / (lmda + 2 * mu)
        
        x0 = [ dataForOkada.okada_start[0], dataForOkada.okada_start[1], - dataForOkada.okada_start[2] ]
        depth = dataForOkada.okada_start[2]
        dip = dataForOkada.okada_start[4]
        strike_width = [ -dataForOkada.okada_start[5]/2, dataForOkada.okada_start[5]/2 ]
        dip_width = [ -dataForOkada.okada_start[6]/2, dataForOkada.okada_start[6]/2 ]
        dislocation = [ dataForOkada.okada_start[7], dataForOkada.okada_start[8], dataForOkada.okada_start[9] ]
        
        return alpha, x0, depth, dip, strike_width, dip_width, dislocation
    
    def test_dc3d():
        alpha, x0, depth, dip, strike_width, dip_width, dislocation = OkadaDC3D.get_params(self)
        n = (100, 100)
        x = linspace(dataForOkada.lower_bounds[0], dataForOkada.upper_bounds[0], n[0])
        y = linspace(dataForOkada.lower_bounds[1], dataForOkada.upper_bounds[1], n[1])
        ux = zeros((n[0], n[1]))
        for i in range(n[0]):
            for j in range(n[1]):
                success, u, grad_u = dc3dwrapper(alpha,
                                                 [x0[i], y0[j], x0[2]],
                                                 depth, 
                                                 dip,
                                                 strike_width, 
                                                 dip_width,
                                                 dislocation
                                                )
                assert(success == 0)
                ux[i, j] = u[0]
    
        levels = linspace(-0.5, 0.5, 21)
        cntrf = contourf(x, y, ux.T, levels = levels)
        contour(x, y, ux.T, colors = 'k', levels = levels, linestyles = 'solid')
        xlabel('x')
        ylabel('y')
        cbar = colorbar(cntrf)
        tick_locator = matplotlib.ticker.MaxNLocator(nbins=5)
        cbar.locator = tick_locator
        cbar.update_ticks()
        cbar.set_label('$u_{\\textrm{x}}$')
        savefig("strike_slip.png")
        show()
    
    
    def calc_SWZR_okada(self, okada_params, site_neu):
        """
        """
        
        #result = dtopotools.SubFault().okada(self, site_neu[1] - okada_params[0], site_neu[0] - okada_params[1])
        
        success, u, grad_u = dc3dwrapper(0.6, 
                                         [1.0, 1.0, -1.0],
                                         3.0, 
                                         90, 
                                         [-0.7, 0.7], 
                                         [-0.7, 0.7],
                                         [1.0, 0.0, 0.0]
                                         ) 
            
        return success
    
    
