from Scripts.vectors import matrix, vector
import math

def lstr(e):
    x = str(e)
    y = repr(e)
    if len(x) > len(y):
        return x
    else:
        return y

def lprint(e):
    print(lstr(e))

def validate(val, name):
    if (not (isinstance(val, int) or isinstance(val, float))):
        raise TypeError(name + " must be float or int but is " + lstr(type(val)))
    if val < 0:
        raise ValueError(name + " must be greater than or equal to zero.")
    if val > 1:
        raise ValueError(name + " must be smaller than or equal to one.")

asixth = 1 / 6
athird = 1 / 3
ahalf = 1 / 2
twothirds = 2 / 3
fivesixths = 5 / 6

class rgb(vector):
    def __init__(self, r, g, b):
        validate(r, "Red")
        validate(g, "Green")
        validate(b, "Blue")
        super(rgb, self).__init__((r, g, b))
        #self.r = r
        #self.g = g
        #self.b = b
    
    def hsv(self):
        
        red = self[0]
        green = self[1]
        blue = self[2]
        
        if red > green:
            if green > blue:
                # red > green > blue
                MIN = blue
                MID = green
                MAX = red
                effectiveHue = (MID - MIN) / (MAX - MIN)
                hue = (0 + effectiveHue) / 6
            else:
                if red > blue:
                    # red > blue > green
                    MIN = green
                    MID = blue
                    MAX = red
                    effectiveHue = (MID - MIN) / (MAX - MIN)
                    hue = (6 - effectiveHue) / 6
                else:
                    # blue > red > green
                    MIN = green
                    MID = red
                    MAX = blue
                    effectiveHue = (MID - MIN) / (MAX - MIN)
                    hue = (4 + effectiveHue) / 6
        else:
            if red > blue:
                # green > red > blue
                MIN = blue
                MID = red
                MAX = green
                effectiveHue = (MID - MIN) / (MAX - MIN)
                hue = (2 - effectiveHue) / 6
            else:
                if green > blue:
                    # green > blue > red
                    MIN = red
                    MID = blue
                    MAX = green
                    effectiveHue = (MID - MIN) / (MAX - MIN)
                    hue = (2 + effectiveHue) / 6
                else:
                    # blue > green > red
                    MIN = red
                    MID = green
                    MAX = blue
                    effectiveHue = (MID - MIN) / (MAX - MIN)
                    hue = (4 - effectiveHue) / 6
        
        saturation = MAX - MIN
        value = MAX
        
        return hsl(hue, saturation, lightness)
    
    def hsv(self):
        return self.hsv().hsl()
    
    def isclose(self, other):
        if (math.isclose(self[0], other[0]) and math.isclose(self[1], other[1]) and math.isclose(self[2], other[2])):
            return True
        return False

class hsv(vector):
    def __init__(self, h, s, v):
        validate(h, "Hue")
        validate(s, "Saturation")
        validate(v, "Value")
        super(hsv, self).__init__((h, s, v))
        #self.h = h
        #self.s = s
        #self.v = v
    
    def rgb(self):
        
        hue = self[0]
        saturation = self[1]
        value = self[2]
        
        MAX = value
        MIN = MAX - saturation
        
        bigHue = 6 * hue
        
        if (bigHue < 1):
            # red > green > blue
            effectiveHue = bigHue
            MID = saturation * effectiveHue + MIN
            red = MIN
            green = MID
            blue = MAX
        elif (bigHue < 2):
            # green > red > blue
            effectiveHue = 2 - bigHue
            MID = saturation * effectiveHue + MIN
            green = MIN
            red = MID
            blue = MAX
        elif (bigHue < 3):
            # green > blue > red
            effectiveHue = bigHue - 2
            MID = saturation * effectiveHue + MIN
            green = MIN
            blue = MID
            red = MAX
        elif (bigHue < 4):
            # blue > green > red
            effectiveHue = 4 - bigHue
            MID = saturation * effectiveHue + MIN
            blue = MIN
            green = MID
            red = MAX
        elif (bigHue < 5):
            # blue > red > green
            effectiveHue = bigHue - 4
            MID = saturation * effectiveHue + MIN
            blue = MIN
            red = MID
            green = MAX
        else:
            # red > blue > green
            effectiveHue = 6 - bigHue
            MID = saturation * effectiveHue + MIN
            red = MIN
            blue = MID
            green = MAX
        
        red = red % 1
        green = green % 1
        blue = blue % 1
        
        return rgb(red, green, blue)
    
    def hsl(self):
        l = self[2] * (1 - (self[1] * 0.5))
        if math.isclose(self[1], 0):
            return hsl(self[0], 0, l)
        if l < 0.5:
            s = (self[1]) / (2 - self[1])
            return hsl(self[0], s, l)
        else:
            s = (self[1] * self[2]) / ((2 - (2 * self[2])) + (self[1] * self[2]))
            return hsl(self[0], s, l)
    
    def isclose(self, other):
        if (math.isclose(self[0], other[0]) and math.isclose(self[1], other[1]) and math.isclose(self[2], other[2])):
            return True
        return False

class hsl(vector):
    def __init__(self, h, s, l):
        validate(h, "Hue")
        validate(s, "Saturation")
        validate(l, "Lightness")
        super(hsl, self).__init__((h, s, l))
        #self.h = h
        #self.s = s
        #self.l = l
    
    def rgb(self):
        return self.hsv().rgb()
    
    def hsv(self):
        if self[2] < 0.5:
            t = (1 + self[1])
            s = (2 * self[1]) / t
            v = t * self[2]
            return hsv(self[0], s, v)
        else:
            t = (self[1] - (self[1] * self[2])) + self[2]
            s = 2 * (1 - (self[2] / t))
            v = t
            return hsv(self[0], s, v)
    
    def isclose(self, other):
        if (math.isclose(self[0], other[0]) and math.isclose(self[1], other[1]) and math.isclose(self[2], other[2])):
            return True
        return False

def test():
    testvals = [0, 0.25, 0.3333333333, 0.5, 0.6666666666, 0.75, 1]
    success = True
    for r in testvals:
        for g in testvals:
            for b in testvals:
                partialsuccess = True
                x1 = rgb(r, g, b)
                y1 = x1.hsv()
                z1 = x1.hsl()
                x2 = y1.rgb()
                z2 = y1.hsl()
                x3 = z1.rgb()
                y2 = z1.hsv()
                if not (x1.isclose(x2) and x2.isclose(x3) and x3.isclose(x1)):
                    print(x1, x2, x3, "x")
                    partialsuccess = False
                    succcess = False
                if not (y1.isclose(y2)):
                    print(y1, y2, "y")
                    partialsuccess = False
                    succcess = False
                if not (z1.isclose(z2)):
                    print(z1, z2, "z")
                    partialsuccess = False
                    succcess = False
                if not partialsuccess:
                    print("")
    if success:
        input("Congratz! Your model passed the test, most likely it works!")
    else:
        input("There are issues with your model, it didn't pass the test!")

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
#test()
"""
lprint(hsl(0.25, 1, 0.5))
lprint(hsl(0.25, 1, 0.5).torgb())
lprint(hsv(0.25, 1, 1))
lprint(hsv(0.25, 1, 1).torgb())

lprint(hsl(0.25, 0.75, 0.5))
lprint(hsl(0.25, 0.75, 0.5).torgb())
lprint(hsv(0.25, 0.75, 1))
lprint(hsv(0.25, 0.75, 1).torgb())
"""