# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the BI_linefile Data
OK
You will have to change the PATHS to data (excel or txt) !  
"""


# Moduls imported
import os
import numpy as np
import matplotlib.pyplot as plt


# feature: size of doc
bi_fx = open("C:\\Users\\bruce\\Desktop\\KilaueaProject\\Data\\BI_linefile\\features\\x.txt", "r")
len_fxy = 0
while bi_fx.readline():
    len_fxy += 1
bi_fx.close()
# feature.x
bi_fx = open("C:\\Users\\bruce\\Desktop\\KilaueaProject\\Data\\BI_linefile\\features\\x.txt", "r")
fx = np.zeros((len_fxy, 1))
for i in range(len_fxy):
    fx[i][0] = bi_fx.readline()
bi_fx.close()
# feature.y
bi_fy = open("C:\\Users\\bruce\\Desktop\\KilaueaProject\\Data\\BI_linefile\\features\\y.txt", "r")
fy = np.zeros((len_fxy, 1))
for i in range(len_fxy):
    fy[i][0] = bi_fy.readline()
bi_fy.close()

# coast: size of doc
bi_cx = open("C:\\Users\\bruce\\Desktop\\KilaueaProject\\Data\\BI_linefile\\coast\\x.txt", "r")
len_cxy = 0
while bi_cx.readline():
    len_cxy += 1
bi_cx.close()
# coast.x
bi_cx = open("C:\\Users\\bruce\\Desktop\\KilaueaProject\\Data\\BI_linefile\\coast\\x.txt", "r")
cx = np.zeros((len_cxy, 1))
for i in range(len_cxy):
    cx[i][0] = bi_cx.readline()
bi_cx.close()
# coast.y
bi_cy = open("C:\\Users\\bruce\\Desktop\\KilaueaProject\\Data\\BI_linefile\\coast\\y.txt", "r")
cy = np.zeros((len_cxy, 1))
for i in range(len_cxy):
    cy[i][0] = bi_cy.readline()
bi_cy.close()