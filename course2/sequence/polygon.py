"""
https://www.udemy.com/course/python-3-deep-dive-part-2/learn/lecture/10515966#overview
"""
import math


class Polygon:
    def __init__(self, n, radius):
        if n < 3:
            raise ValueError('n must be larger than 2')
        self._n = n
        self._radius = radius

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        self._n = n

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        self._radius = radius

    @property
    def internal_angle(self):
        return (self._n - 2) * 180 / (self._n - 2)

    @property
    def edge_length(self):
        return 2 * self._radius * math.sin(math.pi / self._n)

    @property
    def apothem(self):
        return self._radius * math.cos(math.pi / self._n)

    @property
    def area(self):
        return self._n * self.edge_length * self.apothem / 2

    @property
    def perimeter(self):
        return self._n * self.edge_length

    def __repr__(self):
        return 'Polygon: n={}, radius={}'.format(self._n, self._radius)

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.n == other.n and self.radius == other.radius
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.n > other.n
        else:
            return NotImplemented


polygon1 = Polygon(3, 3)
polygon2 = Polygon(3, 3)
polygon3 = Polygon(4, 3)
print(polygon1)
print(polygon1 == polygon2)
print(polygon3 > polygon2)





