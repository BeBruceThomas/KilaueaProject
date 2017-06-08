# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
IN PROGRESS 
"""

# Moduls imported
import os
import numpy as np
import matplotlib.pyplot as plt

# Load final_vstack_out_pagers_rtv_datenums
from Data import rtv
# Load BI_linefile
from Data import bi

# Import personnal modul and class 
from Class.CLannex import Annex
annex = Annex("annex")
from Class.CLcalendar import Calendar
cal = Calendar("calendar")
from Class.CLgeographic import Geographic
geo = Geographic("geographic")
from Class.CLmodel import Model
mod = Model("model")
from Class.CLokada import Okada
oka = Okada("okada")
from Class.CLstation import Station
sta = Station("station")


# Main program : all the run is done here
def main():
    
    
    #--------------------------------------------------------------------------
    # GPS station : ids and dates 
    #--------------------------------------------------------------------------
    
    
    # Date of start of analyse
    t0 = cal.jdyTOmjd(125, 2015)
    # Dates of start and end of dike
    t1 = cal.jdyTOmjd(133, 2015)
    t2 = cal.jdyTOmjd(137, 2015)
      
    # Reference sites for GPS   
    # kilsites is actually a list but on matlab it was a table !!!            
    kilsites = ['UWEV', 'NUPM', 'AHUP', 'HOVL', 'CNPK', 'BYRL', 'NPIT', 'KOSM', 'OUTL', 'CRIM', 'MANE', 'HLNA', 'KFAP', 'AINP', 'GOPM']
   
    # isN : table with numbers assigned at each GPS station name
    # ! "is" is not use as a variable in Python beaucause it already exist as a function in Python, not the same as in MATLAB 
    isN = sta.stname2num(rtv.stnm, kilsites)
    # isN size : 15 lines (GPS number) for 1 column
    len_isN = len(isN)
    
    # it : array with ids of measures after t0 
    it = np.where(rtv.epochs >= t0)
    # it size : 1 line for n columns (398)
    len_it = len(it[0])
    
    # mjds : list with dates assigned at each ids of array "it"
    # mjds size : len_it elements (398)
    mjds = [0] * len_it
    for i in range(len_it):
        mjds[i] = rtv.epochs[it[0][i]]
    # conversion of mjds in jdays & years
    """
    # Conversion in jdays & years 
    # [doys, yrs] = mjday(mjds)
    jdys = np.zeros((len_it,2))
    for i in range(len_it):
        [doys, yrs] = cal.mjdTOjdy( mjds[i] )
        jdys[i][0] = doys
        jdys[i][1] = yrs
    """
    
    # subN, subE, subU : tables for north, east and altitude coordinates for the stations of interest after date t0
    # subN, subE, subU size : len_isN (15) lines, one for each GPS & len_it (398) columns, one for each date of measure after t0
    subN = np.zeros((len_isN, len_it))
    for i in range(len_it):
        for j in range(len_isN):
            subN[j][i] = rtv.rt_north.cell_value(int(isN[j][0])+1, i+311)
    subE = np.zeros((len_isN, len_it))
    for i in range(len_it):
        for j in range(len_isN):
            subE[j][i] = rtv.rt_east.cell_value(int(isN[j][0])+1, i+311)
    subU = np.zeros((len_isN, len_it))
    for i in range(len_it):
        for j in range(len_isN):
            subU[j][i] = rtv.rt_up.cell_value(int(isN[j][0])+1, i+311)
    
    # ifit : list with dates after t0 but not during the dike, same role as it but without dike dates and has the form of a list not array
    # ifit size : date number (303) elements 
    ifit1 = np.where(mjds <= t1)[0]
    ifit2 = np.where(mjds >= t2)[0]
    len_ifit = len(ifit1) + len(ifit2)
    #ifit = np.zeros((1, len_ifit))
    ifit = [0] * len_ifit
    j = 0
    for i in range(len_ifit):
        if i <= len(ifit1)-1:
            ifit[i] = ifit1[i] + 1
        else:
            ifit[i] = ifit2[j] + 1
            j += 1

    
    #--------------------------------------------------------------------------
    # Fit a Robust Step to each site's time series.
    #--------------------------------------------------------------------------

    
    # x : table with dates for each ifit ids (without dike) 
    # x size : n lines (303) for 1 column 
    
    x = np.zeros((len_ifit, 1))
    for i in range(len_ifit):
        x[i][0] = mjds[ifit[i]-1]
    
    """
    x = [0] * len_ifit
    for i in range(len_ifit):
        x[i] = mjds[ifit[i]-1]
    """
    """
    x = np.ones((len_ifit, 1)) * 3
    
    y = np.ones((len_ifit, 303)) * 2
    """
    # search on each GPS site 
    stepN = [0] * len_isN
    errsN = [0] * len_isN  
    stepE = [0] * len_isN
    errsE = [0] * len_isN
    stepU = [0] * len_isN
    errsU = [0] * len_isN
       
    for isite in range(0, len_isN):
        [ymodel, a0hat, a1hat, bhat] = mod.robust_step(x, annex.get_y(ifit, subN, isite)[1], t1, t2)
        stepN[isite] = a1hat
        #errsN[isite] = stats.se(2)
        [ymodel, a0hat, a1hat, bhat] = mod.robust_step(x, annex.get_y(ifit, subE, isite)[1], t1, t2)
        stepE[isite] = a1hat
        #errsE[isite] = stats.se(2)
        [ymodel, a0hat, a1hat, bhat] = mod.robust_step(x, annex.get_y(ifit, subU, isite)[1], t1, t2)
        stepU[isite] = a1hat
        #errsU[isite] = stats.se(2)  
    
    
    # Save data in a GMT-readable table
    fid = open("Kilauea_May2015_Intrusion.dat", "w")
    fid.write("Site     Lat          Lon            Elev       N (mm)    err     E (mm)    err     U (mm)    err")
    fid.write("")
    
    # Write data for each GPS station 
    for isite in range(len_isN):
        fid.write("\n" 
                  + kilsites[isite] 
                  + "     " 
                  + str( format(rtv.lat[ isN[isite][0] ] [0], '.5f') ) 
                  + "     "
                  + str( format(rtv.lon[ isN[isite][0] ] [0], '.5f') )
                  + "     "
                  + str( format(rtv.elev[ isN[isite][0] ] [0], '.1f').zfill(6) )
                  + "     "
                  + str( format(stepN[isite], '.1f').zfill(5) )
                  + "     "
                  + str( format(errsN[isite], '.1f') )
                  + "     "
                  + str( format(stepE[isite], '.1f').zfill(5) )
                  + "     "
                  + str( format(errsE[isite], '.1f') )
                  + "     "
                  + str( format(stepU[isite], '.1f').zfill(5) )
                  + "     "
                  + str( format(errsU[isite], '.1f') )
                  )
    # Close table for a save!
    fid.close()


    #--------------------------------------------------------------------------
    # Plot GPS data and linear regression. 
    #--------------------------------------------------------------------------
    
    
    # Plot variables
    x0 = 250000
    y0 = 2140000
    xlims = [0, 20000]
    ylims = [-2500, 17500]
    
    # site : table with UTM coordinate of each station GPS 
    siteLAT = np.zeros((len_isN, 1))
    siteLON = np.zeros((len_isN, 1))
    for isite in range(len_isN):
        result = geo.from_latlon(rtv.lat[isN[isite][0]][0], rtv.lon[isN[isite][0]][0])
        siteLAT[isite] = result[0]
        siteLON[isite] = result[1]               
    
    #twocolfig(6.5)
    plt.figure(figsize = (10, 8))
    # Plot faults?  
    plt.plot(bi.fx - x0, bi.fy - y0, 'k-')   
    
    # Plot Big Island
    plt.plot(bi.cx - x0, bi.cy - y0, 'k-')
    
    # Define limit axes
    """
    axes = plt.gca()
    axes.set_xlim([xlims[0], xlims[1]])
    axes.set_ylim([ylims[0], ylims[1]])
    """
    plt.plot(siteLAT - x0, siteLON - y0, 'bo')
    """
    hvert = plt.quiver(siteLAT - x0, siteLON - y0, 0 * stepE, stepU, 1)
    #hhoriz = quiver(sitex - x0, sitey - y0, stepE, stepN, 1)
    #set(hhoriz,'Color','r')
    plt.scatter(siteLAT - x0, siteLON - y0, color='r', s=5)
    #set(hvert, 'Color', 'm')
    """
    plt.title("GPS Vectors between days 133 and 137 2015")
    
    plt.show()
    plt.savefig("GPS_Vectors_133_137_2015.png")
    
    
    #--------------------------------------------------------------------------
    # Fit an Okada : surface deformation due to a finite rectangular source.
    #--------------------------------------------------------------------------
    
    
    """
    # Defnition of the site locations & motions
    site_neu_posn = [sitey - y0, sitex - x0, rtv.elev(isN)]
    site_neu_slip = [stepN, stepE, stepU]
    site_neu_err =  [errsN, errsE, errsU]
    
    # Okada parameters
    #                   E,     N,    Z, strike,   dip,  length,  width,  rake,   slip, opening    ,nu  ???
    upper_bounds = [14000, 12000, 5000,    180,    90,    1000,   5000,   0.1,    0.1,   10000]
    okada_start  = [ 8000,  5000, 1000,    -45,     0,    4000,   2000,   0.0,    0.0,    1000]
    lower_bounds = [ 2000,     0,    0,   -180,   -90,     500,    100,  -0.1,   -0.1,       1]
    
    """
    
    
   
"""    
% fit an okada to the data:

%[okada_params,resnorm,residual,exitflag] =  lsqnonlin('okada_SWRZ_fit',okada_start,lower_bounds,upper_bounds);
options = optimset('fminsearch');
[okada_params,resnorm,exitflag,output] =  fminsearchbnd('okada_SWRZ_fit',okada_start,lower_bounds,upper_bounds,options);
        
calc_slip = NaN.*site_neu_err;

for isite = 1:nsites;
    site_slip = calc_SWRZ_okada(okada_params,site_neu_posn(:,isite));
    calc_slip(:,isite)=site_slip;
end

h_okada_vert=quiver(sitex-x0,sitey-y0,0*stepE',calc_slip(3,:)',1)
h_okada_horiz=quiver(sitex-x0,sitey-y0,calc_slip(2,:)',calc_slip(1,:)',1)
set(h_okada_horiz,'Color','k')
set(h_okada_vert,'Color',[.7 .7 .7])
"""

main()