from vectors import matrix, vector
import math

class rgb(vector):
    
    #gamma correction:
    a = 0.2126
    b = 0.7152
    c = 0.0722
    
    #standard model without gamma correction:
    #a = 0.3333333
    #b = 0.3333334
    #c = 0.3333333
    
    n = vector((a, b, c))
    normal = n.normalize()
    s_red = vector((1 - a, 0 - a, 0 - a))
    
    def __init__(self, r, g, b):
        super(rgb, self).__init__((r, g, b))
    
    def hsl(self):
        lightness = self.dot(rgb.n)
        
        if lightness < 0.001:
            return hsl(0, 0, 0)
        elif lightness > 0.999:
            return hsl(0, 0, 1)
        
        s_0 = 1 - (min(self) / lightness)
        s_1 = (max(self) - lightness) / (1 - lightness)
        
        #we search for the smallest value of (s_0, s_1) that is greater than 0
        if s_0 > 0:
            if s_1 > 0:
                saturation = min(s_0, s_1)
            else:
                saturation = s_0
        elif s_1 > 0:
            saturation = s_1
        else:
            #this should never happen, but just in case...
            saturation = max(s_0, s_1)
        
        l_vec = vector((lightness, lightness, lightness))
        s_vec = self - l_vec
        
        cos_phi = s_vec.dot(rgb.s_red)
        sin_phi = matrix((rgb.normal, rgb.s_red, s_vec)).determinant()
        
        hue = math.atan2(sin_phi, cos_phi) / (2 * math.pi)
        if hue < 0:
            hue += 1
        
        return hsl(hue, saturation, lightness)

class hsl(vector):
    
    a = rgb.a
    b = rgb.b
    c = rgb.c
    
    n = rgb.n
    normal = rgb.normal
    s_red = rgb.s_red
    
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
        
        rotMat = matrix.rotateNormal(axis = hsl.normal, angle = hue * 2 * math.pi)
        s_vec_wrong_length =  rotMat * hsl.s_red
        
        possible_vals = []
        for param in s_vec_wrong_length:
            if param < 0:
                val_0 = (0 - lightness) / param
                possible_vals.append(val_0)
            elif param > 0:
                val_1 = (1 - lightness) / param
                possible_vals.append(val_1)
        val = min(possible_vals)
        
        s_vec = s_vec_wrong_length * val * saturation
        l_vec = vector((lightness, lightness, lightness))
        result = l_vec + s_vec
        
        red = result[0]
        green = result[1]
        blue = result[2]
        
        return rgb(red, green, blue)

def test(r, g, b):
    print("")
    x = rgb(r, g, b)
    y = x.hsl().rgb()
    print("Color: ", str((r, g, b)))
    err = (abs((y - x) / vector((max(x[0], 1 - x[0]), max(x[1], 1 - x[1]), max(x[2], 1 - x[2])))).dot(vector((1, 1, 1)))) * 100
    print("Percentage Total Error: " + repr(err) + "%")
    err = (abs(y.angle(x)) / (2 * math.pi)) * 100
    print("Percentage Angle Error: " + repr(err) + "%")
    err = (abs(y.length() - x.length()) / x.length()) * 100
    print("Percentage Length Error: " + repr(err) + "%")

#test(0, 0, 0)
test(1, 0, 0)
test(0, 1, 0)
test(1, 1, 0)
test(0, 0, 1)
test(1, 0, 1)
test(0, 1, 1)
test(1, 1, 1)