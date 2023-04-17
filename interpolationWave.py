# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 13:17:56 2023

@author: admin
"""

#POI = points of interest
#make sure 0<=x<1 for all POI keys
def interpolateWave(x, POI):
    
    keys = list(POI.keys())
    values = list(POI.values())
    items = list(POI.items())
    
    y_s = 0
    for y in values:
        y_s += y
    y_s /= len(values)
    
    p = 2 * math.pi
    
    result = y_s
    for key, value in items:
        Dividend = 1
        Divisor = 2
        for otherKey in keys:
            
            #This would be ideal but floats are too imprecise for that:
            #if abs(key - otherKey) % 0.5 != 0:
            
            #This is what we do instead:
            if abs((abs(key - otherKey) % 0.5) - 0) <= 0.001:
                
                otherKey = (items[j])[0]
                Dividend *= math.sin(p * (x - otherKey))
                Divisor *= math.sin(p * (key - otherKey))
        
        summand = (value - y_s) * (Dividend / Divisor) * (math.cos(p * (x - key)) + math.cos(2 * p * (x - key)))
        result += summand
    
    return result