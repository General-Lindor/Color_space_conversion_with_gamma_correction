# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 09:49:11 2023

@author: admin
"""
from Scripts.vectors import matrix, vector
import math
import time

#from Color_wikipedia import rgb, hsl
from Color_standard import rgb, hsl
#from Color_math import rgb, hsl
#from Color_gamma import rgb, hsl
#from Color_hybrid import rgb, hsl
#from Color_hybridGamma import rgb, hsl

def test(r, g, b):
    print("")
    try:
        x = rgb(r, g, b)
        print("Color BEFORE: ", repr(tuple(x.data)))
    except Exception as e:
        print(repr(e))
    try:
        y = x.hsl()
        print("Color HSL:    ", repr(tuple(y.data)))
    except Exception as e:
        print(repr(e))
    try:
        y = y.rgb()
        print("Color AFTER:  ", repr(tuple(y.data)))
    except Exception as e:
        print(repr(e))
    try:
        err = (abs((y - x) / vector((max(x[0], 1 - x[0]), max(x[1], 1 - x[1]), max(x[2], 1 - x[2])))).dot(vector((1, 1, 1)))) * 100
        print("Percentage Total Error: " + repr(err) + "%")
    except Exception as e:
        print(repr(e))
    try:
        err = (abs(y.angle(x)) / (2 * math.pi)) * 100
        print("Percentage Angle Error: " + repr(err) + "%")
    except Exception as e:
        print(repr(e))
    try:
        err = (abs(y.length() - x.length()) / x.length()) * 100
        print("Percentage Length Error: " + repr(err) + "%")
    except Exception as e:
        print(repr(e))

#BLACK & WHITE
def BnW():
    #BLACK Crash due to division by 0
    test(0, 0, 0)
    test(1, 1, 1)

#COLORS
def COL():
    test(1, 0, 0)
    test(1, 1, 0)
    test(0, 1, 0)
    test(0, 1, 1)
    test(0, 0, 1)
    test(1, 0, 1)

#RANDOM
def RND():
    test(0.2, 0.6, 0.75)
    test(0.2, 0.7, 1)
    test(0.2, 0.5, 0.75)
    test(0.252, 0.265, 0.462372355)
    test(0.39369, 0.9733, 0.6373)

#GREY
def grey():
    for a in range(10):
        test((a + 1) / 10, (a + 1) / 10, (a + 1) / 10)

#BENCHMARK
def benchmark(size):
    print("")
    x = time.time()
    for a in range(size):
        for b in range(size):
            for c in range(size):
                if min(a, b, c) == max(a, b, c):
                    print("Benchmark " + str(a) + "% complete")
                try:
                    ((((rgb((a / size), (b / size), (c / size))).hsl)()).rgb)()
                except Exception as e:
                    print("ERROR: ", a, b, c)
                    print(repr(e))
    print("\nConverting " + str(size * size * size) + " colors from RGB to HSL and back to RGB took " + str(time.time() - x) + " seconds with the current model.")

BnW()
COL()
RND()
grey()
benchmark(100)