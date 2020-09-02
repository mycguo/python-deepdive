from pythondeepdive.course2.sequence.polygon import *


class Polygons:
    def __init__(self, n, radius):
        if n <= 3 or radius < 0:
            raise ValueError('invalid inputs of n {} or radius {}'.format(n, radius))
        self._n = n
        self._radius = radius

    def __getitem__(self, n):
        return Polygon(n + 3, self._radius)

    def __len__(self):
        return self._n - 2

    @property
    def max_eff(self):
        list_of_polygon = [Polygon(x, self._radius) for x in range(3, self._n + 1)]
        list_of_polygon.sort(key=lambda p: p.area/p.perimeter, reverse=True)
        return list_of_polygon[0]


polygons = Polygons(20, 3)
print(polygons.__getitem__(3))
print(polygons.max_eff)

