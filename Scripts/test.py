#from Color_wikipedia import rgb, hsl
#from Color_standard import rgb, hsl
#from Color_math import rgb, hsl
#from Color_gamma import rgb, hsl
#from Color_hybrid import rgb, hsl
from Color_hybridGamma import rgb, hsl

def test(r, g, b):
    print("")
    x = rgb(r, g, b)
    print("Color BEFORE: ", str(tuple(x.data)))
    y = x.hsl()
    print("Color HSL:    ", str(tuple(y.data)))
    y = y.rgb()
    print("Color AFTER:  ", str(tuple(y.data)))
    err = (abs((y - x) / vector((max(x[0], 1 - x[0]), max(x[1], 1 - x[1]), max(x[2], 1 - x[2])))).dot(vector((1, 1, 1)))) * 100
    print("Percentage Total Error: " + repr(err) + "%")
    err = (abs(y.angle(x)) / (2 * math.pi)) * 100
    print("Percentage Angle Error: " + repr(err) + "%")
    err = (abs(y.length() - x.length()) / x.length()) * 100
    print("Percentage Length Error: " + repr(err) + "%")

#COLORS
test(1, 0, 0)
test(1, 1, 0)
test(0, 1, 0)
test(0, 1, 1)
test(0, 0, 1)
test(1, 0, 1)

#BLACK & WHITE
#Crash due to division by 0
#test(0, 0, 0)
test(1, 1, 1)

#RANDOM
test(0.2, 0.6, 0.75)
test(0.2, 0.7, 1)
test(0.2, 0.5, 0.75)
test(0.252, 0.265, 0.462372355)
test(0.39369, 0.9733, 0.6373)