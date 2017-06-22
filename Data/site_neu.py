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
s = open(path+"/Data/site_neu/site_neu_posnY.txt", "r")
len_s = 0
while s.readline():
    len_s += 1
s.close()


posn = np.zeros((3, len_s))

posnY = open(path+"/Data/site_neu/site_neu_posnY.txt", "r")
for i in range(len_s):
    posn[0][i] = posnY.readline()
posnY.close()
posnX = open(path+"/Data/site_neu/site_neu_posnX.txt", "r")
for i in range(len_s):
    posn[1][i] = posnX.readline()
posnX.close()
posnZ = open(path+"/Data/site_neu/site_neu_posnZ.txt", "r")
for i in range(len_s):
    posn[2][i] = posnZ.readline()
posnZ.close()


slip = np.zeros((3, len_s))

slipY = open(path+"/Data/site_neu/site_neu_slipY.txt", "r")
for i in range(len_s):
    slip[0][i] = slipY.readline()
slipY.close()
slipX = open(path+"/Data/site_neu/site_neu_slipX.txt", "r")
for i in range(len_s):
    slip[1][i] = slipX.readline()
slipX.close()
slipZ = open(path+"/Data/site_neu/site_neu_slipZ.txt", "r")
for i in range(len_s):
    slip[2][i] = slipZ.readline()
slipZ.close()


err = np.zeros((3, len_s))

errY = open(path+"/Data/site_neu/site_neu_errY.txt", "r")
for i in range(len_s):
    err[0][i] = errY.readline()
errY.close()
errX = open(path+"/Data/site_neu/site_neu_errX.txt", "r")
for i in range(len_s):
    err[1][i] = errX.readline()
errX.close()
errZ = open(path+"/Data/site_neu/site_neu_errZ.txt", "r")
for i in range(len_s):
    err[2][i] = errZ.readline()
errZ.close()