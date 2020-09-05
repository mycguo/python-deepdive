class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin']

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        return CityIterator(self)


class CityIterator:
    def __init__(self, cities):
        self._city_object = cities
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            item = self._city_object.cities[self._index]
            self._index + 1
            return item

