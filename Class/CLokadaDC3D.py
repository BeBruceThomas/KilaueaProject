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

# Moduls imported
import os
import numpy as np
from okada_wrapper import dc3d0wrapper, dc3dwrapper

# Load Data
from Data import dataForOkada
from Data import site_neu



class OkadaDC3D():
 
    
    def __init__(self, name):
        self.name = name
    
    
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
            
        return result
    
    
