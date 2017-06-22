# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the OKADA Class
IN PROGRESS 
"""

# Moduls imported
import os
from clawpack.geoclaw import dtopotools
#from Class.CLokada import SubFault
#subfault = SubFault("okada")


class Okada():
 
    
    def __init__(self, name):
        self.name = name

    
    def set_params(params):
        """
        Set the subfault parameters. Most are fixed for the examples below, and only the strike, dip, and rake will be varied.
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


    def calcSWZRokada(self, okada_params, site_neu):
        """
        """
        
        result = dtopotools.SubFault().okada(self, site_neu[1] - okada_params[0], site_neu[0] - okada_params[1])
        
        return result
        
        
    def okadaSWZRfit(self, oakada_params, site_neu):
        """
        Evaluates the misfit of an okada solution defined by the passed parameters to the slip (and errors) globally defined.
        """
        
        [dummy, ]
        

    
    
        
        
