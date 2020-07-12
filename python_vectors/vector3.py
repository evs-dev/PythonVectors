from .sqrt import sqrt
from .vector2 import Vector2

class Vector3(Vector2):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def get_normalised(self):
        """Return the normalised version of the vector"""
        mag = self.get_magnitude()
        return Vector3(self.x / mag, self.y / mag, self.z / mag)

    def get_square_magnitude(self):
        """Return the square magnitude (length) of the vector"""
        return self.x**2 + self.y**2 + self.z**2

    def to_vector2(self):
        """Converts this Vector3 to Vector2, ignoring z attribute"""
        return Vector2(self.x, self.y)

    # Arithmetic Operator Overloads

    def __str__(self):
        return f'Vector3({self.x}, {self.y}, {self.z})'

    def __int__(self):
        return Vector3(int(self.x), int(self.y), int(self.z))

    def __iter__(self):
        return iter([self.x, self.y, self.z])

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

    # Comparison Operator Overloads (inherited)
