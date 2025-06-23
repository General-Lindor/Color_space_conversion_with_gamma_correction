# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:51:22 2023

@author: admin
"""

#HYBRID - Combines formula consistency advantage of mathematical model for lightness and saturation with computational speed advantage for hue calculation of standard model

from Scripts.vectors import matrix, vector
import math

class rgb(vector):
    
    def __init__(self, r, g, b):
        super(rgb, self).__init__((r, g, b))
    
    def hsl(self):
        lightness = (self[0] + self[1] + self[2]) / 3
        
        if lightness < 0.001:
            return hsl(0, 0, 0)
        elif lightness > 0.999:
            return hsl(0, 0, 1)
        
        s_0 = 1 - (min(self) / lightness)
        s_1 = (max(self) - lightness) / (1 - lightness)
        saturation = max(s_0, s_1)
        
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
        
        def getVals(FAC):
            nonlocal lightness
            nonlocal saturation
            
            if ((FAC + 1) > (3 * lightness)):
                
                MIN = (1 - saturation) * lightness
                MAX = ((3 * lightness) - ((2 - FAC) * MIN)) / (1 + FAC)
                MID = (FAC * (MAX - MIN)) + MIN
                
            else:
                
                MAX = (saturation * (1 - lightness)) + lightness
                MIN = ((3 * lightness) - ((1 + FAC) * MAX)) / (2 - FAC)
                MID = (FAC * (MAX - MIN)) + MIN
                
            return MIN, MID, MAX
        
        #   new                     = (old - MIN) / (MAX - MIN)
        #=> new * (MAX - MIN) + MIN = old
        #=> old = new * (MAX - MIN) + MIN
        
        if (hue < (1 / 6)):
            
            #1x0
            FAC = (hue - 0) * 6
            MIN, MID, MAX = getVals(FAC)
            
            red = MAX
            green = MID
            blue = MIN
            
        elif (hue < (2 / 6)):
            
            #x10
            FAC = ((1 / 3) - hue) * 6
            MIN, MID, MAX = getVals(FAC)
            
            red = MID
            green = MAX
            blue = MIN
            
        elif (hue < (3 / 6)):
            
            #01x
            FAC = (hue - (1 / 3)) * 6
            MIN, MID, MAX = getVals(FAC)
            
            red = MIN
            green = MAX
            blue = MID
            
        elif (hue < (4 / 6)):
            
            #0x1
            FAC = ((2 / 3) - hue) * 6
            MIN, MID, MAX = getVals(FAC)
            
            red = MIN
            green = MID
            blue = MAX
            
        elif (hue < (5 / 6)):
            
            #x01
            FAC = (hue - (2 / 3)) * 6
            MIN, MID, MAX = getVals(FAC)
            
            red = MID
            green = MIN
            blue = MAX
            
        else:
            
            #10x
            FAC = (1 - hue) * 6
            MIN, MID, MAX = getVals(FAC)
            
            red = MAX
            green = MIN
            blue = MID
        
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