class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("width must be non negative")
        else:
            self._width = width

    def area(self):
        return self._width * self._height

    def __str__(self):
        return 'str width={0}, height={1}'.format(self._width,self._height)

    def __repr__(self):
        return 'repr Rectangle({0},{1})'.format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False


r1 = Rectangle(10, 20)
r1.area()
print(r1)
print(str(r1))
print(repr(r1))
r1.set_width(-10)
