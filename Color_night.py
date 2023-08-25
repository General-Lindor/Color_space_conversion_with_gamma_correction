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
        if self[0] > self[1]:
            if self[1] > self[2]:
                maxval = self[0]
                if math.isclose(maxval, 0):
                    return hsv(0, 0, 0)
                midval = self[1]
                minval = self[2]
                d = maxval - minval
                if math.isclose(d, 0):
                    h = 0
                else:
                    h = (midval - minval) / (d * 6)
            elif self[2] > self[0]:
                maxval = self[2]
                if math.isclose(maxval, 0):
                    return hsv(0, 0, 0)
                midval = self[0]
                minval = self[1]
                d = maxval - minval
                if math.isclose(d, 0):
                    h = 0
                else:
                    h = twothirds + ((midval - minval) / (d * 6))
            else:
                maxval = self[0]
                if math.isclose(maxval, 0):
                    return hsv(0, 0, 0)
                midval = self[2]
                minval = self[1]
                d = maxval - minval
                if math.isclose(d, 0):
                    h = 0
                else:
                    h = fivesixths + ((maxval - midval) / (d * 6))
        else:
            if self[2] > self[1]:
                maxval = self[2]
                if math.isclose(maxval, 0):
                    return hsv(0, 0, 0)
                midval = self[1]
                minval = self[0]
                d = maxval - minval
                if math.isclose(d, 0):
                    h = 0
                else:
                    h = ahalf + ((maxval - midval) / (d * 6))
            elif self[2] > self[0]:
                maxval = self[1]
                if math.isclose(maxval, 0):
                    return hsv(0, 0, 0)
                midval = self[2]
                minval = self[0]
                d = maxval - minval
                if math.isclose(d, 0):
                    h = 0
                else:
                    h = athird + ((midval - minval) / (d * 6))
            else:
                maxval = self[1]
                if math.isclose(maxval, 0):
                    return hsv(0, 0, 0)
                midval = self[0]
                minval = self[2]
                d = maxval - minval
                if math.isclose(d, 0):
                    h = 0
                else:
                    h = asixth + ((maxval - midval) / (d * 6))
        s = d / maxval
        v = maxval
        return hsv(h, s, v)
    
    def hsl(self):
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
        maxval = self[2]
        minval = maxval * (1 - self[1])
        if self[0] >= fivesixths:
            midval = maxval - (((6 * self[0]) - 5) * (maxval - minval))
            return rgb(maxval, minval, midval)
        elif self[0] >= twothirds:
            midval = minval + (((6 * self[0]) - 4) * (maxval - minval))
            return rgb(midval, minval, maxval)
        elif self[0] >= ahalf:
            midval = maxval - (((6 * self[0]) - 3) * (maxval - minval))
            return rgb(minval, midval, maxval)
        elif self[0] >= athird:
            midval = minval + (((6 * self[0]) - 2) * (maxval - minval))
            return rgb(minval, maxval, midval)
        elif self[0] >= asixth:
            midval = maxval - (((6 * self[0]) - 1) * (maxval - minval))
            return rgb(midval, maxval, minval)
        else:
            midval = minval + (6 * self[0] * (maxval - minval))
            return rgb(maxval, midval, minval)
    
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