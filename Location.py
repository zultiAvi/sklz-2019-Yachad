from math import sqrt
from MapObject import MapObject

class Location (MapObject):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        MapObject.__init__(self, self)

    def __add__(self, other):
        return Location(self.row + other.row, self.col + other.col)

    def __sub__(self, other):
        return Location(self.row - other.row, self.col - other.col)

    def __norm(self):
        return sqrt(self.row * self.row + self.col * self.col)

    def __mul__(self, factor):
        return Location(factor * self.row, factor * self.col)

    def __int_location(self):
        return Location (int(self.row), int(self.col))

    def add(self, other):
        return self + other

    def distance(self, other):
        return self.__norm(self-other)

    def equals(self, other):
        return self.row == other.row and self.col == other.col

    def in_range(self, other, dist):
        return self.distance(other) <= dist

    def multiply(self, factor):
        return self * factor

    def subtract(self, other):
        return self - other

    def towards(self, other, dist):
        if self.in_range(other, dist):
            return other

        vec = other - self
        vec = vec * (float(dist) / vec.__norm())
        return self + vec.__int_location()



