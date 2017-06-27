# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the site_neu Data
OK 
You will have to change the PATHS to data (excel or txt) !  
"""


# Moduls imported
import os
import numpy as np

path = "/gps/Bruce/KilaueaProject"



# Size of site_neu data docs
s = open(path+"/Data/site_neu/site_neu_posnY.dat", "r")
len_s = 0
while s.readline():
    len_s += 1
s.close()


posn = np.zeros((3, len_s))

posnY = open(path+"/Data/site_neu/site_neu_posnY.dat", "r")
for i in range(len_s):
    posn[0][i] = posnY.readline()
posnY.close()
posnX = open(path+"/Data/site_neu/site_neu_posnX.dat", "r")
for i in range(len_s):
    posn[1][i] = posnX.readline()
posnX.close()
posnZ = open(path+"/Data/site_neu/site_neu_posnZ.dat", "r")
for i in range(len_s):
    posn[2][i] = posnZ.readline()
posnZ.close()


slip = np.zeros((3, len_s))

slipY = open(path+"/Data/site_neu/site_neu_slipY.dat", "r")
for i in range(len_s):
    slip[0][i] = slipY.readline()
slipY.close()
slipX = open(path+"/Data/site_neu/site_neu_slipX.dat", "r")
for i in range(len_s):
    slip[1][i] = slipX.readline()
slipX.close()
slipZ = open(path+"/Data/site_neu/site_neu_slipZ.dat", "r")
for i in range(len_s):
    slip[2][i] = slipZ.readline()
slipZ.close()


err = np.zeros((3, len_s))

errY = open(path+"/Data/site_neu/site_neu_errY.dat", "r")
for i in range(len_s):
    err[0][i] = errY.readline()
errY.close()
errX = open(path+"/Data/site_neu/site_neu_errX.dat", "r")
for i in range(len_s):
    err[1][i] = errX.readline()
errX.close()
errZ = open(path+"/Data/site_neu/site_neu_errZ.dat", "r")
for i in range(len_s):
    err[2][i] = errZ.readline()
errZ.close()