# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the Okada Data
OK 
You will have to change the PATHS to data (excel or txt) !  
"""


# Moduls imported
import os
import numpy as np

path = "/gps/Bruce/KilaueaProject"



okada_initial_params = np.zeros((3, 11))

okada_start = open(path+"/Data/okada/okada_start.txt", "r")
for i in range(11):
    okada_initial_params[1][i] = okada_start.readline()
okada_start.close()

upper_bounds = open(path+"/Data/okada/upper_bounds.txt", "r")
for i in range(11):
    okada_initial_params[0][i] = upper_bounds.readline()
upper_bounds.close()

lower_bounds = open(path+"/Data/okada/lower_bounds.txt", "r")
for i in range(11):
    okada_initial_params[2][i] = lower_bounds.readline()
lower_bounds.close()

