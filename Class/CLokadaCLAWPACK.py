#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the OKADA Class - CLAWPACK
IN PROGRESS 
"""

# Moduls imported
import os
import numpy as np
from clawpack.geoclaw import dtopotools

# Load Data
from Data import dataForOkada
from Data import site_neu



class OkadaCLAWPACK():
 
    
    def __init__(self, name):
        self.name = name

    
    def set_params(params):
        """
        Set the subfault parameters. 
        """
        
        subfault = dtopotools.SubFault()
        
        subfault.longitude = params[0]
        subfault.latitude = params[1]
        subfault.depth = params[2]
        subfault.strike = params[3]
        subfault.dip = params[4]
        subfault.length = params[5]
        subfault.width = params[6]
        subfault.rake = params[7]
        subfault.slip = params[8]

        subfault.coordinate_specification = "top center"
    
        fault = dtopotools.Fault()
        fault.subfaults = [subfault]
        
        return fault, subfault
      
        
    def calc_SWZR_okada(self, okada_params, site_neu):
        """
        """
        
        result = dtopotools.SubFault().okada(self, site_neu[1] - okada_params[0], site_neu[0] - okada_params[1])
        
        return result
        
        
    def okada_SWZR_fit(self):
        """
        Evaluates the misfit of an okada solution defined by the passed parameters to the slip (and errors) globally defined.
        """
        
        nsite = len(site_neu.err[0])
        
        slip_weights = np.zeros((3, nsite))
        for i in range(3):
            for j in range(nsite):
                slip_weights = 1 / (site_neu.err[i][j]**2)
        
        # only for z first
        calc_slip = np.zeros((1, nsite))
        slip_misfit = np.zeros((1, nsite))
        
        for isite in range(nsite):
            site_slip = Okada.calc_SWZR_okada(self, dataForOkada.okada_start, site_neu.posn)
            calc_slip[0][isite] = site_slip
            slip_misfit[0][isite] = site_neu.slip[2][isite] - calc_slip[0][isite]
        
        misfit = np.zeros((1, nsite))
        
        for isite in range(nsite):            
            misfit[0][isite] = slip_misfit[0][isite] * slip_weights[2][isite] / (sum(slip_weights[2]))
        
        return misfit 
       
        
        