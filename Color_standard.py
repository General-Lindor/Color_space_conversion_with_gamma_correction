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
        #saturation = (MAX - MIN) / (1 - abs(MAX + MIN - 1))
        if lightness > 0.5:
            saturation = (MAX - MIN) / (2 * (1 - lightness))
        else:
            saturation = (MAX - MIN) / (2 * lightness)
        
        #HUE
        try:
            cs = self - min(self)
            cs /= max(cs)
            idx = min((val, idx) for (idx, val) in enumerate(cs))[1]
            if idx == 0:
                if cs[1] < cs[2]:
                    #0x1
                    hue = (4 - cs[1]) / 6
                else:
                    #01x
                    hue = (2 + cs[2]) / 6
            elif idx == 1:
                if cs[0] < cs[2]:
                    #x01
                    hue = (4 + cs[0]) / 6
                else:
                    #10x
                    hue = (6 - cs[2]) / 6
            elif idx == 2:
                if cs[0] < cs[1]:
                    #x10
                    hue = (2 - cs[0]) / 6
                else:
                    #1x0
                    hue = (0 + cs[1]) / 6
            else:
                raise Exception("minColorError")
        except:
            hue = 0.5
            
        hue = hue % 1
        saturation = saturation % 1
        lightness = lightness % 1
        
        return hsl(hue, saturation, lightness)

class hsl(vector):
    def __init__(self, r, g, b):
        super(hsl, self).__init__((r, g, b))
    
    def rgb(self):
        
        hue = self[0]
        saturation = self[1]
        lightness = self[2]
        
        bigHue = hue * 6
        
        if lightness > 0.5:
            MIN = lightness + (lightness * saturation) - saturation
            MAX = lightness - (lightness * saturation) + saturation
        else:
            MIN = lightness - (lightness * saturation)
            MAX = lightness + (lightness * saturation)
        
        #   hue               = (MID - MIN) / (MAX - MIN)
        #=> hue * (MAX - MIN) = MID - MIN
        #=> MID               = hue * (MAX - MIN) + MIN
        
        if (bigHue < 1):
            #1x0
            red = MAX
            green = ((bigHue - 0) * (MAX - MIN)) + MIN
            blue = MIN
        elif (bigHue < 2):
            #x10
            red = ((2 - bigHue) * (MAX - MIN)) + MIN
            green = MAX
            blue = MIN
        elif (bigHue < 3):
            #01x
            red = MIN
            green = MAX
            blue = ((bigHue - 2) * (MAX - MIN)) + MIN
        elif (bigHue < 4):
            #0x1
            red = MIN
            green = ((4 - bigHue) * (MAX - MIN)) + MIN
            blue = MAX
        elif (bigHue < 5):
            #x01
            red = ((bigHue - 4) * (MAX - MIN)) + MIN
            green = MIN
            blue = MAX
        else:
            #10x
            red = MAX
            green = MIN
            blue = ((6 - bigHue) * (MAX - MIN)) + MIN
        
        return rgb(red, green, blue)

if __name__ == "__main__":
    import numpy
    from PIL import Image

    def conv(x):
        return int(255 * x)
    
    size = 300
    data = numpy.zeros((size, size, 3), dtype = numpy.uint8)
    for lightness in range(size):
        for hue in range(size):
            col = tuple(map(conv, hsl(hue / size, 1, lightness / size).rgb()))
            data[size - lightness - 1, hue] = [col[0], col[1], col[2]]
    image = Image.fromarray(data)
    image.show()
    print("Done!")