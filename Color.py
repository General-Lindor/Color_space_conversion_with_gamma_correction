# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 09:43:47 2023

@author: admin
"""

#IMPROVED STANDARD RGB-HSL MODEL

from Scripts.vectors import matrix, vector
import math

def dmax(a, b):
    if a > b:
        return a
    else:
        return b

def dmin(a, b):
    if a < b:
        return a
    else:
        return b

class rgb(vector):
    
    vRed = 0.2126
    vGreen = 0.7152
    vBlue = 0.0722
    
    #vRed = 1 / 3
    #vGreen = 1 / 3
    #vBlue = 1 / 3
    
    def __init__(self, r, g, b):
        super(rgb, self).__init__((r, g, b))
    
    def hsl(self):
        
        red = self[0]
        green = self[1]
        blue = self[2]
        
        lightness = (red + green + blue) / 3
        
        MAX = max(self)
        MIN = min(self)
        
        #if lightness < (lightness * MAX) + ((1 - lightness) * MIN):
        
        #sat_0 = (MAX - lightness) / (1 - lightness)
        #sat_1 = (lightness - MIN) / lightness
        #saturation = dmax(sat_0, sat_1y
        
        if lightness > 0.5:
            saturation = (MAX - lightness) / (1 - lightness)
        else:
            saturation = (lightness - MIN) / lightness
        
        if red > green:
            if green > blue:
                # red > green > blue
                var = (green - blue) / (red - blue)
                hue = (0 + var) / 6
            else:
                if red > blue:
                    # red > blue > green
                    var = (blue - green) / (red - green)
                    hue = (6 - var) / 6
                else:
                    # blue > red > green
                    var = (red - green) / (blue - green)
                    hue = (4 + var) / 6
        else:
            if red > blue:
                # green > red > blue
                var = (red - blue) / (green - blue)
                hue = (2 - var) / 6
            else:
                if green > blue:
                    # green > blue > red
                    var = (blue - red) / (green - red)
                    hue = (2 + var) / 6
                else:
                    # blue > green > red
                    var = (green - red) / (blue - red)
                    hue = (4 - var) / 6
        
        return hsl(hue, saturation, lightness)

class hsl(vector):
    def __init__(self, h, s, l):
        super(hsl, self).__init__((h, s, l))
    
    def rgb(self):
        
        hue = self[0]
        saturation = self[1]
        lightness = self[2]
        
        bigHue = 6 * hue
        
        if (bigHue < 1):
            # red > green > blue
            effectiveHue = bigHue
            a = rgb.vRed
            b = rgb.vGreen
            c = rgb.vBlue
        elif (bigHue < 2):
            # green > red > blue
            effectiveHue = 2 - bigHue
            a = rgb.vGreen
            b = rgb.vRed
            c = rgb.vBlue
        elif (bigHue < 3):
            # green > blue > red
            effectiveHue = bigHue - 2
            a = rgb.vGreen
            b = rgb.vBlue
            c = rgb.vRed
        elif (bigHue < 4):
            # blue > green > red
            effectiveHue = 4 - bigHue
            a = rgb.vBlue
            b = rgb.vGreen
            c = rgb.vRed
        elif (bigHue < 5):
            # blue > red > green
            effectiveHue = bigHue - 4
            a = rgb.vBlue
            b = rgb.vRed
            c = rgb.vGreen
        else:
            # red > blue > green
            effectiveHue = 6 - bigHue
            a = rgb.vRed
            b = rgb.vBlue
            c = rgb.vGreen
        
        if lightness < (b * effectiveHue) + c:
            MIN = (1 - saturation) * lightness
            MAX = ((((1 - a) + (a * saturation)) * lightness) - ((1 - effectiveHue) * b * MIN)) / ((b * effectiveHue) + c)
            MID = ((((1 - a) + (a * saturation)) * lightness) - (c * MAX)) / b
        else:
            MAX = lightness - (saturation * (lightness - 1))
            MIN = (lightness - (MAX * ((b * effectiveHue) + c))) / (a + ((1 - effectiveHue) * b))
            MID = ((lightness - (c * MAX)) - (a * MIN)) / b
        
        '''
        if lightness < (b * effectiveHue) + c:
            MAX = (((a * saturation) - (b * (1 - effectiveHue) * (1 - saturation))) * lightness) / (a * (effectiveHue + c))
            MID = ((saturation * lightness) - (c * MAX)) / b
            MIN = ((1 - saturation) * lightness) / a
        else:
            MIN = ((((lightness - saturation) * c) - b) + ((lightness - c) * b * effectiveHue * saturation)) / (c * ((1 + a) - effectiveHue))
            MID = (((lightness - c) * saturation) - (a * MIN)) / b
            MAX = (((1 - saturation) * lightness) / c) + saturation
        '''
        
        '''
        if lightness < (effectiveHue + 1) * c:
            CMAX = (((2 - effectiveHue) * saturation) + (effectiveHue - 1)) * (lightness / (effectiveHue + 1))
            BMID = (saturation * lightness) - CMAX
            AMIN = (1 - saturation) * lightness
        else:
            AMIN = (((1 + effectiveHue) * saturation * (lightness - c)) - (effectiveHue * lightness)) / (2 - effectiveHue)
            BMID = (saturation * (lightness - c)) - AMIN
            CMAX = lightness - (saturation * (lightness - c))
        MIN = AMIN / a
        MID = BMID / b
        MAX = CMAX / c
        '''
        
        if (bigHue < 1):
            # red > green > blue
            red = MAX
            green = MID
            blue = MIN
        elif (bigHue < 2):
            # green > red > blue
            red = MID
            green = MAX
            blue = MIN
        elif (bigHue < 3):
            # green > blue > red
            red = MIN
            green = MAX
            blue = MID
        elif (bigHue < 4):
            # blue > green > red
            red = MIN
            green = MID
            blue = MAX
        elif (bigHue < 5):
            # blue > red > green
            red = MID
            green = MIN
            blue = MAX
        else:
            # red > blue > green
            red = MAX
            green = MIN
            blue = MID
        
        return rgb(red, green, blue)

'''
class expect():
    def __init__(self, h, s, l):
        self.h = h
        self.s = s
        self.l = l
        self.c = rgb(0, 0, 0)
        self.e = 3
    
    def rep(self, crgb, chsl):
        e = abs(self.h - chsl[0]) + abs(self.s - chsl[1]) + abs(self.l - chsl[2])
        if e < self.e:
            self.c = crgb
'''

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
    
    '''
    print("Building...")
    hashMap = {}
    for lightness in range(size):
        l = lightness / size
        t = {}
        hashMap[l] = t
        for hue in range(size):
            h = hue / size
            q = expect(h, 1, l)
            t[h] = q
        hashMap[l] = t
    
    print("Sorting...")
    for red in range(size):
        print(red)
        for green in range(size):
            print(green)
            for blue in range(size):
                col = rgb(red / size, green / size, blue / size)
                colhsl = col.hsl()
                for t in hashMap.values():
                    for q in t.values():
                        q.rep(col, colhsl)
    
    print("Generating...")
    for litem in hashMap.items():
        lightness = litem[0]
        t = litem[1]
        for qitem in t.items():
            hue = qitem[0]
            q = qitem[1]
            col = tuple(map(conv, q.c))
            data[size - lightness - 1, hue] = [col[0], col[1], col[2]]
    '''
    
    image = Image.fromarray(data)
    image.show()
    print("Done!")