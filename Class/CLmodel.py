# -*- coding: utf-8 -*-
"""
Kilauea_Project
@author: bruce.eo.thomas
"""

"""
Script for the MODEL Class
IN PROGRESS 
"""

# Moduls imported
import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import (LinearRegression, TheilSenRegressor, RANSACRegressor, HuberRegressor)
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


class Model():
    
    def __init__(self, name):
        self.name = name
    
    def robust_step(self, x, y, x1, x2):
        
        X = x
        Y = y
        
        n = len(X)
        
        I0 = np.ones((n,1))
        I1 = np.ones((n,1))
        
        for i in range(n):
            if X[i] >= x1:
                I0[i][0] = 0
            elif X[i] <= x2:
                I1[i][0] = 0
        
        count = 0
        for i in range(n):
            if I0[i] == 0:
                count += 1
        
        X0 = np.zeros((n-count,1))
        X1 = np.zeros((count,1))
        
        for i in range(n-count):
            X0[i][0] = X[i][0]
        #for i in range(count):
        #    X1[i][0] = X[i+n-1][0]
        
        result = Model.graph(self, X0, Y)
        
        # Data that intrest us 
        ymodel = result[0]
        a0hat = result[1]
        a1hat = result[2]
        bhat = result[3]
               
        return ([ymodel, a0hat, a1hat, bhat])

    
    def graph(self, x, y):
                   
        estimators = [('OLS', LinearRegression()),
                      ('Theil-Sen', TheilSenRegressor(random_state = 42)),
                      ('RANSAC', RANSACRegressor(random_state = 42)),
                      ('HuberRegressor', HuberRegressor())
                     ]
        
        colors = {'OLS': 'turquoise', 'Theil-Sen': 'gold', 'RANSAC': 'lightgreen', 'HuberRegressor': 'black'}
        linestyle = {'OLS': '-', 'Theil-Sen': '-.', 'RANSAC': '--', 'HuberRegressor': '--'}
        lw = 3
        
        x_plot = np.linspace(x.min(), x.max())
                   
        plt.figure(figsize = (10, 8))
        plt.plot(x[:, 0], y, 'b+')
    
        for name, estimator in estimators:
            model = make_pipeline(PolynomialFeatures(3), estimator)
        
            where_are_NaNs = np.isnan(y)
            y[where_are_NaNs] = 0
              
            model.fit(x, y)
        
            #model_ransac = linear_model.RANSACRegressor(linear_model.LinearRegression())
            #model_ransac.fit(this_X, this_Y)              
            
            mse = mean_squared_error(model.predict(x), y)
            y_plot = model.predict(x_plot[:, np.newaxis])
            plt.plot(x_plot, y_plot, color=colors[name], linestyle=linestyle[name], linewidth=lw, label='%s: error = %.3f' % (name, mse))

        
        Xl = []
        for i in range(len(x)):
            Xl.append(x[i][0])
        b = np.polyfit(Xl, y, 1)
        #msep = mean_squared_error(model.predict(x), y)
        ymodel = b[0] * x + b[1]
        a1hat = b[0] * Xl[-1] + b[1]
        plt.plot(x, ymodel, color='red', linestyle='-', linewidth=lw, label='%s: error = %.3f' % ('Polyfit', 0))
        
        legend_title = 'Type Estimation'
        legend = plt.legend(loc='upper right', frameon=False, title=legend_title)        
        plt.title('Kilauea Project')
             
        plt.show()
        
        return ([ymodel, b[1], a1hat, b[0]])