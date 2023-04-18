import copy
import math

def _validate_instances(data, types):
    for typeName in types:
        choices = types[0]
        result = False
        for choice in choices:
            if isinstance(data, choice):
                result = True
                break
        if result == False:
            return result
        if len(types) > 1:
            subTypes = types[1:]
            for subData in data:
                if not _validate_instances(subData, subTypes):
                    return False
    return True

from math import sin, cos

class matrix():
    
    def rotateNormal(axis, angle, *args, **kwargs):
        #print("axis: ", axis, "angle", angle, "*args", *args, "**kwargs", **kwargs)
        a = angle
        x = axis[0]
        y = axis[1]
        z = axis[2]
        return matrix(
                (
                    ((x * x * (1 - cos(a))) + cos(a),       (x * y * (1 - cos(a))) + (z * sin(a)),  (x * z * (1 - cos(a))) - (y * sin(a))),
                    ((x * y * (1 - cos(a))) - (z * sin(a)), (y * y * (1 - cos(a))) + cos(a),        (y * z * (1 - cos(a))) + (x * sin(a))),
                    ((x * z * (1 - cos(a))) + (y * sin(a)), (y * z * (1 - cos(a))) - (x * sin(a)),  (z * z * (1 - cos(a))) + cos(a)),
                )
            )
    
    def __init__(self, data):
        if not _validate_instances(data, ((list, tuple, vector), (list, tuple, vector), (int, float, complex))):
            raise TypeError("Invalid data input for matrix constructor:\n" + str(data) + " " + str(type(data)) + " " + str(type(data[0])) + " " + str(type(data[0][0])))
        
        #Matrix
        self.data = list(data)
        
        #Die LÄNGE einer Reihe! NICHT die Anzahl der Reihen!
        self.dim_row = len(self.data)
        
        #Die LÄNGE einer Spalte! NICHT die Anzahl der Spalten!
        self.dim_column = len((self.data)[0])
        
        #Make it read-write
        for i in range(self.dim_row):
            (self.data)[i] = list((self.data)[i])
        
        #Validate
        for column in self.data:
            if len(column) != self.dim_column:
                raise Exception("Dimension Error: Not all rows of this matrix have the same length:\n" + str(self))
        
        self.count_row = self.dim_column
        self.count_column = self.dim_row
    
    def __mul__(self, value):
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
            newData = []
            for i in range(self.dim_column):
                column = []
                for j in range(self.dim_row):
                    column.append((((self.data)[i])[j]) * value)
                newData.append(column)
            return matrix(newData)
        elif isinstance(value, matrix):
            if self.dim_row != value.dim_column:
                print(self, "\n", value)
                raise Exception("Error: Attempt to multiply two matrices with non-fitting dimensions. Make sure the Row length of Matrix 0 equals the Column length of Matrix 1.")
            else:
                newData = []
                for i in range(value.count_column):
                    column = []
                    for j in range(self.count_row):
                        column.append(vector((value.column)(i)).dot(vector((self.row)(j))))
                    newData.append(column)
                return matrix(newData)
        elif isinstance(value, vector):
            return vector(((self * value.toMatrix()).column)(0))
        else:
            raise TypeError("Attempt to multiply a matrix with an instance of a non-fitting type (type " + str(type(value)) + ")")
    
    def __add__(self, value):
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
            newData = []
            for i in range(self.dim_column):
                column = []
                for j in range(self.dim_row):
                    column.append((((self.data)[i])[j]) + value)
                newData.append(column)
            return matrix(newData)
        elif isinstance(value, matrix):
            if ((self.dim_row != value.dim_row) or (self.dim_column != value.dim_column)):
                raise Exception("Error: Attempt to add two matrices with non-fitting dimensions.")
            else:
                newData = []
                for i in range(self.dim_column):
                    column = []
                    for j in range(self.dim_row):
                        column.append((((self.data)[i])[j]) + (((value.data)[i])[j]))
                    newData.append(column)
                return matrix(newData)
        elif isinstance(value, vector):
            return vector(((self * value.toMatrix()).column)(0))
        else:
            raise TypeError("Attempt to add a matrix with an instance of a non-fitting type (type " + str(type(value)) + ")")
    
    def __sub__(self, value):
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
            newData = []
            for i in range(self.dim_column):
                column = []
                for j in range(self.dim_row):
                    column.append((((self.data)[i])[j]) - value)
                newData.append(column)
            return matrix(newData)
        elif isinstance(value, matrix):
            if ((self.dim_row != value.dim_row) or (self.dim_column != value.dim_column)):
                raise Exception("Error: Attempt to subtract two matrices with non-fitting dimensions.")
            else:
                newData = []
                for i in range(self.dim_column):
                    column = []
                    for j in range(self.dim_row):
                        column.append((((self.data)[i])[j]) - (((value.data)[i])[j]))
                    newData.append(column)
                return matrix(newData)
        elif isinstance(value, vector):
            return vector(((self * value.toMatrix()).column)(0))
        else:
            raise TypeError("Attempt to subtract a matrix with an instance of a non-fitting type (type " + str(type(value)) + ")")
    
    def __truediv__(self, value):
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
            newData = []
            for i in range(self.dim_column):
                column = []
                for j in range(self.dim_row):
                    column.append((((self.data)[i])[j]) / value)
                newData.append(column)
            return matrix(newData)
        elif isinstance(value, matrix):
            if ((self.dim_row != value.dim_row) or (self.dim_column != value.dim_column)):
                raise Exception("Error: Attempt to divide two matrices with non-fitting dimensions.")
            else:
                newData = []
                for i in range(self.dim_column):
                    column = []
                    for j in range(self.dim_row):
                        column.append((((self.data)[i])[j]) / (((value.data)[i])[j]))
                    newData.append(column)
                return matrix(newData)
        elif isinstance(value, vector):
            return vector(((self * value.toMatrix()).column)(0))
        else:
            raise TypeError("Attempt to divide a matrix with an instance of a non-fitting type (type " + str(type(value)) + ")")
    
    def __floordiv__(self, value):
        if isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
            newData = []
            for i in range(self.dim_column):
                column = []
                for j in range(self.dim_row):
                    column.append((((self.data)[i])[j]) // value)
                newData.append(column)
            return matrix(newData)
        elif isinstance(value, matrix):
            if ((self.dim_row != value.dim_row) or (self.dim_column != value.dim_column)):
                raise Exception("Error: Attempt to divide two matrices with non-fitting dimensions.")
            else:
                newData = []
                for i in range(self.dim_column):
                    column = []
                    for j in range(self.dim_row):
                        column.append((((self.data)[i])[j]) // (((value.data)[i])[j]))
                    newData.append(column)
                return matrix(newData)
        elif isinstance(value, vector):
            return vector(((self * value.toMatrix()).column)(0))
        else:
            raise TypeError("Attempt to divide a matrix with an instance of a non-fitting type (type " + str(type(value)) + ")")
    
    def __str__(self):
        result = ""
        for i in range(self.dim_column):
            row = []
            for column in self.data:
                row.append(column[i])
            result = result + str(row)[1:-1].replace(", ", "	") + "\n"
        result = result[:-1]
        result = "Matrix(\n" + result + ")"
        return result
    
    def __repr__(self):
        return str(self)
    
    def copy(self):
        return copy.deepcopy(self)
        #return matrix(list(self))
    
    #Transponierte Matrix
    def transpose(self):
        data_inverse = []
        for i in range(self.dim_column):
            row = []
            for column in self.data:
                row.append(column[i])
            data_inverse.append(row)
        return matrix(data_inverse)
    
    #Inverse Matrix
    def invert(self):
        newData = []
        det = self.determinant()
        if ((det != 0) and (det != 0.0)):
            for i in range(self.dim_row):
                curr = []
                for j in range(self.dim_column):
                    if (((i + j) % 2) == 0):
                        curr.append(((self.subMatrix(i, j)).determinant()) / det)
                    else:
                        curr.append((0 - 1) * ((self.subMatrix(i, j)).determinant()) / det)
                newData.append(curr)
            return matrix(newData).transpose()
        else:
            raise ZeroDivisionError("Attempt to inverse matrix with determinant of 0!")
    
    def dimension(self):
        return str(self.dim_row) + "x" + str(self.dim_column)
    
    def subMatrix(self, row, column):
        newData = []
        for i in range(self.dim_row):
            if (not (i == row)):
                curr = []
                for j in range(self.dim_column):
                    if (not (j == column)):
                        curr.append(((self.data)[i])[j])
                newData.append(curr)
        return matrix(newData)
    
    def determinant(self):
        if self.dim_row != self.dim_column:
            raise Exception("Attempt to calculate the determinant of a non-quadratic matrix!")
        if self.dim_row == 1:
            return (((self.data)[0])[0])
        else:
            result = 0
            for i in range(self.dim_row):
                if i % 2 == 0:
                    result += ((self.data)[i])[0] * ((self.subMatrix(i, 0)).determinant())
                else:
                    result -= ((self.data)[i])[0] * ((self.subMatrix(i, 0)).determinant())
            return result
    
    def column(self, key):
        return (self.data)[key]
    
    def row(self, key):
        result = []
        for row in self.data:
            result.append(row[key])
        return result

class vector(object):
    def __init__(self, data):
        if not _validate_instances(data, ((list, tuple, vector), (int, float, complex))):
            raise TypeError("Invalid data input for matrix constructor:\n" + str(data))
        
        #Vector
        self.data = list(data)
        
        #Die LÄNGE einer Spalte! NICHT die Anzahl der Spalten!
        self.dim = len(self.data)
    
    def __iter__(self):
        return iter(self.data)
    
    def __next__(self):
        return next(self.data)
    
    def __len__(self):
        return len(self.data)
    
    def length(self):
        res = (self.dot(self)) ** 0.5
        return res
    
    def normalize(self):
        res = self / (self.length())
        return res
    
    def __getitem__(self, key):
        return (((self.data).__getitem__)(key))
    
    def __setitem__(self, key, value):
        return (((self.data).__setitem__)(key, value))
    
    def dot(self, vec):
        if not isinstance(vec, vector):
            raise TypeError("Attempt to multiply vector with non-vector (type " + str(type(vec)) + ")")
        elif self.dim != vec.dim:
            raise Exception("Attempt to execute dot product on two differently-dimensioned vectors.")
        else:
            result = 0
            for i in range(self.dim):
                result += ((self[i]) * (vec[i]))
            return result
    
    def __str__(self):
        return "vector(" + str(self.data)[1:-1] + ")"
    
    def __repr__(self):
        return str(self)
    
    def toMatrix(self):
        return matrix([self.data, ])
    
    def cross(self, vec):
        if not isinstance(vec, vector):
            raise TypeError("Attempt to get cross product of vector with non-vector (type" + str(type(vec)) + ").")
        if ((self.dim != 3) or (vec.dim != 3)):
            raise Exception("Attempt to get cross product of two non-3D vectors (" + str(self) + ", " + str(vec) + ").")
        return vector([((self[1] + vec[2]) - (self[2] * vec[1])), ((self[2] + vec[0]) - (self[0] * vec[2])), ((self[0] + vec[1]) - (self[1] * vec[0]))])
    
    def __mul__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to multiply two differently-dimensioned vectors.")
            else:
                newData = []
                for i in range(self.dim):
                    newData.append(self[i] * value[i])
                return (vector(newData))
        elif isinstance(value, matrix):
            return (self.toMatrix() * value)
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            newData = []
            for i in range(self.dim):
                newData.append(self[i] * value)
            return (vector(newData))
        else:
            raise TypeError("Attempt to multiply vector with instance of type " + str(type(value)) + ".")
    
    def __add__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to add two differently-dimensioned vectors.")
            else:
                newData = []
                for i in range(self.dim):
                    newData.append(self[i] + value[i])
                return (vector(newData))
        elif isinstance(value, matrix):
            return (self.toMatrix() + value)
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            newData = []
            for i in range(self.dim):
                newData.append(self[i] + value)
            return (vector(newData))
        else:
            raise TypeError("Attempt to add vector with instance of type " + str(type(value)) + ".")
    
    def __sub__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to add two differently-dimensioned vectors.")
            else:
                newData = []
                for i in range(self.dim):
                    newData.append(self[i] - value[i])
                return (vector(newData))
        elif isinstance(value, matrix):
            return (self.toMatrix() - value)
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            newData = []
            for i in range(self.dim):
                newData.append(self[i] - value)
            return (vector(newData))
        else:
            raise TypeError("Attempt to add vector with instance of type " + str(type(value)) + ".")
    
    def __truediv__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to add two differently-dimensioned vectors.")
            else:
                newData = []
                for i in range(self.dim):
                    newData.append(self[i] / value[i])
                return (vector(newData))
        elif isinstance(value, matrix):
            return (self.toMatrix() / value)
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            newData = []
            for i in range(self.dim):
                newData.append(self[i] / value)
            return (vector(newData))
        else:
            raise TypeError("Attempt to add vector with instance of type " + str(type(value)) + ".")
    
    def __floordiv__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to add two differently-dimensioned vectors.")
            else:
                newData = []
                for i in range(self.dim):
                    newData.append(self[i] // value[i])
                return (vector(newData))
        elif isinstance(value, matrix):
            return (self.toMatrix() // value)
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            newData = []
            for i in range(self.dim):
                newData.append(self[i] // value)
            return (vector(newData))
        else:
            raise TypeError("Attempt to add vector with instance of type " + str(type(value)) + ".")
        
    def __imul__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to multiply two differently-dimensioned vectors.")
            else:
                for i in range(self.dim):
                    self[i] *= value[i]
                return self
        elif isinstance(value, matrix):
            self = self.toMatrix() * value
            return self
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            for i in range(self.dim):
                self[i] *= value
            return self
        else:
            raise TypeError("Attempt to multiply vector with instance of type " + str(type(value)) + ".")
    
    def __iadd__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to multiply two differently-dimensioned vectors.")
            else:
                for i in range(self.dim):
                    self[i] += value[i]
                return self
        elif isinstance(value, matrix):
            self = self.toMatrix() + value
            return self
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            for i in range(self.dim):
                self[i] += value
            return self
        else:
            raise TypeError("Attempt to multiply vector with instance of type " + str(type(value)) + ".")
    
    def __isub__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to multiply two differently-dimensioned vectors.")
            else:
                for i in range(self.dim):
                    self[i] -= value[i]
                return self
        elif isinstance(value, matrix):
            self = self.toMatrix() - value
            return self
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            for i in range(self.dim):
                self[i] -= value
            return self
        else:
            raise TypeError("Attempt to multiply vector with instance of type " + str(type(value)) + ".")
    
    def __itruediv__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to multiply two differently-dimensioned vectors.")
            else:
                for i in range(self.dim):
                    self[i] /= value[i]
                return self
        elif isinstance(value, matrix):
            self = self.toMatrix() / value
            return self
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            for i in range(self.dim):
                self[i] /= value
            return self
        else:
            raise TypeError("Attempt to multiply vector with instance of type " + str(type(value)) + ".")
    
    def __ifloordiv__(self, value):
        if isinstance(value, vector):
            if not (self.dim == value.dim):
                raise Exception("Attempt to multiply two differently-dimensioned vectors.")
            else:
                for i in range(self.dim):
                    self[i] //= value[i]
                return self
        elif isinstance(value, matrix):
            self = self.toMatrix() // value
            return self
        elif (isinstance(value, int) or isinstance(value, float) or isinstance(value, complex)):
            for i in range(self.dim):
                self[i] //= value
            return self
        else:
            raise TypeError("Attempt to multiply vector with instance of type " + str(type(value)) + ".")
    
    def __abs__(self):
        newData = []
        for i in range(self.dim):
            newData.append(abs(self[i]))
        return (vector(newData))
    
    def angle(self, vec):
        cos_phi = self.dot(vec)
        sin_phi = matrix(((((self.cross)(vec)).normalize)(), self, vec)).determinant()
        res = math.atan2(sin_phi, cos_phi)
        return res

def test():
    mat = matrix(([1, 2, 3], [4, 0, 6], [7, 8, 9]))
    print(mat, "\n")
    print(mat.determinant(), "\n")
    print(mat.invert(), "\n", "\n")
    mat = mat.transpose()
    print(mat, "\n")
    print(mat.determinant(), "\n")
    print(mat.invert(), "\n")
    print(mat.invert().invert(), "\n")
    
    x = vector([1, 1, 0])
    print(x)
    y = vector([1, 1, 2])
    print(y)
    print("DOT: ", x.dot(y))
    print("CROSS: ", x.cross(y))
    print("MUL: ", x * y)
    print("MUL2: ", x * 2)
    print("MULy: ", y * y)
    print("mat:\n", mat, "\nvec:\n", x, "\nprod:\n", mat * x)
    print("\n\n", mat, "\n\n", mat * mat)
    print((x + y) * y // 2)

        