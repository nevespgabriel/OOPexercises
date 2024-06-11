from math import sqrt, pow
from functools import total_ordering

@total_ordering
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def tyer(obj):
        if not isinstance(obj, Vector):
            raise TypeError("The instance is not a Vector!!")

    def __repr__(self):
        return f'Vector(x = {self.x}, y = {self.y}, z = {self.z})'

    def __abs__(self):
        return abs(sqrt((pow(self.x,2) + pow(self.y,2) + pow(self.z,2))))

    def __add__(self, other):
        self.tyer(other)
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        if not type(other) == int and not type(other) == float:
            raise TypeError("Operation only support float or integer values.")
        return Vector(self.x*other, self.y*other, self.z*other)

    def __rmul__(self, other):
        return self * other

    def __le__(self, other):
        self.tyer(other)
        return abs(self) <= abs(other)

    def __eq__(self, other):
        self.tyer(other)
        return abs(self) == abs(other)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __bool__(self):
        return bool(abs(self))

    def __getitem__(self, item):
        if type(item) == str and item.lower() in ['x', 'y', 'z']:
            return eval(f'self.{item.lower()}')
        return NotImplemented


v1 = Vector(2, 4, 6)
v2 = Vector(1, 3, 5)
v3 = Vector(0, 0, 0)
print(v1['Y'])
