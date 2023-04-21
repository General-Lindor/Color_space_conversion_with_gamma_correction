# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 09:43:47 2023

@author: admin
"""

#IMPROVED STANDARD RGB-HSL MODEL

from Scripts.vectors import matrix, vector
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
        try:
            cs = self - min(self)
            cs /= max(cs)
            idx = min((val, idx) for (idx, val) in enumerate(cs))[1]
            if idx == 0:
                if cs[1] < cs[2]:
                    #0x1
                    hue = (2 / 3) - (cs[1] / 6)
                else:
                    #01x
                    hue = (1 / 3) + (cs[2] / 6)
            elif idx == 1:
                if cs[0] < cs[2]:
                    #x01
                    hue = (2 / 3) + (cs[0] / 6)
                else:
                    #10x
                    hue = 1 - (cs[2] / 6)
            elif idx == 2:
                if cs[0] < cs[1]:
                    #x10
                    hue = (1 / 3) - (cs[0] / 6)
                else:
                    #1x0
                    hue = 0 + (cs[1] / 6)
            else:
                raise Exception("minColorError")
            if hue >= 1:
                hue = 0
        except:
            hue = 0.5
        
        return hsl(hue, saturation, lightness)

class hsl(vector):
    def __init__(self, r, g, b):
        super(hsl, self).__init__((r, g, b))
    
    def rgb(self):
        
        hue = self[0]
        saturation = self[1]
        lightness = self[2]
        
        if lightness < 0.001:
            return rgb(0, 0, 0)
        elif lightness > 0.999:
            return rgb(1, 1, 1)
        
        if lightness >= 0.5:
            MIN = lightness + (lightness * saturation) - saturation
            MAX = lightness - (lightness * saturation) + saturation
        else:
            MIN = lightness - (lightness * saturation)
            MAX = lightness + (lightness * saturation)
        
        #   new                     = (old - MIN) / (MAX - MIN)
        #=> new * (MAX - MIN) + MIN = old
        #=> old = new * (MAX - MIN) + MIN
        
        if (hue < (1 / 6)):
            #1x0
            red = MAX
            green = ((hue - 0) * 6 * (MAX - MIN)) + MIN
            blue = MIN
        elif (hue < (2 / 6)):
            #x10
            red = (((1 / 3) - hue) * 6 * (MAX - MIN)) + MIN
            green = MAX
            blue = MIN
        elif (hue < (3 / 6)):
            #01x
            red = MIN
            green = MAX
            blue = ((hue - (1 / 3)) * 6 * (MAX - MIN)) + MIN
        elif (hue < (4 / 6)):
            #0x1
            red = MIN
            green = (((2 / 3) - hue) * 6 * (MAX - MIN)) + MIN
            blue = MAX
        elif (hue < (5 / 6)):
            #x01
            red = ((hue - (2 / 3)) * 6 * (MAX - MIN)) + MIN
            green = MIN
            blue = MAX
        else:
            #10x
            red = MAX
            green = MIN
            blue = ((1 - hue) * 6 * (MAX - MIN)) + MIN
        
        return rgb(red, green, blue)