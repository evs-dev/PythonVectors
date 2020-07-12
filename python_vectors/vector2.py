from .sqrt import sqrt

class Vector2():
    """Representation of points and vectors in 2-dimensional space"""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_normalised(self):
        """Return the normalised version of the vector"""
        mag = self.get_magnitude()
        return Vector2(self.x / mag, self.y / mag)

    def get_normalized(self):
        """Return the normalized version of the vector
        (alias for get_normalised)"""
        return self.get_normalised()

    def get_square_magnitude(self):
        """Return the square magnitude (length) of the vector"""
        return self.x**2 + self.y**2

    def get_magnitude(self):
        """Return the magnitude (length) of the vector"""
        return sqrt(self.get_square_magnitude())

    # Arithmetic Operator Overloads

    def __str__(self):
        return f'Vector2({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector2(x, y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Vector2(x, y)

    def __floordiv__(self, other):
        x = self.x // other.x
        y = self.y // other.y
        return Vector2(x, y)

    def __mod__(self, other):
        x = self.x % other.x
        y = self.y % other.y
        return Vector2(x, y)

    # Comparison Operator Overloads

    def __lt__(self, other):
        self_mag = self.get_square_magnitude()
        other_mag = other.get_square_magnitude()
        return self_mag < other_mag

    def __le__(self, other):
        self_mag = self.get_square_magnitude()
        other_mag = other.get_square_magnitude()
        return self_mag <= other_mag

    def __gt__(self, other):
        return not self.__lt__(other)

    def __ge__(self, other):
        self_mag = self.get_square_magnitude()
        other_mag = other.get_square_magnitude()
        return self_mag >= other_mag

    def __eq__(self, other):
        self_mag = self.get_square_magnitude()
        other_mag = other.get_square_magnitude()
        return self_mag == other_mag

    def __ne__(self, other):
        return not self.__eq__(other)
