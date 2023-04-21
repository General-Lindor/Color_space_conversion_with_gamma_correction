# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:17:56 2023

@author: admin
"""

#POI = points of interest
def interpolateWave(x, POI, wavelength):
    
    keys = list(POI.keys())
    values = list(POI.values())
    items = list(POI.items())
    
    y_average = 0
    for y_i in values:
        y_average += y_i
    y_average /= len(values)
    pi = math.pi / wavelength
    y = y_average
    for i in range(len(items)):
        key, value = items[i]
        Dividend = 1
        Divisor = 1
        for j in range(len(items)):
            if i != j:
                otherKey = (items[j])[0]
                Dividend *= math.sin(pi * (x - otherKey))
                Divisor *= math.sin(pi * (key - otherKey))
        summand = (value - y_average) * (Dividend / Divisor) * math.cos(pi * (x - key))
        y += summand
    
    return y