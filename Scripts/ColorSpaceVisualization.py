# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:46:11 2023

@author: admin
"""

import numpy
from PIL import Image

#from Color_wikipedia import hsl
from Color_standard import hsl
#from Color_math import hsl
#from Color_gamma import hsl

def conv(x):
    return int(255 * x)

def main():
    size = 300
    data = numpy.zeros((size, size, 3), dtype = numpy.uint8)
    for lightness in range(size):
        for hue in range(size):
            col = tuple(map(conv, hsl(hue / size, 1, lightness / size).rgb()))
            data[size - lightness - 1, hue] = [col[0], col[1], col[2]]
    image = Image.fromarray(data)
    #image.save("C:\\Users\\admin\\Pictures\\ColorSpaceVisualization\\wikipedia.png")
    image.save("C:\\Users\\admin\\Pictures\\ColorSpaceVisualization\\standard.png")
    #image.save("C:\\Users\\admin\\Pictures\\ColorSpaceVisualization\\math.png")
    #image.save("C:\\Users\\admin\\Pictures\\ColorSpaceVisualization\\gamma.png")
    image.show()

main()