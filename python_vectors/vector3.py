from sqrt import sqrt
from vector2 import Vector2

class Vector3(Vector2):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def get_normalised(self):
        mag = self.get_magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def get_square_magnitude(self):
        return self.x**2 + self.y**2 + self.z**2

    def get_magnitude(self):
        return sqrt(self.get_square_magnitude())

    '''Arithmetic Operator Overloads'''

    def __str__(self):
        return f'Vector3({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3(x, y, z)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        z = self.z * other.z
        return Vector3(x, y, z)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        z = self.z / other.z
        return Vector3(x, y, z)

    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        z = self.z // other.z
        return Vector3(x, y, z)

    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        z = self.z % other.z
        return Vector3(x, y, z)

    '''Comparison Operator Overloads (inherited)'''