# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 14:46:11 2023

@author: admin
"""

import numpy
from PIL import Image

import Color_wikipedia
import Color_standard
import Color_hybrid
import Color_hybridGamma
import Color_night
import Color_math
import Color_gamma

def conv(x):
    return int(255 * x)

def main(hsl, name, last = False):
    size = 300
    data = numpy.zeros((size, size, 3), dtype = numpy.uint8)
    for lightness in range(size):
        for hue in range(size):
            col = tuple(map(conv, hsl(hue / size, 1, lightness / size).rgb()))
            data[size - lightness - 1, hue] = [col[0], col[1], col[2]]
    image = Image.fromarray(data)
    image.save("C:\\Users\\Jean-Luc Picard\\Pictures\\ColorSpaceVisualization\\" + name + ".png")
    image.show()
    print(name + " done.")

main(Color_wikipedia.hsl, "wikipedia")
main(Color_standard.hsl, "standard")
main(Color_hybrid.hsl, "hybrid")
main(Color_hybridGamma.hsl, "hybridGamma")
main(Color_night.hsl, "night")
main(Color_math.hsl, "math")
main(Color_gamma.hsl, "gamma", True)

input("finished")