# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 11:17:03 2023

@author: admin
"""

#STANDARD RGB-HSL MODEL FROM WIKIPEDIA

from vectors import matrix, vector
import math

class rgb(vector):
    def __init__(self, r, g, b):
        super(rgb, self).__init__((r, g, b))
    
    def hsl(self):

        MAX = max(self)
        MIN = min(self)
        
        #LIGHTNESS
        lightness = (MAX + MIN) / 2
        if lightness < 0.001:
            return hsl(0, 0, 0)
        elif lightness > 0.999:
            return hsl(0, 0, 1)
        
        #SATURATION
        saturation = (MAX - MIN) / (1 - abs(MAX + MIN - 1))
        
        #HUE
        if MAX == self[0]:
            hue = (1 / 6) * (0 + ((self[1] - self[2]) / (MAX - MIN)))
        elif MAX == self[1]:
            hue = (1 / 6) * (2 + ((self[0] - self[2]) / (MAX - MIN)))
        elif MAX == self[2]:
            hue = (1 / 6) * (4 + ((self[0] - self[1]) / (MAX - MIN)))
        else:
            raise Exception("minColorError")
        if hue < 0:
            hue += 1
        if hue > 1:
            hue = 0
        
        return hsl(hue, saturation, lightness)

class hsl(vector):
    def __init__(self, r, g, b):
        super(hsl, self).__init__((r, g, b))
            
    def f(self, n):
        hue = self[0]
        saturation = self[1]
        lightness = self[2]
        
        k = (n + (12 * hue)) % 12
        a = saturation * min(lightness, 1 - lightness)
        
        result = lightness - (a * max(-1, min(k - 3, 9 - k, 1)))
        return result
    
    def rgb(self):
        
        lightness = self[2]
        
        if lightness < 0.001:
            return rgb(0, 0, 0)
        elif lightness > 0.999:
            return rgb(1, 1, 1)
        
        red = self.f(0)
        green = self.f(8)
        blue = self.f(4)
        
        return rgb(red, green, blue)